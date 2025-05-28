# template: hammer_plugin
%global gem_name hammer_cli_foreman_remote_execution
%global plugin_name foreman_remote_execution

%global hammer_confdir %{_sysconfdir}/hammer

Name: rubygem-%{gem_name}
Version: 0.3.2
Release: 1%{?foremandist}%{?dist}
Summary: CLI for the Foreman remote execution plugin
License: GPLv3+
URL: https://github.com/theforeman/hammer_cli_foreman_remote_execution
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
This gem provides CLI support for the Foreman remote execution plugin.


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
* Tue Feb 25 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.2-1
- Update to 0.3.2

* Tue Jan 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.0-1
- Update to 0.3.0

* Sun Feb 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.2.3-1
- Update to 0.2.3

* Fri Jul 23 2021 Adam Ruzicka <aruzicka@redhat.com> 0.2.2-1
- Update to 0.2.2

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.2.1-2
- Rebuild plugins for Ruby 2.7

* Wed Dec 09 2020 Adam Ruzicka <aruzicka@redhat.com> 0.2.1-1
- Update to 0.2.1

* Mon Nov 09 2020 Adam Ruzicka <aruzicka@redhat.com> 0.2.0-1
- Update to 0.2.0

* Tue May 26 2020 Evgeni Golov 0.1.2-1
- Update to 0.1.2

* Tue Feb 18 2020 Ondrej Prazak <oprazak@redhat.com> 0.1.1-1
- Update to 0.1.1

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jun 04 2018 Adam Ruzicka <aruzicka@redhat.com> 0.1.0-1
- Update to 0.1.0

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.0.6-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Aug 16 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.6-1
- Update rubygem-hammer_cli_foreman_remote_execution to 0.0.6
  (aruzicka@redhat.com)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.5-2
- Use gem_install macro (dominic@cleal.org)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.5-1
- Release hammer_cli_foreman_remote_execution 0.0.5 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release hammer_cli_foreman_remote_execution 0.0.4 (stbenjam@redhat.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 0.0.2-2
- Add foremandist to plugin (dcleal@redhat.com)
- Fix spec filename to match RPM (dcleal@redhat.com)

* Fri Dec 11 2015 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial release
