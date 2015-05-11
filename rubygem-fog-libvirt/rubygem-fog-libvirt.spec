%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-libvirt

Summary: Module for the 'fog' gem to support libvirt
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.0.1
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog-libvirt
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.27.4
Requires: %{?scl_prefix}rubygem(fog-core) < 2
Requires: %{?scl_prefix}rubygem(fog-json)
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 0.2
# On Fedora use ruby-libvirt and not the gem as it's newer
%if 0%{?fedora}
Requires: %{?scl_prefix}ruby-libvirt >= 0.5
Requires: %{?scl_prefix}ruby-libvirt < 0.6
%else
Requires: %{?scl_prefix}rubygem(ruby-libvirt) >= 0.5
Requires: %{?scl_prefix}rubygem(ruby-libvirt) < 0.6
%endif
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

# Remove gem dep so its presence isn't checked at load time, use ruby-libvirt instead
%if 0%{?fedora}
sed -i '/add_.*dependency.*ruby-libvirt/d' %{buildroot}%{gem_spec}
%endif

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/.*

%files doc
%{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/README.md
%{gem_instdir}/tests
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
