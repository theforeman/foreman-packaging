%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-xenserver

Summary: Module for the 'fog' gem to support XENSERVER
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.2.3
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog-xenserver
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-core)
Requires: %{?scl_prefix}rubygem(fog-xml)
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
This library can be used as a module for `fog` or as standalone provider to
use the Google in applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/README.md
%{gem_instdir}/spec
%{gem_instdir}/gemfiles
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Feb 29 2016 Dominic Cleal <dominic@cleal.org> 0.2.3-1
- update fog-xenserver to 0.2.3 (kvedulv@kvedulv.de)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.2.2-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 20 2015 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- new package built with tito

