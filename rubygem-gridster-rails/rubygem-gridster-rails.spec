%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkgname %{name}}

%define gem_name gridster-rails
%global rubyabi 1.9.1

Summary: This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3 application
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.5
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/vanetten/gridster-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(railties) >= 3.1.0
Requires: %{?scl_prefix}rubygem(railties) < 4.0.0
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Gridster is a jQuery plugin that makes building intuitive draggable layouts
from elements spanning multiple columns. You can even dynamically add and
remove elements from the grid.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/vendor
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Thu Jul 17 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.5-3
- Fixed dependency in the -doc subpackage

* Wed May 21 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-2
- Remove RHEL 7 from ruby(release) conditional (dcleal@redhat.com)

* Tue May 20 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- new package built with tito

