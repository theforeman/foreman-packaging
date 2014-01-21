%global gemname hammer_cli

%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Universal command-line interface for Foreman
Name: rubygem-%{gemname}
Version: 0.0.15
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli
Source0: %{gemname}-%{version}.gem

%if 0%{?rhel} == 6 || 0%{?fedora} < 19
Requires: ruby(abi)
%endif

# on ruby 1.8.x
Requires: ruby(rubygems)
Requires: rubygem(clamp)
Requires: rubygem(rest-client)
Requires: rubygem(logging)
Requires: rubygem(awesome_print)
Requires: rubygem(table_print)
Requires: rubygem(highline)
Requires: rubygem(fastercsv)
Requires: rubygem(mime-types)
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
%if 0%{?rhel} == 6 || 0%{?fedora} < 19
BuildRequires: ruby(abi)
%endif
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

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

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}%{geminstdir}/hammer_cli_complete %{buildroot}%{_sysconfdir}/bash_completion.d/%{gemname}
sed -i 's/^_HAMMER_BUNDLER_CMD=.*/_HAMMER_BUNDLER_CMD=""/' %{buildroot}%{_sysconfdir}/bash_completion.d/%{gemname}

%files
%dir %{geminstdir}
%{_bindir}/hammer
%{_sysconfdir}/bash_completion.d/%{gemname}
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/config/cli_config.template.yml
%{geminstdir}/LICENSE
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{geminstdir}/test
%doc %{gem_dir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/doc/developer_docs.md
%doc %{geminstdir}/doc/creating_apipie_commands.md
%doc %{geminstdir}/doc/creating_commands.md
%doc %{geminstdir}/doc/development_tips.md
%doc %{geminstdir}/doc/writing_a_plugin.md
%doc %{geminstdir}/doc/option_normalizers.md
%doc %{geminstdir}/doc/design.png
%doc %{geminstdir}/doc/design.uml
%doc %{geminstdir}/README.md

%changelog
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
