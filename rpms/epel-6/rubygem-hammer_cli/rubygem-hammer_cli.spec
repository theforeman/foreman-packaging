%global gemname hammer_cli

%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Universal command-line interface for Foreman
Name: rubygem-%{gemname}
Version: 0.0.1
Release: 7%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli
Source0: %{gemname}-%{version}.gem

%if 0%{?rhel} == 6 || 0%{?fedora} < 19
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
Requires: rubygem(clamp)
Requires: rubygem(terminal-table)
Requires: rubygem(rest-client)
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

%files
%dir %{geminstdir}
%{_bindir}/hammer
%{geminstdir}/bin
%{geminstdir}/lib
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}


%changelog
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
