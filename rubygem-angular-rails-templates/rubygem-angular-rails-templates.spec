# Template for Rubygem's spec file
# It should work with f18, f19, rhel6 and rhel6 with SCL

%{?scl:%scl_package rubygems-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name angular-rails-templates

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   0.0.4
Release:   6%{?dist}
Summary:   Use your angular templates with rails' asset pipeline
Group:     Development/Languages
License:   MIT
URL:       https://github.com/pitr/angular-rails-templates
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires:  %{?scl_prefix}ruby(rubygems)
Requires:  %{?scl_prefix}rubygem(railties) >= 3.1
Requires:  %{?scl_prefix}rubygem(sprockets-rails)
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
Adds your HTML templates into Angular's $templateCache using Rails asset pipeline.
It removes the need for AJAX calls to retrieve the templates (or for you to manually set them into the DOM).

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
%{gem_instdir}/app/assets/javascripts/angular-rails-templates.js.erb
%{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}

%files doc
%doc %{gem_instdir}/README.md

%changelog
