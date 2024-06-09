# template: default
%global gem_name railties

Name: rubygem-%{gem_name}
Version: 6.1.7.8
Release: 1%{?dist}
Summary: Tools for creating, working with, and running Rails applications
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Recommends: rubygem(irb)
# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Rails internals: application bootup, plugins, generators, and rake tasks.


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

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rails
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/RDOC_MAIN.rdoc
%doc %{gem_instdir}/README.rdoc

%changelog
* Sun Jun 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.7.8-1
- Update to 6.1.7.8

* Wed Apr 03 2024 Eric D. Helms <ericdhelms@gmail.com> - 6.1.7.7-2
- Require rubygem-irb

* Thu Feb 29 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.7.7-1
- Update to 6.1.7.7

* Sun Aug 27 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.6-1
- Update to 6.1.7.6

* Sun Jul 02 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.4-1
- Update to 6.1.7.4

* Tue Mar 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.3-1
- Update to 6.1.7.3

* Fri Jan 27 2023 Eric D. Helms <ericdhelms@gmail.com> - 6.1.7.2-1
- Release rubygem-railties 6.1.7.2

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.1-1
- Update to 6.1.7.1

* Sun Nov 20 2022 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7-1
- Update to 6.1.7

* Thu Jul 14 2022 Evgeni Golov - 6.1.6.1-1
- Release rubygem-railties 6.1.6.1

* Mon May 16 2022 Eric D. Helms <ericdhelms@gmail.com> - 6.1.6-1
- Release rubygem-railties 6.1.6

* Fri Mar 18 2022 Eric D. Helms <ericdhelms@gmail.com> - 6.0.4.7-1
- Release rubygem-railties 6.0.4.7

* Mon May 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.7-1
- Release 6.0.3.7

* Wed Mar 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.5-2
- Rebuild against rh-ruby27

* Tue Feb 23 2021 Evgeni Golov - 6.0.3.5-1
- Release rubygem-railties 6.0.3.5

* Mon Oct 26 2020 Evgeni Golov - 6.0.3.4-1
- Release rubygem-railties 6.0.3.4

* Mon Jun 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.1-1
- Release rubygem-railties 6.0.3.1

* Tue Apr 28 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.0.2.2-1
- Update to 6.0.2.2

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.0.2.1-1
- Release rubygem-railties 6.0.2.1

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 5.2.1-2
- Bump for moving over to foreman-packaging

* Wed Aug 22 2018 Eric D. Helms <ericdhelms@gmail.com> 5.2.1-1
- Release tfm-ror52-rubygem-railties 5.2.1

* Fri Aug 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-2
- Fix rake requires

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-1
- Initial package
