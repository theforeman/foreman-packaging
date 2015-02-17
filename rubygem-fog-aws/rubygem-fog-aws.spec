%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-aws

Summary: Module for the 'fog' gem to support Amazon Web Services
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.0.6
Release: 1%{dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog-aws
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.27
Requires: %{?scl_prefix}rubygem(fog-core) < 2
Requires: %{?scl_prefix}rubygem(fog-json) >= 1
Requires: %{?scl_prefix}rubygem(fog-json) < 2
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 1
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8
Requires: %{?scl_prefix}rubygem(ipaddress) < 1
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
This library can be used as a module for `fog` or as standalone provider to
use the Amazon Web Services in applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

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
%{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/.*

%files doc
%{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/README.md
%{gem_instdir}/tests
%{gem_instdir}/gemfiles
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
