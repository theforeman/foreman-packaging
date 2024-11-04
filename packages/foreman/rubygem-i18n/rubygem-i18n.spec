# template: default
%global gem_name i18n

Name: rubygem-%{gem_name}
Version: 1.14.6
Release: 1%{?dist}
Summary: New wave Internationalization support for Ruby
License: MIT
URL: https://github.com/ruby-i18n/i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems-devel >= 1.3.5
BuildArch: noarch
# end specfile generated dependencies

%description
New wave Internationalization support for Ruby.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.14.6-1
- Update to 1.14.6

* Sun May 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.14.5-1
- Update to 1.14.5

* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.14.4-1
- Update to 1.14.4

* Thu Jun 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.14.1-1
- Update to 1.14.1

* Sun Jun 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.14.0-1
- Update to 1.14.0

* Sun Apr 30 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.13.0-1
- Update to 1.13.0

* Sun Jul 17 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.12.0-1
- Update to 1.12.0

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.11.0-1
- Update to 1.11.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.8.2-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.2-1
- Release rubygem-i18n 1.8.2

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.0-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.0-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.4.0-2
- Bump for moving over to foreman-packaging

* Thu Jan 03 2019 Michael Moll <mmoll@mmoll.at> - 1.4.0-1
- Update to 1.4.0

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-1
- Initial package
