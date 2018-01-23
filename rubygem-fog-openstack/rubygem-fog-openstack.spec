%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-openstack

Summary: Module for the 'fog' gem to support OpenStack clouds
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.1.23
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/fog/fog-openstack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.40
Requires: %{?scl_prefix}rubygem(fog-core) < 2.0
Requires: %{?scl_prefix}rubygem(fog-json) >= 1.0
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
This is the plugin Gem to talk to OpenStack clouds via fog.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.md

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/supported.md
%doc %{gem_instdir}/docs
%doc %{gem_instdir}/examples
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Tue Jan 23 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.23-1
- Update fog-openstack to 0.1.23 (me@daniellobato.me)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.18-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Jan 04 2017 Dominic Cleal <dominic@cleal.org> 0.1.18-1
- Update fog-openstack to 0.1.18 (dominic@cleal.org)

* Mon Sep 05 2016 Dominic Cleal <dominic@cleal.org> 0.1.12-1
- Update fog-openstack to 0.1.12 (dominic@cleal.org)

* Wed Aug 10 2016 Dominic Cleal <dominic@cleal.org> 0.1.11-1
- Update fog-openstack to 0.1.11 (dominic@cleal.org)

* Thu Aug 04 2016 Dominic Cleal <dominic@cleal.org> 0.1.10-1
- Update fog-openstack to 0.1.10 (dominic@cleal.org)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 0.1.8-1
- Update fog-openstack to 0.1.8 (dominic@cleal.org)

* Thu Mar 31 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- new package built with tito

