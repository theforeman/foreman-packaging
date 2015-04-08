%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-json

Summary: JSON parsing for fog providers
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.0.1
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog-json
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(multi_json) => 1.0
Requires: %{?scl_prefix}rubygem(multi_json) < 2
Requires: %{?scl_prefix}rubygem(fog-core) >= 1
Requires: %{?scl_prefix}rubygem(fog-core) < 2
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
Extraction of the JSON parsing tools shared between a number of providers in
the 'fog' gem.

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
%{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/.*

%files doc
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/README.md
%{gem_instdir}/test
%{gem_instdir}/Gemfile*
%{gem_instdir}/gemfiles
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/fog-json.gemspec

%changelog
* Tue Mar 25 2014 Dominic Cleal <dcleal@redhat.com> 1.0.0-2
- Fix Provides for correct gem name (dcleal@redhat.com)

* Wed Mar 19 2014 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- new package built with tito

