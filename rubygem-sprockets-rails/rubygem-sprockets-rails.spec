# Template for Rubygem's spec file
# It should work with f18, f19, rhel6 and rhel6 with SCL

%{?scl:%scl_package rubygems-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sprockets-rails

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   2.0.1
Release:   5%{?dist}  
Summary:   Sprockets Rails integration
License:   MIT
Group:     Development/Languages
URL:       https://github.com/rails/sprockets-rails
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires:  %{?scl_prefix}ruby(rubygems)
Requires:  %{?scl_prefix}rubygem(sprockets) >= 2.8
Requires:  %{?scl_prefix}rubygem(sprockets) < 3
Requires:  %{?scl_prefix}rubygem(actionpack) >= 3
Requires:  %{?scl_prefix}rubygem(activesupport) >= 3
%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires:      %{?scl_prefix}ruby(abi)
%else
Requires:      %{?scl_prefix}ruby(release)
%endif

BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems-devel
%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
BuildRequires: %{?scl_prefix}ruby(abi)
%else
BuildRequires: %{?scl_prefix}ruby(release)
%endif

%description
Provides Sprockets implementation for Rails

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for %{name}

%description doc
This package contains documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files 
%dir %{gem_instdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_instdir}/README.md

%changelog
