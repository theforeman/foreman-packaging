# template: default
%global gem_name mime-types-data

Name: rubygem-%{gem_name}
Version: 3.2025.0805
Release: 1%{?dist}
Summary: mime-types-data provides a registry for information about MIME media type definitions
License: MIT
URL: https://github.com/mime-types/mime-types-data/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0
BuildRequires: ruby >= 2.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.


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
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENCE.md
%exclude %{gem_instdir}/Manifest.txt
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Rakefile

%changelog
* Thu Aug 07 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0805-1
- Update to 3.2025.0805

* Sun Aug 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0729-1
- Update to 3.2025.0729

* Wed Jul 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0722-1
- Update to 3.2025.0722

* Fri Jul 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0715-1
- Update to 3.2025.0715

* Sun Jul 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0708-1
- Update to 3.2025.0708

* Sun Jul 06 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0701-1
- Update to 3.2025.0701

* Wed Jun 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0624-1
- Update to 3.2025.0624

* Sun Jun 22 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0617-1
- Update to 3.2025.0617

* Sun Jun 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0610-1
- Update to 3.2025.0610

* Sun Jun 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0603-1
- Update to 3.2025.0603

* Sun Jun 01 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0527-1
- Update to 3.2025.0527

* Sun May 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0520-1
- Update to 3.2025.0520

* Sun May 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0514-1
- Update to 3.2025.0514

* Thu May 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0507-1
- Update to 3.2025.0507

* Sun May 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0429-1
- Update to 3.2025.0429

* Tue Apr 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0422-1
- Update to 3.2025.0422

* Sun Apr 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0415-1
- Update to 3.2025.0415

* Thu Apr 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0402-1
- Update to 3.2025.0402

* Wed Mar 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0325-1
- Update to 3.2025.0325

* Thu Mar 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0318-1
- Update to 3.2025.0318

* Sun Mar 09 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0304-1
- Update to 3.2025.0304

* Sun Feb 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0220-1
- Update to 3.2025.0220

* Sun Feb 09 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0204-1
- Update to 3.2025.0204

* Wed Jan 15 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.2025.0107-1
- Update to 3.2025.0107

* Sun Dec 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2024.1203-1
- Update to 3.2024.1203

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2024.1105-1
- Update to 3.2024.1105

* Sun Sep 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2024.0903-1
- Update to 3.2024.0903

* Sun Aug 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2024.0806-1
- Update to 3.2024.0806

* Sun May 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2024.0507-1
- Update to 3.2024.0507

* Sun Feb 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2024.0206-1
- Update to 3.2024.0206

* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2023.1205-1
- Update to 3.2023.1205

* Sun Nov 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.2023.1003-1
- Update to 3.2023.1003

* Sun Aug 27 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.2023.0808-1
- Update to 3.2023.0808

* Wed Feb 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.2023.0218.1-1
- Update to 3.2023.0218.1

* Wed Jul 06 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.2022.0105-1
- Update to 3.2022.0105

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.2018.0812-5
- Rebuild against rh-ruby27

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2018.0812-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2018.0812-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 3.2018.0812-2
- Bump for moving over to foreman-packaging

* Mon Aug 13 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2018.0812-1
- Initial package
