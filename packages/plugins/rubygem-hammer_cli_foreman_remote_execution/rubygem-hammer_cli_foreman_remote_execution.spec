# template: hammer_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hammer_cli_foreman_remote_execution
%global plugin_name foreman_remote_execution

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}
%global hammer_confdir %{_root_sysconfdir}/hammer

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.0
Release: 1%{?foremandist}%{?dist}
Summary: CLI for the Foreman remote execution plugin
Group: Development/Languages
License: GPLv3+
URL: https://github.com/theforeman/hammer_cli_foreman_remote_execution
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
CLI for the Foreman remote execution plugin.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{hammer_confdir}/cli.modules.d
install -m 0644 .%{gem_instdir}/config/%{plugin_name}.yml \
                %{buildroot}%{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.tx
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%config %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/config
%{gem_instdir}/hammer_cli_foreman_remote_execution.gemspec
%{gem_instdir}/test

%changelog
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
