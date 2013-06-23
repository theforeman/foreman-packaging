%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from ruby2ruby-1.2.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby2ruby

%global rubyabi 1.9.1


Summary: Generate pure ruby from RubyParser compatible Sexps
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.1
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: http://seattlerb.rubyforge.org/ruby2ruby/
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygem(sexp_processor) >= 4.0
Requires: %{?scl_prefix}rubygem(ruby_parser)
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(sexp_processor)
BuildRequires: %{?scl_prefix}rubygem(ruby_parser)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
ruby2ruby provides a means of generating pure ruby code easily from
RubyParser compatible Sexps. This makes making dynamic language
processors in ruby easier than ever!

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

%build
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}
%{?scl:"}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Drop the standalone mode for tests - won't run that way due to missing 
# rubygems require anyway.
find %{buildroot}%{gem_instdir}/test -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/.*\/ruby.*/d'
find %{buildroot}%{gem_libdir} -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}%{gem_instdir} -type f | \
  xargs chmod 0644
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs chmod 0755
sed -i '1,$s/<ruby_parser>, \["~> 3.0.0"]/<ruby_parser>/g' %{buildroot}/%{gem_spec}

%files
%{_bindir}/r2r_show
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/.autotest
%{gem_instdir}/.gemtest
%{gem_instdir}/test
%{gem_docdir}

%changelog
* Wed Mar 20 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-5
- soften requires even in gemspec (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-4
- soften requires (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-3
- rebase to ruby2ruby-2.0.1 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-2
- add libdir macro to el6 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.1-1
- new package built with tito

* Fri Nov 30 2012 Mo Morsi <mmorsi@redhat.com> - 2.0.1-2
- Add missing file

* Fri Nov 30 2012 Mo Morsi <mmorsi@redhat.com> - 2.0.1-1
- Update to new upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.4-6
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 1.2.4-4
- replace BR(check) w/ BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 29 2009 Matthew Kent <mkent@magoazul.com> - 1.2.4-2
- Move pt_testcase.rb to the build stage so it's included in the rpm (#541512).
- Drop version requirements for sexp_processor and ruby_parser as they are new
  packages (#541512).

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 1.2.4-1
- Initial package
