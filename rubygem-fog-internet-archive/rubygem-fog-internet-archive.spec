%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-internet-archive

Summary: Module for the 'fog' gem to support Internet Archive.
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.0.1
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog-internet-archive
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.45.0
Requires: %{?scl_prefix}rubygem(fog-core) < 2.0.0
Requires: %{?scl_prefix}rubygem(fog-json)
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 0.2.0
Requires: %{?scl_prefix_ruby}ruby(release)

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(fog-core) >= 1.45.0
BuildRequires: %{?scl_prefix}rubygem(fog-core) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(fog-json)
BuildRequires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
BuildRequires: %{?scl_prefix}rubygem(fog-xml) < 0.2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(fog-internet-archive) = %{version}

%description
Module for the 'fog' gem to support Internet Archive.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%{gem_instdir}/Rakefile

%changelog
