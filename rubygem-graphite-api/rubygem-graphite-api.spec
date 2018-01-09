%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name graphite-api

Summary: Graphite API - A Simple ruby client, aggregator daemon and API tools
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.5
Release: 5%{?dist}
Group: Development/Languages
License: LGPLv3
URL: https://github.com/kontera-technologies/graphite-api
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(eventmachine) >= 0.3.3
Requires: %{?scl_prefix}rubygem(zscheduler) >= 0.0.3

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

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
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

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
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.1.5-4
- Use gem_install macro (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- new package built with tito
