# template: default
%global gem_name mime-types-data

Name: rubygem-%{gem_name}
Version: 3.2024.1203
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
%doc %{gem_instdir}/Code-of-Conduct.md
%license %{gem_instdir}/Licence.md
%exclude %{gem_instdir}/Manifest.txt
%{gem_instdir}/data
%{gem_libdir}
%{gem_instdir}/types
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Contributing.md
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Rakefile

%changelog
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
