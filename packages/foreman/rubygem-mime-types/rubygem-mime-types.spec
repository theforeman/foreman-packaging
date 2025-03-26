# template: default
%global gem_name mime-types

Name: rubygem-%{gem_name}
Version: 3.6.2
Release: 1%{?dist}
Summary: The mime-types library provides a library and registry for information about MIME content type definitions
License: MIT
URL: https://github.com/mime-types/ruby-mime-types/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: (rubygem(logger) or ruby-default-gems < 3.5)

# start specfile generated dependencies
Requires: ruby >= 2.0
BuildRequires: ruby >= 2.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
The mime-types library provides a library and registry for information about
MIME content type definitions. It can be used to determine defined filename
extensions for MIME types, or to use filename extensions to look up the likely
MIME type definitions.
Version 3.0 is a major release that requires Ruby 2.0 compatibility and
removes
deprecated functions. The columnar registry format introduced in 2.6 has been
made the primary format; the registry data has been extracted from this
library
and put into {mime-types-data}[https://github.com/mime-types/mime-types-data].
Additionally, mime-types is now licensed exclusively under the MIT licence and
there is a code of conduct in effect. There are a number of other smaller
changes described in the History file.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g logger

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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Wed Mar 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.6.2-1
- Update to 3.6.2

* Wed Mar 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.6.1-1
- Update to 3.6.1

* Tue Dec 10 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.6.0-1
- Update to 3.6.0

* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.5.2-1
- Update to 3.5.2

* Sun Sep 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.5.1-1
- Update to 3.5.1

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.5.0-1
- Update to 3.5.0

* Wed Jul 06 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.4.1-1
- Update to 3.4.1

* Mon Apr 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.3.1-2
- Rebuild against rh-ruby27

* Mon Mar 22 2021 Eric D. Helms <ericdhelms@gmail.com> 3.3.1-1
- Update to 3.3.1-1

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.2-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.2-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 3.2.2-2
- Bump for moving over to foreman-packaging

* Mon Aug 13 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.2-1
- Initial package
