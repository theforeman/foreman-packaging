%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_virt_who_configure
%global confdir hammer

Summary: Hammer CLI commands for configuring Virt Who for Katello
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.7
Release: 2%{?dist}
Group:   Development/Languages
License: GPLv3
URL:     https://github.com/theforeman/hammer-cli-foreman-virt-who-configure
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli) >= 0.5.0
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) >= 0.5.0

BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

%description
Hammer CLI commands for configuring Virt Who for Katello

%package doc
Summary:   Documentation for %{pkg_name}
Group:     Documentation
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
install -m 644 .%{gem_instdir}/config/foreman_virt_who_configure.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_virt_who_configure.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
# once we get i18n strings
%{gem_instdir}/locale
%{gem_instdir}/test
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_virt_who_configure.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.7-2
- Rebuild for Ruby 2.7

* Mon Dec 14 2020 Jonathon Turel <jturel@gmail.com> 0.0.7-1
- Update to 0.0.7

* Fri Mar 13 2020 Marek Hulan <mhulan@redhat.com> 0.0.6-1
- Update to 0.0.6

* Wed Nov 27 2019 Marek Hulan <mhulan@redhat.com> 0.0.5-1
- Update to 0.0.5

* Wed Sep 04 2019 Marek Hulan <mhulan@redhat.com> 0.0.4-1
- Update to 0.0.4

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.3-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 0.0.3-2
- new package built with tito

* Mon Jun 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.3-1
- Update hammer_cli_foreman_virt_who_configure to 0.0.3 (tstrachota@redhat.com)

* Wed Jun 07 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.2-1
- new package built with tito

