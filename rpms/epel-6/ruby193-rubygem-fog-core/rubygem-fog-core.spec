%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-core

Summary: Shared classes and tests for fog providers and services
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.21.1
Release: 1%{dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog-core
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem-builder
Requires: %{?scl_prefix}rubygem-excon >= 0.32.0
Requires: %{?scl_prefix}rubygem-excon < 0.33.0
Requires: %{?scl_prefix}rubygem-formatador => 0.2.0
Requires: %{?scl_prefix}rubygem-formatador < 0.3
Requires: %{?scl_prefix}rubygem-mime-types
Requires: %{?scl_prefix}rubygem-net-scp => 1.1.0
Requires: %{?scl_prefix}rubygem-net-scp < 2
Requires: %{?scl_prefix}rubygem-net-ssh >= 2.1.3
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(fog) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
Shared classes and tests for fog providers and services.

The Ruby cloud services library. Supports all major cloud providers including
AWS, Rackspace, Linode, Blue Box, StormOnDemand, and many others. Full support
for most AWS services including EC2, S3, CloudWatch, SimpleDB, ELB, and RDS.

# Disabled until https://github.com/fog/fog-core/pull/26 is fixed and there is
# documentation available to package.
#%package doc
#BuildArch:  noarch
#Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
#Summary:    Documentation for rubygem-%{gem_name}
#
#%description doc
#This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0} --no-rdoc --no-ri 
%{?scl:"}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
#%{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/.*

#%files doc
#%{gem_instdir}/LICENSE.md
#%{gem_instdir}/README.md
#%{gem_instdir}/tests
#%{gem_instdir}/Gemfile*
#%{gem_instdir}/Rakefile
#%exclude %{gem_instdir}/fog-core.gemspec

%changelog
* Wed Mar 19 2014 Dominic Cleal <dcleal@redhat.com> 1.21.1-1
- new package built with tito

