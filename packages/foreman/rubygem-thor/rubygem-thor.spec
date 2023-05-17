# template: default
%global gem_name thor

Name: rubygem-%{gem_name}
Version: 1.2.2
Release: 1%{?dist}
Summary: Thor is a toolkit for building powerful command-line interfaces
License: MIT
URL: https://whatisthor.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems-devel >= 1.3.5
BuildArch: noarch
# end specfile generated dependencies

%description
Thor is a toolkit for building powerful command-line interfaces.


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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/thor
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/thor.gemspec

%changelog
* Wed May 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.2.2-1
- Update to 1.2.2

* Wed Jul 06 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.1-1
- Update to 1.2.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-3
- Rebuild against rh-ruby27

* Tue May 19 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.1-2
- Add missing obsoletes tfm-ror52 line

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.1-1
- Release rubygem-thor 1.0.1

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.20.0-6
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.20.0-5
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 0.20.0-4
- Bump for moving over to foreman-packaging

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.20.0-3
- Add missing gem_docdir

* Wed Aug 08 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.20.0-2
- Update for new gem_install

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.20.0-1
- Initial package
