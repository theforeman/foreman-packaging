%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rack-openid
%global rubyabi 1.9.1

Summary: Provides a more HTTPish API around the ruby-openid library.
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.1
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/josh/rack-openid
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}rubygem(rack) >= 1.1.0
Requires: %{?scl_prefix}rubygem(ruby-openid) >= 2.1.8
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildArch: noarch
BuildRequires:  %{?scl_prefix}ruby(rubygems)
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Provides a more HTTPish API around the ruby-openid library.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.


%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}


