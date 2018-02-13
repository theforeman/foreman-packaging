%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name kafo_wizards

Summary: Define and render wizard-like user interfaces
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.1
Release: 2%{?dist}
Group: Development/Libraries
License: GPLv3+
URL: https://github.com/theforeman/kafo_wizards
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?scl:1} || (0%{?el6} && 0%{!?scl:1})
Requires:      %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires:      %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(highline)

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem provides tools to define and execute wizard-like user interface
for your application. Rendering of the wizards uses highline library.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for %{name}
Group:      Documentation

%description doc
This package contains documentation for %{name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE.txt


%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE.txt

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-2
- Use gem_install macro (dominic@cleal.org)

* Tue Jan 26 2016 Dominic Cleal <dcleal@redhat.com> 0.0.1-1
- new package built with tito

