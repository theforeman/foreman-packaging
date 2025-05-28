# template: default
%global gem_name foreman_maintain

%global directory_name foreman-maintain
%global dnfplugindir %{python3_sitelib}/dnf-plugins

Summary: The Foreman/Satellite maintenance tool
Name: rubygem-%{gem_name}
Version: 1.10.3
Release: 1%{?dist}
Epoch: 1
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman_maintain
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}.logrotate

# start specfile generated dependencies
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

Requires: hostname
Requires: yum-utils
Requires: /usr/bin/psql
Requires: nftables
Conflicts: satellite-maintain < 0.0.3
BuildRequires: python3-devel

Provides: foreman-maintain = %{version}

%description
foreman_maintain aims to provide various features that helps keeping
the Foreman/Satellite up and running. It supports multiple versions
and subparts of the Foreman infrastructure, including server or smart
proxy and is smart enough to provide the right tools for the specific
version.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}%{gem_instdir}/config/foreman-maintain.completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{gem_name}

install -d -m0750 %{buildroot}%{_localstatedir}/lib/%{directory_name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{directory_name}
install -d -m0750 %{buildroot}%{_sysconfdir}/%{directory_name}
install -D -m0640 %{buildroot}%{gem_instdir}/config/foreman_maintain.yml.packaging %{buildroot}%{_sysconfdir}/%{directory_name}/foreman_maintain.yml

install -D -m0644 %{buildroot}%{gem_instdir}/extras/foreman_protector/foreman-protector.conf %{buildroot}%{_sysconfdir}/yum/pluginconf.d/foreman-protector.conf
install -D -m0644 %{buildroot}%{gem_instdir}/extras/foreman_protector/foreman-protector.whitelist %{buildroot}%{_sysconfdir}/yum/pluginconf.d/foreman-protector.whitelist
install -D -m0644 %{buildroot}%{gem_instdir}/extras/foreman_protector/dnf/foreman-protector.py %{buildroot}%{dnfplugindir}/foreman-protector.py
install -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{gem_name}

%py_byte_compile %{__python3} %{buildroot}%{dnfplugindir}/foreman-protector.py

%files
%dir %{gem_instdir}
%{_bindir}/foreman-maintain
%{_bindir}/foreman-maintain-complete
%{_sysconfdir}/bash_completion.d/%{gem_name}
%{gem_instdir}/bin
%{gem_instdir}/definitions
%{gem_instdir}/lib
%{gem_instdir}/config
%{gem_instdir}/extras
%{dnfplugindir}/foreman-protector.py*
%{dnfplugindir}/__pycache__/foreman-protector.cpython*

%config(noreplace) %{_sysconfdir}/%{directory_name}
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/foreman-protector.conf
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/foreman-protector.whitelist
%config(noreplace) %{_sysconfdir}/logrotate.d/%{gem_name}
%{_localstatedir}/log/%{directory_name}
%{_localstatedir}/lib/%{directory_name}
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Mon Mar 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.10.3-1
- Update to 1.10.3

* Tue Feb 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.10.2-1
- Update to 1.10.2

* Sun Feb 16 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.10.1-1
- Update to 1.10.1

* Wed Jan 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.10.0-1
- Update to 1.10.0

* Wed Jan 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.9.2-1
- Update to 1.9.2

* Tue Dec 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.9.1-1
- Update to 1.9.1

* Mon Nov 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.9.0-1
- Update to 1.9.0

* Wed Nov 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.8.2-1
- Update to 1.8.2

* Thu Oct 24 2024 Evgeni Golov - 1:1.8.1-2
- Conflict satellite-maintain < 0.0.3

* Mon Oct 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.8.1-1
- Update to 1.8.1

* Thu Oct 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.8.0-1
- Update to 1.8.0

* Thu Sep 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.7.5-1
- Update to 1.7.5

* Wed Sep 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.7.4-1
- Update to 1.7.4

* Thu Aug 29 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.7.3-1
- Update to 1.7.3

* Mon Aug 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.7.2-1
- Update to 1.7.2

* Wed Aug 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.7.1-1
- Update to 1.7.1

* Tue Aug 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.7.0-1
- Update to 1.7.0

* Mon Aug 05 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.14-1
- Update to 1.6.14

* Mon Jul 22 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.13-1
- Update to 1.6.13

* Thu Jul 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.12-1
- Update to 1.6.12

* Wed Jun 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.11-1
- Update to 1.6.11

* Mon Jun 17 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.10-1
- Update to 1.6.10

* Wed Jun 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.9-1
- Update to 1.6.9

* Thu Jun 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.8-1
- Update to 1.6.8

* Mon May 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.7-1
- Update to 1.6.7

* Wed May 01 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.6-1
- Update to 1.6.6

* Wed Apr 17 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.4-1
- Update to 1.6.4

* Sun Apr 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.3-1
- Update to 1.6.3

* Thu Apr 04 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.6.2-2
- Add dependency on hostname

* Sun Mar 31 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.2-1
- Update to 1.6.2

* Mon Mar 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.1-1
- Update to 1.6.1

* Mon Mar 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.6.0-1
- Update to 1.6.0

* Sun Feb 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1:1.5.1-1
- Update to 1.5.1

* Wed Jan 03 2024 Foreman Packaging Automation <packaging@theforeman.org> 1:1.5.0-1
- Update to 1.5.0

* Thu Dec 14 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.4.4-1
- Update to 1.4.4

* Mon Nov 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.4.3-1
- Update to 1.4.3

* Thu Oct 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.4.2-1
- Update to 1.4.2

* Fri Oct 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.4.1-1
- Update to 1.4.1

* Wed Sep 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.4.0-1
- Update to 1.4.0

* Wed Aug 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.3.5-1
- Update to 1.3.5

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.3.4-1
- Update to 1.3.4

* Wed Jul 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.3.3-1
- Update to 1.3.3

* Tue Jun 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.3.2-1
- Update to 1.3.2

* Thu Apr 27 2023 Eric D. Helms <ericdhelms@gmail.com> - 1:1.3.1-1
- Release rubygem-foreman_maintain 1.3.1

* Tue Mar 28 2023 Eric D. Helms <ericdhelms@gmail.com> - 1:1.3.0-1
- Release rubygem-foreman_maintain 1.3.0

* Tue Mar 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.2.8-1
- Update to 1.2.8

* Wed Mar 08 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.2.7-1
- Update to 1.2.7

* Thu Feb 23 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.2.6-1
- Update to 1.2.6

* Wed Feb 22 2023 Eric D. Helms <ericdhelms@gmail.com> 1:1.2.5-1
- Update to 1.2.5

* Wed Feb 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.2.4-1
- Update to 1.2.4

* Thu Jan 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.2.3-1
- Update to 1.2.3

* Tue Jan 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1:1.2.2-1
- Update to 1.2.2

* Fri Nov 18 2022 Evgeni Golov 1:1.2.1-1
- Update to 1.2.1

* Tue Nov 01 2022 Eric D. Helms <ericdhelms@gmail.com> - 1:1.2.0-1
- Release 1.2.0

* Thu Oct 06 2022 Eric D. Helms <ericdhelms@gmail.com> - 1:1.1.8-1
- Release rubygem-foreman_maintain 1.1.8

* Mon Aug 15 2022 Evgeni Golov - 1:1.1.3-2
- Fixes #35366 - make foreman-protector work as non-root

* Fri Jul 01 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.1.3-1
- Update to 1.1.3

* Fri Jul 01 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.1.2-1
- Update to 1.1.2

* Tue May 03 2022 Evgeni Golov - 1:1.1.1-3
- Adjust psql requires to use SCL'ed version on EL7

* Mon May 02 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.1.1-2
- Add requires of psql utility

* Wed Apr 27 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.1.1-1
- Update to 1.1.1

* Fri Apr 22 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.8-1
- Update to 1.0.8 and update yum and dnf foreman-protector file paths

* Wed Apr 20 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.7-2
- Require nftables for newer than EL7 operating systems

* Wed Apr 06 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.7-1
- Update to 1.0.7

* Wed Mar 30 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.6-1
- Update to 1.0.6

* Wed Mar 30 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.5-1
- Update to 1.0.5

* Wed Mar 09 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.4-1
- Update to 1.0.4

* Wed Feb 09 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.3-1
- Update to 1.0.3

* Wed Jan 26 2022 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.2-1
- Update to 1.0.2

* Mon Dec 13 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.1-1
- Update to 1.0.1

* Fri Dec 03 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:1.0.0-1
- Update to 1.0.0

* Wed Nov 24 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.9.3-1
- Update to 0.9.3

* Wed Nov 10 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.9.2-1
- Update to 0.9.2

* Wed Oct 20 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.9.1-1
- Update to 0.9.1

* Tue Oct 19 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.20-1
- Update to 0.8.20

* Wed Oct 06 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.19-1
- Update to 0.8.19

* Fri Oct 01 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.18-1
- Update to 0.8.18

* Wed Sep 22 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.17-1
- Update to 0.8.17

* Fri Sep 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:0.8.16-1
- Release rubygem-foreman_maintain 0.8.16

* Thu Sep 09 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.15-1
- Update to 0.8.15

* Wed Sep 08 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.14-1
- Update to 0.8.14

* Tue Aug 31 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:0.8.13-2
- Drop requires on facter

* Tue Aug 31 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.13-1
- Update to 0.8.13

* Wed Aug 25 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:0.8.12-2
- Add requires on facter

* Wed Aug 25 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.12-1
- Update to 0.8.12

* Wed Aug 25 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.11-1
- Update to 0.8.11

* Tue Aug 03 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.10-1
- Update to 0.8.10

* Fri Jul 30 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.9-2
- Add logrotate configuration file

* Tue Jul 27 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.9-1
- Update to 0.8.9

* Tue Jul 27 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.8-1
- Update to 0.8.8

* Mon Jul 19 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.7-1
- Update to 0.8.7

* Tue Jul 13 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.6-1
- Update to 0.8.6

* Fri Jul 09 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.5-1
- Update to 0.8.5

* Thu Jul 08 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.4-1
- Update to 0.8.4

* Tue Jul 06 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.3-1
- Update to 0.8.3

* Wed Jun 16 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.2-1
- Update to 0.8.2

* Mon May 10 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.1-1
- Update to 0.8.1

* Fri Apr 09 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.8.0-1
- Update to 0.8.0

* Thu Mar 25 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.9-1
- Update to 0.7.9

* Mon Mar 22 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.8-1
- Update to 0.7.8

* Mon Mar 08 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.7-1
- Update to 0.7.7

* Tue Mar 02 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.6-1
- Update to 0.7.6

* Thu Feb 04 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.5-1
- Update to 0.7.5

* Mon Jan 11 2021 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.4-1
- Update to 0.7.4

* Wed Dec 23 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.2-1
- Update to 0.7.2

* Fri Dec 04 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.1-1
- Update to 0.7.1

* Wed Dec 02 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.7.0-1
- Update to 0.7.0

* Tue Sep 22 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.13-1
- Update to 0.6.13

* Mon Sep 21 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.12-1
- Update to 0.6.12

* Thu Sep 10 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.11-1
- Update to 0.6.11

* Fri Sep 04 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.10-1
- Update to 0.6.10

* Mon Aug 03 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.9-1
- Update to 0.6.9

* Wed Jul 08 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.8-1
- Update to 0.6.8

* Wed Jul 08 2020 Suraj Patil <patilsuraj767@gmail.com> 1:0.6.8-1
- Fixes #30342 - fix snapshot backup dir detection

* Wed Jul 08 2020 Bernhard Suttner <bernhard.suttner@atix.de> - 1:0.6.8-1
- Fixes #30324 - check for http(s) proxy

* Wed Jul 08 2020 Kavita Gaikwad <kavitagaikwad103@gmail.com> - 1:0.6.8-1
- Fixes #30276 - handle nil case while updating all packages

* Thu Jun 25 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.6-1
- Update to 0.6.6

* Wed Jun 03 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.5-1
- Update to 0.6.5

* Wed May 27 2020 kgaikwad <kavitagaikwad103@gmail.com> 1:0.6.4-1
- Update to 0.6.4

* Wed Apr 08 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:0.6.3-2
- Build for EL8

* Thu Apr 02 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.3-1
- Update to 0.6.3

* Fri Mar 13 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.2-1
- Update to 0.6.2

* Fri Mar 06 2020 Amit Upadhye <upadhyeammit@gmail.com> 1:0.6.1-1
- Release rubygem-foreman_maintain 0.6.1

* Wed Jan 29 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:0.6.0-1
- Release rubygem-foreman_maintain 0.6.0

* Fri Jan 10 2020 kgaikwad <kavitagaikwad103@gmail.com> 1:0.5.1-1
- Update to 0.5.1

* Tue Nov 19 2019 Martin Bacovsky <mbacovsk@redhat.com> 1:0.5.0-1
- Update to 0.5.0

* Thu Sep 12 2019 Martin Bacovsky <mbacovsk@redhat.com> 1:0.4.9-1
- Update to 0.4.9

* Thu Sep 05 2019 Martin Bacovsky <mbacovsk@redhat.com> 1:0.4.8-1
- Update to 0.4.8

* Fri Jul 12 2019 Evgeni Golov - 1:0.4.5-1
- Update to 0.4.5

* Tue Jul 02 2019 Evgeni Golov 1:0.4.4-1
- Update to 0.4.4

* Mon Jun 10 2019 Martin Bacovsky <mbacovsk@redhat.com> 0.4.3-1
- Update to 0.4.3

* Mon May 20 2019 Martin Bacovsky <mbacovsk@redhat.com> 0.4.2-1
- Update to 0.4.2

* Fri Mar 01 2019 Martin Bacovsky <mbacovsk@redhat.com> 0.4.1-1
- Update to 0.4.1

* Thu Jan 31 2019 Ivan Nečas <inecas@redhat.com> 0.3.1-1
- Update to 0.3.1

* Thu Nov 08 2018 Ivan Nečas <inecas@redhat.com> 0.3.0-1
- Update to 0.3.0

* Thu Oct 18 2018 Ivan Nečas <inecas@redhat.com> 0.2.12-1
- Update to 0.2.12

* Tue Sep 25 2018 Ivan Nečas <inecas@redhat.com> 0.2.11-1
- Update to 0.2.11

* Wed Sep 19 2018 Ivan Nečas <inecas@redhat.com> 0.2.9-2
- Ship /etc/passenger-recycler.yaml

* Fri Sep 07 2018 Ivan Nečas <inecas@redhat.com> 0.2.9-1
- Update to 0.2.9

* Mon Aug 20 2018 Martin Bacovsky <mbacovsk@redhat.com> 0.2.8-1
- Update to 0.2.8
- Added bash completion
- Update shebang only in ruby scripts

* Wed Aug 15 2018 Ivan Nečas <inecas@redhat.com> 0.2.7-1
- Update to 0.2.7

* Tue Jul 31 2018 Ivan Nečas <inecas@redhat.com> 0.2.6-1
- Update to 0.2.6

* Thu Jul 26 2018 Martin Bacovsky <mbacovsk@redhat.com> 0.2.5-1
- Update to 0.2.5

* Thu Jul 12 2018 Ivan Nečas <inecas@redhat.com> 0.2.4-1
- Update to 0.2.4

* Fri May 18 2018 Ivan Nečas <inecas@redhat.com> 0.2.2-1
- Update to 0.2.2

* Thu May 03 2018 Ivan Nečas <inecas@redhat.com> 0.2.1-1
- Update to 0.2.1

* Wed Apr 4 2018 Sean o'Keeffe <seanokeeffe797@gmail.com> 0.1.5-2
- Provide foreman-maintain & foreman_maintain (seanokeeffe797@gmail.com)

* Wed Jan 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.3-1
- Update foreman_maintain to 0.1.3 (inecas@redhat.com)

* Wed Jan 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.2-1
- Ref #19496 - Install passenger-recycler (imswapab@gmail.com)

* Tue Dec 12 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.1-1
- Update rubygem-foreman_maintain to 0.1.1 (gnurag@gmail.com)

* Thu Nov 02 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.11-1
- Update foreman_maintain to 0.0.11 (inecas@redhat.com)

* Wed Oct 18 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.10-1
- Update foreman_maintain to 0.0.10 (inecas@redhat.com)

* Thu Sep 14 2017 Anurag Patel <apatel@redhat.com> 0.0.9-1
- Updated gem version to 0.0.9

* Tue Aug 29 2017 Anurag Patel <apatel@redhat.com> 0.0.8-1
- Updated gem version to 0.0.8, with upgrade scenario updates.

* Mon Aug 21 2017 Anurag Patel <apatel@redhat.com> 0.0.7-1
- Updated gem version to 0.0.7, that includes full upgrade path support.

* Tue Jul 25 2017 Anurag Patel <apatel@redhat.com> 0.0.6-1
- Updated gem version to 0.0.6, that fixes an issue with config file location.

* Thu Jul 06 2017 Anurag Patel <apatel@redhat.com> 0.0.5-4
- Updated spec to support config file, data and log dirs.

* Fri Jun 16 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.3-1
- new package built with tito

* Tue May 23 2017 Anurag Patel <apatel@redhat.com> 0.0.3-1
- Updated foreman_maintain with 0.0.3 tag.

* Mon Mar 20 2017 Anurag Patel <apatel@redhat.com> 0.0.2-1
- Updated foreman_maintain with 0.0.2 tag.

* Mon Feb 27 2017 Anurag Patel <apatel@redhat.com> 0.0.1-1
- Package foreman_maintain into RPM (#3, apatel@redhat.com)

