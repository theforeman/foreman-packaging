%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name librarian-puppet

# we are using this gem also as non-SCL in RHEL6
%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%define gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%define gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%define gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%endif

Summary: Bundler for your Puppet modules
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.10
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/rodjek/librarian-puppet
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: git
Requires: %{?scl_prefix}puppet
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi)
Requires: %{?scl_prefix}rubygem-thor >= 0.15
Requires: %{?scl_prefix}rubygem-thor < 1
BuildRequires: %{?scl_prefix}rubygems
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%endif

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Simplify deployment of your Puppet infrastructure by automatically pulling in
modules from the forge and git repositories with a single command.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}

%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%{_bindir}/librarian-puppet
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Fri Jan 17 2014 Dominic Cleal <dcleal@redhat.com> 0.9.10-3
- Correct rubygem-thor dependency (dcleal@redhat.com)

* Fri Jan 17 2014 Dominic Cleal <dcleal@redhat.com> 0.9.10-2
- Add git dependency (dcleal@redhat.com)

* Fri Jan 17 2014 Dominic Cleal <dcleal@redhat.com> 0.9.10-1
- new package built with tito

