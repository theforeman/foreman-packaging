%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_host_extra_validator

Summary:    Foreman plugin to add extra validations to a host.
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.4
Release:    2%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/FILIADATAGmbH/foreman_host_extra_validator
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.11.0
Requires:   %{?scl_prefix_ruby}ruby(release)
Requires:   %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: foreman-plugin >= 1.11.0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-host_extra_validator

%description
This is a foreman plugin that adds validations to a host.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%{foreman_bundlerd_file}

%posttrans
%{foreman_restart}
exit 0

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_instdir}/locale
%{gem_spec}
%exclude %{gem_cache}
%doc %{gem_instdir}/LICENSE
%{foreman_bundlerd_plugin}

%exclude %{gem_instdir}/test

%files doc
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md
%{gem_docdir}

%changelog
* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.4-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jul 20 2016 Timo Goebel <mail@timogoebel.name> 0.0.4-1
- initial packaging
