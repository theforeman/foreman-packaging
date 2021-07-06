%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_maintain
%global directory_name foreman-maintain
%global yumplugindir %{_prefix}/lib%{nil}/yum-plugins

%{!?_root_bindir:%global _root_bindir %{_bindir}}

Summary: The Foreman/Satellite maintenance tool
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.8.3
Release: 1%{?dist}
Epoch: 1
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman_maintain
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(clamp) >= 0.6.2
Requires: %{?scl_prefix}rubygem(highline)
Requires: yum-utils
%if 0%{?rhel} < 8
BuildRequires: python2-devel
%else
BuildRequires: python3-devel
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: %{gem_name} = %{version}
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
Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
sed -i '1s@/.*ruby.*@/usr/bin/%{?scl_prefix}ruby@' .%{_bindir}/*
mkdir -p %{buildroot}%{_root_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_root_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}%{gem_instdir}/config/foreman-maintain.completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{gem_name}

install -d -m0750 %{buildroot}%{_localstatedir}/lib/%{directory_name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{directory_name}
install -d -m0750 %{buildroot}%{_sysconfdir}/%{directory_name}
install -D -m0640 %{buildroot}%{gem_instdir}/config/foreman_maintain.yml.packaging %{buildroot}%{_sysconfdir}/%{directory_name}/foreman_maintain.yml
install -D -m0640 %{buildroot}%{gem_instdir}/config/passenger-recycler.yaml %{buildroot}%{_sysconfdir}/passenger-recycler.yaml

install -D -m0640 %{buildroot}%{gem_instdir}/extras/foreman_protector/foreman-protector.conf %{buildroot}%{_sysconfdir}/yum/pluginconf.d/foreman-protector.conf
install -D -m0640 %{buildroot}%{gem_instdir}/extras/foreman_protector/foreman-protector.whitelist %{buildroot}%{_sysconfdir}/yum/pluginconf.d/foreman-protector.whitelist
install -D -m0640 %{buildroot}%{gem_instdir}/extras/foreman_protector/foreman-protector.py %{buildroot}%{yumplugindir}/foreman-protector.py

%if 0%{?rhel} < 8
%py_byte_compile %{__python2} %{buildroot}%{yumplugindir}/foreman-protector.py
%else
%py_byte_compile %{__python3} %{buildroot}%{yumplugindir}/foreman-protector.py
%endif

%files
%dir %{gem_instdir}
%{_root_bindir}/foreman-maintain
%{_root_bindir}/foreman-maintain-complete
%{_root_bindir}/foreman-maintain-rotate-tar
%{_root_bindir}/passenger-recycler
%{_sysconfdir}/bash_completion.d/%{gem_name}
%{gem_instdir}/bin
%{gem_instdir}/definitions
%{gem_instdir}/lib
%{gem_instdir}/config
%{gem_instdir}/extras
%{yumplugindir}/foreman-protector.py*

%if 0%{?rhel} > 7
%{yumplugindir}/__pycache__/foreman-protector.cpython*
%endif

%config(noreplace) %{_sysconfdir}/%{directory_name}
%config(noreplace) %{_sysconfdir}/passenger-recycler.yaml
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/foreman-protector.conf
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/foreman-protector.whitelist
%{_localstatedir}/log/%{directory_name}
%{_localstatedir}/lib/%{directory_name}
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
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

