# template: hammer_plugin
%global gem_name hammer_cli_foreman_openscap
%global plugin_name foreman_openscap

%global hammer_confdir %{_sysconfdir}/hammer

Name: rubygem-%{gem_name}
Version: 0.2.2
Release: 1%{?foremandist}%{?dist}
Summary: Foreman OpenSCAP commands for Hammer
License: GPLv3
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: hammer-cli-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Foreman OpenSCAP commands for Hammer.


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

mkdir -p %{buildroot}%{hammer_confdir}/cli.modules.d
install -m 0644 .%{gem_instdir}/config/%{plugin_name}.yml \
                %{buildroot}%{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config
%{gem_instdir}/test

%changelog
* Sun Feb 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.2.2-1
- Update to 0.2.2

* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.2.1-1
- Update to 0.2.1

* Fri Dec 15 2023 Oleh Fedorenko <ofedoren@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Oct 19 2022 Evgeni Golov 0.1.13-2
- Regenerate spec based on latest template

* Fri Jul 23 2021 Ondrej Prazak <oprazak@redhat.com> 0.1.13-1
- Update to 0.1.13

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.12-2
- Rebuild plugins for Ruby 2.7

* Mon Dec 07 2020 Ondrej Prazak <oprazak@redhat.com> 0.1.12-1
- Update to 0.1.12

* Tue Jul 28 2020 Ondrej Prazak <oprazak@redhat.com> 0.1.11-1
- Update to 0.1.11

* Mon Mar 02 2020 Ondrej Prazak <oprazak@redhat.com> 0.1.10-1
- Update to 0.1.10

* Tue Feb 18 2020 Ondrej Prazak <oprazak@redhat.com> 0.1.9-1
- Update to 0.1.9

* Thu May 23 2019 Ondrej Prazak <oprazak@redhat.com> 0.1.8-1
- Update to 0.1.8

* Tue Mar 19 2019 Marek Hulan <mhulan@redhat.com> 0.1.7-1
- Update to 0.1.7

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.6-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Apr 06 2018 Marek Hulan <mhulan@redhat.com> 0.1.6-1
- Update to 0.1.6

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.1.5-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Sep 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.5-1
- Update hammer_cli_foreman_openscap to 0.1.5 (mhulan@redhat.com)

* Wed Jul 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.4-1
- Update hammer_cli_foreman_openscap to 0.1.4 (mhulan@redhat.com)

* Wed Mar 15 2017 Dominic Cleal <dominic@cleal.org> 0.1.3-1
- Update hammer_cli_foreman_openscap to 0.1.3 (mhulan@redhat.com)

* Wed Oct 19 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- Update hammer_cli_foreman_openscap to 0.1.2 (oprazak@redhat.com)

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> 0.1.1-1
- new package built with tito

