# Generated from rb-inotify-0.9.7.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rb-inotify

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.7
Release: 3%{?dist}
Summary: A Ruby wrapper for Linux's inotify, using FFI
Group: Development/Languages
License: MIT
URL: https://github.com/nex3/rb-inotify
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(ffi) >= 0.5.0

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Ruby wrapper for Linux's inotify, using FFI.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

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

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rb-inotify.gemspec

%changelog
* Fri Sep 06 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.9.7-3
- Updates to build for SCL and drop EL6 compatability

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.9.7-2
- Add missing EL6 build information (ericdhelms@gmail.com)

* Fri Jul 29 2016 Dominic Cleal <dominic@cleal.org> 0.9.7-1
- new package built with tito

