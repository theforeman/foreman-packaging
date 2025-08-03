# template: hammer_plugin
%global gem_name hammer_cli_foreman_tasks
%global plugin_name foreman_tasks

%global hammer_confdir %{_sysconfdir}/hammer

Name: rubygem-%{gem_name}
Version: 0.0.23
Release: 1%{?foremandist}%{?dist}
Summary: Foreman CLI plugin for showing tasks information for resoruces and users
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-tasks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: hammer-cli-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Contains the code for showing of the tasks (results and progress) in the
Hammer CLI.


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

%changelog
* Sun Aug 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.0.23-1
- Update to 0.0.23

* Sun Feb 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.0.22-1
- Update to 0.0.22

* Tue Apr 16 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.0.21-1
- Update to 0.0.21

* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.0.20-1
- Update to 0.0.20

* Sun May 07 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.0.19-1
- Update to 0.0.19

* Wed Oct 19 2022 Evgeni Golov 0.0.18-1
- Update to 0.0.18-1

* Thu Jan 20 2022 Adam Ruzicka <aruzicka@redhat.com> 0.0.17-1
- Update to 0.0.17

* Fri Jul 23 2021 Adam Ruzicka <aruzicka@redhat.com> 0.0.16-1
- Update to 0.0.16

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.15-2
- Rebuild plugins for Ruby 2.7

* Mon May 18 2020 Ondrej Prazak <oprazak@redhat.com> 0.0.15-1
- Update to 0.0.15

* Tue Feb 18 2020 Ondrej Prazak <oprazak@redhat.com> 0.0.14-1
- Update to 0.0.14

* Tue Sep 18 2018 Ivan Nečas <inecas@redhat.com> 0.0.13-1
- Update to 0.0.13

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.12-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.0.12-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)

* Wed Oct 25 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.12-1
- Update hammer-cli-foreman-tasks 0.0.12 (inecas@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.10-2
- Use gem_install macro (dominic@cleal.org)

* Fri Feb 19 2016 Dominic Cleal <dominic@cleal.org> 0.0.10-1
- Release hammer_cli_foreman_tasks 0.0.10 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.9-2
- Add foremandist to hammer_cli_foreman_tasks (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.9-1
- Release hammer_cli_foreman_tasks 0.0.9 (stbenjam@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Sep 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-1
- update hammer_cli_foreman_tasks to 0.0.8 (RPM) (jsherril@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-3
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-2
- Increase range of non-SCL obsoletes to cover 1.9 versions (dcleal@redhat.com)

* Tue Aug 04 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Update rubygem-hammer_cli_foreman_tasks to 0.0.7 (ericdhelms@gmail.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Mon Apr 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Update hammer_cli_foreman_tasks to 0.0.6 (dcleal@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- new package built with tito
