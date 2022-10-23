# template: default
%global gem_name googleauth

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 1%{?dist}
Summary: Google Auth Library for Ruby
License: Apache-2.0
URL: https://github.com/googleapis/google-auth-library-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Implements simple authorization for accessing Google APIs, and provides
support for Application Default Credentials.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md

%changelog
* Sun Oct 23 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.3.0-1
- Update to 1.3.0

* Wed Jul 13 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.0-1
- Update to 1.2.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.13.1-2
- Rebuild against rh-ruby27

* Thu Oct 08 2020 Ondřej Ezr <oezr@redhat.com> 0.13.1-1
- Update to 0.13.1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.6.7-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.6.7-2
- Update spec to remove the ror scl

* Thu Mar 14 2019 kgaikwad <kavitagaikwad103@gmail.com> 0.6.7-1
- Add rubygem-googleauth generated by gem2rpm using the scl template

