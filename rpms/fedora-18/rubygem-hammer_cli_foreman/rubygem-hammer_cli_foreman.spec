%global gemname hammer_cli_foreman

%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Universal command-line interface for Foreman
Name: rubygem-%{gemname}
Version: 0.0.9
Release: 2%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli-foreman
Source0: %{gemname}-%{version}.gem
Source1: cli_config.yml

%if 0%{?rhel} == 6 || 0%{?fedora} < 19
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
Requires: rubygem(hammer_cli)
Requires: rubygem(foreman_api) >= 0.1.7
Requires: rubygem(clamp)
BuildRequires: ruby(rubygems)
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
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
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{_sysconfdir}/foreman
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/foreman/cli_config.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/lib
%{_sysconfdir}/foreman
%config(noreplace) %{_sysconfdir}/foreman/cli_config.yml
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}


%changelog
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
