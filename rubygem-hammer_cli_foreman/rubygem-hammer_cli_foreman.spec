%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hammer_cli_foreman
%global confdir hammer

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

Summary: Universal command-line interface for Foreman
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.0
Release: 2%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli-foreman
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli) >= 0.3.0
Requires: %{?scl_prefix}rubygem(apipie-bindings) >= 0.0.11
Requires: %{?scl_prefix}rubygem(apipie-bindings) < 0.1.0
Requires: %{?scl_prefix}rubygem(rest-client) < 1.7.0
Requires: %{?scl_prefix}rubygem(rest-client) >= 1.6.5

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%endif
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name} < 0.3.0-2
%endif

%description
Hammer cli provides universal extendable CLI interface for ruby apps

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name}-doc < 0.3.0-2
%endif

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - << \EOF}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 .%{gem_instdir}/config/foreman.yml \
               %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/test

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-2
- Converted to tfm SCL (dcleal@redhat.com)
- Increase range of non-SCL obsoletes to cover 1.9 versions (dcleal@redhat.com)

* Tue Aug 04 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-1
- Update hammer_cli_foreman to 0.3.0 (dcleal@redhat.com)
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Mon Apr 27 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update hammer_cli_foreman to 0.2.0 (dcleal@redhat.com)
- refs #8829 - use config/ template from gem (dcleal@redhat.com)

* Fri Dec 12 2014 Dominic Cleal <dcleal@redhat.com> 0.1.4-1
- Update hammer-cli-foreman to 0.1.4 (martin.bacovsky@gmail.com)

* Thu Aug 21 2014 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- Update rubygem-hammer_cli_foreman to 0.1.3 (martin.bacovsky@gmail.com)

* Thu Aug 14 2014 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Update rubygem-hammer_cli_foreman to 0.1.2 (martin.bacovsky@gmail.com)

* Tue May 20 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.1.1-1
- Rebased hammer_cli_foreman to 0.1.1 (martin.bacovsky@gmail.com)
- Removed credentials from config file (martin.bacovsky@gmail.com)

* Wed Mar 26 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.1.0-1
- Bump to 0.1.0 (martin.bacovsky@gmail.com)
- hammer_cli_foreman - new config location (tstrachota@redhat.com)

* Wed Jan 29 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.18-1
- Bump to 0.0.18 (mbacovsk@redhat.com)

* Thu Jan 23 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.17-1
- Bump to 0.0.17 (mbacovsk@redhat.com)

* Tue Jan 21 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.16-1
- Bump to 0.0.16 (mbacovsk@redhat.com)

* Thu Dec 19 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.15-1
- Bump to 0.0.15 (mbacovsk@redhat.com)

* Wed Dec 18 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.13-1
- Bump to 0.0.13 (mbacovsk@redhat.com)

* Thu Dec 05 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.12-1
- Bump to 0.0.12 (mbacovsk@redhat.com)

* Tue Nov 26 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.11-1
- Bump to 0.0.11 (mbacovsk@redhat.com)

* Fri Nov 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.10-1
- bump to 0.0.10 (mbacovsk@redhat.com)
- updated dependencies

* Mon Nov 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.9-2
- Mark cli_config.yml as a config file (dcleal@redhat.com)
- Update default config for Foreman installation and non-root users
  (dcleal@redhat.com)

* Tue Oct 29 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.9-1
- Update to Hammer CLI Foreman 0.0.9

* Wed Oct 23 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.8-1
- Rebase to 0.0.8 (mbacovsk@redhat.com)

* Thu Oct 10 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.7-1
- Bumped to 0.0.7 (mbacovsk@redhat.com)
- Fixed default config file
- remove deps on awesome_print and terminal-table

* Tue Oct 08 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.6-1
- Update to the latest version of Hammer CLI Foreman

* Thu Sep 26 2013 Sam Kottler <shk@redhat.com> 0.0.5-1
- Bump the version in the spec (shk@redhat.com)
- Update to the latest version (shk@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-2
- Use rubygems-devel on fedora instead of custom macros (shk@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-1
- Remove the 0.0.1 gem bin (shk@redhat.com)
- Bump to version 0.0.3 (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.1-5
- Add configuration to install (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.1-4
- Version bump for rebuild

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.1-3
- Bump version

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com>
- Initial import of the gem (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> - 0.0.1-1
- Initial package
