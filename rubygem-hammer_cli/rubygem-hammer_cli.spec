%global gem_name hammer_cli
%global confdir hammer

Summary: Universal command-line interface for Foreman
Name: rubygem-%{gem_name}
Version: 0.1.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: cli_config.yml

%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif

# on ruby 1.8.x
Requires: ruby(rubygems)
Requires: rubygem(clamp)
Requires: rubygem(rb-readline)
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(logging)
Requires: rubygem(awesome_print)
Requires: rubygem(table_print) >= 1.5.0
Requires: rubygem(highline)
Requires: rubygem(fast_gettext)
Requires: rubygem(locale) <= 2.0.9
Requires: rubygem(json)
Requires: rubygem(fastercsv)
Requires: rubygem(mime-types) < 2.0.0
Requires: rubygem(apipie-bindings) >= 0.0.10
Requires: rubygem(apipie-bindings) < 0.1.0
BuildRequires: rubygems-devel
%if 0%{?rhel} == 6
BuildRequires: ruby(abi)
%else
BuildRequires: ruby(release)
%endif
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Hammer cli provides universal extendable CLI interface for ruby apps


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{_bindir}
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}%{gem_instdir}/hammer_cli_complete %{buildroot}%{_sysconfdir}/bash_completion.d/%{gem_name}

mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{confdir}/cli_config.yml
rm -r %{buildroot}%{gem_instdir}/config


%files
%dir %{gem_instdir}
%{_bindir}/hammer
%{_sysconfdir}/bash_completion.d/%{gem_name}
%{_sysconfdir}/%{confdir}/cli.modules.d
%{_sysconfdir}/%{confdir}/cli_config.yml
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/locale
%{gem_instdir}/LICENSE
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_instdir}/test
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/README.md

%changelog
* Thu Aug 21 2014 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- Update rubygem-hammer_cli to 0.1.3 (martin.bacovsky@gmail.com)

* Thu Aug 14 2014 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Update rubygem-hammer_cli to 0.1.2 (martin.bacovsky@gmail.com)

* Tue May 20 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.1.1-1
- Rebased hammer_cli to 0.1.1 (martin.bacovsky@gmail.com)

* Wed Mar 26 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.1.0-1
- Bump to 0.1.0 (martin.bacovsky@gmail.com)
- hammer_cli - new config location and dependencies (tstrachota@redhat.com)

* Wed Jan 29 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.18-1
- Bump to 0.0.18 (mbacovsk@redhat.com)

* Thu Jan 23 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.16-1
- Bump to 0.0.16 (mbacovsk@redhat.com)

* Tue Jan 21 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.15-1
- Bump to 0.0.15 (mbacovsk@redhat.com)

* Tue Jan 07 2014 Dominic Cleal <dcleal@redhat.com> 0.0.14-2
- Require fastercsv and mime-types on Fedora to avoid gemspec conflict
  (dcleal@redhat.com)

* Thu Dec 19 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.14-1
- Bump to 0.0.14 (mbacovsk@redhat.com)

* Wed Dec 18 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.13-1
- Bump to 0.0.13 (mbacovsk@redhat.com)

* Thu Dec 05 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.12-1
- Bump to 0.0.12 (mbacovsk@redhat.com)

* Tue Nov 26 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.11-1
- Bump to 0.0.11 (mbacovsk@redhat.com)

* Fri Nov 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.9-1
- Bumped to 0.0.9 (mbacovsk@redhat.com)

* Tue Oct 29 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.8-1
- Update to Hammer CLI Foreman 0.0.8

* Wed Oct 09 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.7-1
- Bumped to 0.0.7 (mbacovsk@redhat.com)
- fixed error handling while loading hammer modules

* Tue Oct 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.6-2
- Added depenedency on fastercsv on ruby 1.8 (mbacovsk@redhat.com)

* Tue Oct 08 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.6-1
- fixes #3184 - update hammer dependencies

* Thu Sep 26 2013 Sam Kottler <shk@redhat.com> 0.0.5-1
- Cherry pick hammer_cli version bump (shk@redhat.com)

* Tue Aug 27 2013 Dominic Cleal <dcleal@redhat.com> 0.0.3-4
- Install bash completion extension (dcleal@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-3
- Fix typo in macro (shk@redhat.com)
- Use macros provided by rubygems-devel on Fedora (shk@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-2
- Add configuration example to packaged files (shk@redhat.com)
- Fix readme path (shk@redhat.com)
- Add docs and other files that are new in the 0.0.3 release (shk@redhat.com)
- Add docs and other files that are new in the 0.0.3 release (shk@redhat.com)
- Bump hammer_cli version to 0.0.3 (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.2-15
- Remove SCL conditional (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.2-14
- Add multi_json dependency to hammer and fix gem_dir (shk@redhat.com)
- Fix changelog (shk@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 0.0.2-13
- Add logging requirement (shk@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 0.0.2-10
- Rebuilding on RHEL

* Mon Aug 12 2013 Sam Kottler <shk@redhat.com> 0.0.2-9
- Bump version

* Mon Aug 12 2013 Sam Kottler <shk@redhat.com> 0.0.2-8
- Bump hammer version (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.0.1-7
- Add a missing %% (shk@redhat.com)
- Remove ruby(abi) for f19 (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.0.1-6
- Fix bindir (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.0.1-5
- Don't require ruby-abi on F19+ (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.0.1-4
- Rebuild

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.0.1-3
- Removed abi version for hammer_cli deps (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.0.1-2
- Initial package with tito
* Wed Jul 31 2013  <shk@redhat.com> - 0.0.1-1
- Initial package
