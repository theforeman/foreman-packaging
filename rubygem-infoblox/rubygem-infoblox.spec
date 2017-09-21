# Generated from infoblox-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name infoblox

Name: rubygem-%{gem_name}
Version: 2.0.4
Release: 1%{?dist}
Summary: A Ruby wrapper to the Infoblox WAPI
Group: Development/Languages
License: MIT
URL: https://github.com/govdelivery/infoblox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(faraday)
Requires: rubygem(faraday_middleware)
%if 0%{?rhel} == 6
BuildRequires: ruby(abi)
%else
BuildRequires: ruby(release)
%endif
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This gem is a Ruby interface to the Infoblox WAPI. Using the gem, you can query,
create, update, and delete DNS records in your Infoblox instance.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/RELEASES.md
%{gem_instdir}/Rakefile
%{gem_instdir}/infoblox.gemspec
%{gem_instdir}/spec

%changelog
* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 2.0.4-1
- Update infoblox to 2.0.4 (ericdhelms@gmail.com)

* Tue Sep 06 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- new package built with tito

