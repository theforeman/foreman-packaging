%global gem_name satyr

Name: rubygem-%{gem_name}
Version: 0.1
Release: 1%{?dist}
Summary: Parse uReport bug report format
Group: Development/Languages
License: GPLv2
URL: http://github.com/abrt/satyr
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: rubygem(ffi)
Requires: satyr

%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
BuildRequires: rubygems-devel

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby bindings for satyr, library for working with the uReport problem report
format.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}

%changelog
* Mon Aug 18 2014 Martin Milata <mmilata@redhat.com> - 0.1-1
- Initial package
