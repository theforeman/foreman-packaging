%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rails-i18n

Summary: Common locale data and translations for Rails i18n
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 3.0.1
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/svenfuchs/rails-i18n
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(i18n) >= 0.5
Requires: %{?scl_prefix}rubygem(i18n) < 1
Requires: %{?scl_prefix}rubygem(rails) >= 3.0.0
Requires: %{?scl_prefix}rubygem(rails) < 4.0.0
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A set of common locale data and translations to internationalize and/or
localize your Rails applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/rails
%doc %{gem_instdir}/MIT-LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 29 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-1
- new package built with tito

