%global gem_name puppet-strings

Summary: Puppet documentation via YARD
Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Group: System Environment/Base
License: ASL-2.0
URL: https://github.com/puppetlabs/puppetlabs-strings
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: puppet >= 3.7.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch

%description
A Puppet Face and plugin built on the YARD Documentation Tool and the
Puppet 4 Parser.

It is uses YARD and the Puppet Parser to generate HTML documentation
about Puppet code and Puppet extensions written in Ruby.

%package doc
Summary:    Documentation for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description doc
This package contains documentation for %{name}.

%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build
# Puppet's shipped as a regular Ruby library, not a gem
sed -i '/dependency.*puppet/d' .%{gem_spec}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Fri May 27 2016 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- new package built with tito

