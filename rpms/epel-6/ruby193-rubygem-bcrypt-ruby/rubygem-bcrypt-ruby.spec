%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from bcrypt-ruby-2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bcrypt-ruby

%global rubyabi 1.9.1

Summary: Wrapper around bcrypt() password hashing algorithm
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 3.0.1
Release: 7%{?dist}
Group: Development/Languages
# ext/* - Public Domain
# spec/TestBCrypt.java - ISC
License: MIT and Public Domain and ISC
URL: http://bcrypt-ruby.rubyforge.org
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygem(rspec)
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project
for hashing passwords. bcrypt-ruby provides a simple, humane wrapper for
safely handling
passwords.


%prep
%setup -q -c -T

%build
mkdir -p ./%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %scl "}
gem install --local --install-dir ./%{gem_dir} \
            --force -V --rdoc %{SOURCE0}
%{?scl:"}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir}/lib
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mv %{buildroot}%{gem_libdir}/bcrypt_ext.so %{buildroot}%{gem_extdir}/lib

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl "}
rspec spec
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/bcrypt-ruby.gemspec
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/COPYING
%exclude %{gem_instdir}/ext
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_extdir}
%{gem_instdir}/spec
%doc %{gem_docdir}
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.1-7
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.1-6
- Specfile cleanup.

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.1-5
- Rebuilt for scl.

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.1-4
- Fixed wrong provide.

* Mon Jan 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.1-1
- Update to bcrypt-ruby 3.0.1.

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 2.1.2-4
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Mohammed Morsi <mmorsi@redhat.com> - 2.1.2-2
- Updates / fixes based on review feedback
- Fixed bcrypt_ext.so install location

* Tue Aug 10 2010 Mohammed Morsi <mmorsi@redhat.com> - 2.1.2-1
- Initial package
