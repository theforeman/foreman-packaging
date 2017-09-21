%global gem_name puppet-strings

Summary: Puppet documentation via YARD
Name: rubygem-%{gem_name}
Version: 0.99.0
Release: 1%{?dist}
Group: System Environment/Base
License: ASL-2.0
URL: https://github.com/puppetlabs/puppets-strings
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
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
# Patch for compatibility with yard pre-0.9.2
sed -i '/--no-progress/d' .%{gem_libdir}/puppet-strings.rb

# Compatible with yard 0.8.x too now
sed -i '/yard/ s/0\.9\.5/0.8/' .%{gem_spec}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/*.md
%{gem_instdir}/spec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%changelog
* Mon Oct 31 2016 Dominic Cleal <dominic@cleal.org> 0.99.0-1
- Update puppet-strings to 0.99.0 (dominic@cleal.org)

* Fri May 27 2016 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- new package built with tito

