%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name jwt
%global rubyabi 1.9.1

Summary: JSON Web Token implementation in Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/progrium/ruby-jwt
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby

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
A Ruby implementation of JSON Web Token draft 06.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
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
%exclude %{gem_cache}
%{gem_spec}

%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_instdir}/Manifest
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_docdir}

%changelog
* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.1.8-1
- new package built with tito

