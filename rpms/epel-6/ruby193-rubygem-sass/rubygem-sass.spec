%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from sass-3.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sass

%global rubyabi 1.9.1

Summary: A powerful but elegant CSS compiler that makes CSS fun again
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2.13
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://sass-lang.com/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Sass makes CSS fun again. Sass is an extension of CSS3, adding
nested rules, variables, mixins, selector inheritance, and more.
It's translated to well-formatted, standard CSS using the
command line tool or a web-framework plugin.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
# Remove bundled rubygem-listener:
# https://github.com/nex3/sass/issues/458
rm -rf vendor
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
export LANG=en_US.utf8
%{?scl:scl enable %{scl} "}
find -type f -name *_test.rb | xargs testrb -Itest
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%{_bindir}/sass
%{_bindir}/sass-convert
%{_bindir}/scss
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/init.rb
%{gem_instdir}/rails/init.rb
%{gem_instdir}/extra/update_watch.rb
%{gem_instdir}/VERSION
%{gem_instdir}/VERSION_DATE
%{gem_instdir}/VERSION_NAME
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/CONTRIBUTING
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/REVISION
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Sun Dec 29 2013 Dominic Cleal <dcleal@redhat.com> 3.2.13-1
- Update to sass 3.2.13 (dcleal@redhat.com)
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 3.1.20-3
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1.20-2
- Rebuilt for SCL.

* Mon Jul 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.1.20-1
- Update to sass 3.1.20.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1.7-6
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Chris Lalancette <clalance@redhat.com> - 3.1.4-4
- Add patches to make sass work in Fedora

* Thu Jul 21 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.4-3
- changed ruby(fssm) dep to rubygem(fssm)

* Thu Jul 14 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.4-2
- corrected license, whitespace fixes

* Wed Jul 13 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.4-1
- Initial package
