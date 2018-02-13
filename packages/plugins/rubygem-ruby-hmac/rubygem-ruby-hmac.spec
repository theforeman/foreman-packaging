# Generated from ruby-hmac-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-hmac

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: This module provides common interface to HMAC functionality
Group: Development/Languages
License: MIT
URL: http://ruby-hmac.rubyforge.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif
Requires: ruby
Requires: ruby(rubygems)
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
This module provides common interface to HMAC functionality. HMAC is a kind of
"Message Authentication Code" (MAC) algorithm whose standard is documented in
RFC2104. Namely, a MAC provides a way to check the integrity of information
transmitted over or stored in an unreliable medium, based on a secret key.
Originally written by Daiki Ueno. Converted to a RubyGem by Geoffrey
Grosenbach.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.txt
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Wed Jun 15 2016 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- new package built with tito

