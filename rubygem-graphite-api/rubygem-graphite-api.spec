%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name graphite-api
%global rubyabi 1.9.1

Summary: Graphite API - A Simple ruby client, aggregator daemon and API tools
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.5
Release: 1%{?dist}
Group: Development/Languages
License: LGPLv3
URL: https://github.com/kontera-technologies/graphite-api
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(eventmachine) >= 0.3.3
Requires: %{?scl_prefix}rubygem(zscheduler) >= 0.0.3

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Ruby API toolkit for Graphite.

GraphiteAPI provides two ways for interacting with Graphite's Carbon Daemon,
the first is for Ruby applications using the GraphiteAPI::Client, the second
is through GraphiteAPI-Middleware daemon, both methods implements Graphite's
plaintext protocol.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/


%files
%{_bindir}/graphite-middleware
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- new package built with tito

