# template: default
%global gem_name tzinfo

Name: rubygem-%{gem_name}
Version: 2.0.6
Release: 1%{?dist}
Summary: Time Zone Library
License: MIT
URL: https://tzinfo.github.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.3
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
TZInfo provides access to time zone data and allows times to be converted
using time zone rules.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Feb 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.0.6-1
- Update to 2.0.6

* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.0.5-1
- Update to 2.0.5

* Mon May 16 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.0.4-1
- Release rubygem-tzinfo 2.0.4

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.2.6-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.6-1
- Release rubygem-tzinfo 1.2.6

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.5-4
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.5-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.2.5-2
- Bump for moving over to foreman-packaging

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.5-1
- Initial package
