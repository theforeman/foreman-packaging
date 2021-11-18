%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_csv
%global confdir hammer

Summary: CSV input/output command plugin for the Hammer CLI
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.1
Release: 3%{?dist}
Group:   Development/Languages
License: GPLv3
URL:     https://github.com/Katello/hammer-cli-csv
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name} < 1.0.1-7
%endif
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_katello)

BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

%description
CSV input/output command plugin for the Hammer CLI.

%package doc
Summary:   Documentation for %{pkg_name}
Group:     Documentation
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 .%{gem_instdir}/config/csv.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/csv.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%{gem_instdir}/test
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/csv.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.3.1-3
- Rebuild for Ruby 2.7

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.3.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Apr 10 2018 Eric D. Helms <ericdhelms@gmail.com> 2.3.1-1
- Update hammer_cli_csv to 2.3.1

* Tue Jun 13 2017 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
- Fixes #19972 - Update hammer_cli_csv to 2.3.0 (akofink@redhat.com)
- Use gem_install macro (ericdhelms@gmail.com)

* Wed Jan 04 2017 Eric D Helms <ericdhelms@gmail.com> 2.2.1-1
- Update hammer_cli_csv to 2.2.1 (thomasmckay@redhat.com)

* Tue Dec 20 2016 Justin Sherrill <jsherril@redhat.com> 2.2.0-1
- Update hammer_cli_csv to 2.2.0 (thomasmckay@redhat.com)

* Fri Oct 14 2016 Eric D Helms <ericdhelms@gmail.com> 2.1.2-1
- Update hammer_cli_csv to 2.1.2 (thomasmckay@redhat.com)

* Mon Oct 03 2016 Justin Sherrill <jsherril@redhat.com> 2.1.1-1
- Update hammer_cli_csv to 2.1.1 (thomasmckay@redhat.com)

* Wed Aug 31 2016 Eric D Helms <ericdhelms@gmail.com> 2.1.0-1
- Update rubygem-hammer_cli_csv to 2.1.0 (#277) (eric.d.helms@gmail.com)

* Tue Mar 15 2016 Eric D Helms <ericdhelms@gmail.com> 2.0.0-2
- Remove requires on ruby(abi) for hammer_cli_csv (ericdhelms@gmail.com)

* Fri Mar 11 2016 Eric D Helms <ericdhelms@gmail.com> 2.0.0-1
- hammer_cli_csv-2.0.0 (thomasmckay@redhat.com)

* Fri Sep 04 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.1-8
- Update rubygem-hammer_cli_csv to tfm SCL (ericdhelms@gmail.com)

* Fri Jul 31 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.1-7
- Fixes #11259: Move hammer packages to SCL (ericdhelms@gmail.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.1-6
- new package built with tito

* Thu Mar 05 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-5
- Remove the Fedora check that evaluates to true on EL7 (ericdhelms@gmail.com)

* Thu Mar 05 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-4
- Remove gem_dir definition. (ericdhelms@gmail.com)

* Thu Mar 05 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-3
- Adding default configuration for tags. (ericdhelms@gmail.com)

* Thu Mar 05 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-2
- Adding basic releasers configuration for Koji. (ericdhelms@gmail.com)
- Switch to ReleaseTagger for tito (ericdhelms@gmail.com)
- Require rubygems-devel in all cases. (ericdhelms@gmail.com)

* Thu Mar 05 2015 Eric D. Helms <ericdhelms@gmail.com>
- Require rubygems-devel in all cases. (ericdhelms@gmail.com)

* Wed Mar 04 2015 Adam Price <komidore64@gmail.com> 1.0.0-1
- new package built with tito

* Wed Mar 26 2014 Mike McCune <mmccune@redhat.com> 0.0.1-1
- initial version (mmccune@redhat.com)
