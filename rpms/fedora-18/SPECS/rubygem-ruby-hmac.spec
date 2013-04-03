# Generated from ruby-hmac-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-hmac
%global rubyabi 1.9.1

Summary: This module provides common interface to HMAC functionality
Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://ruby-hmac.rubyforge.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This module provides common interface to HMAC functionality. HMAC is a kind of
"Message Authentication Code" (MAC) algorithm whose standard is documented in
RFC2104. Namely, a MAC provides a way to check the integrity of information
transmitted over or stored in an unreliable medium, based on a secret key.
Originally written by Daiki Ueno. Converted to a RubyGem by Geoffrey
Grosenbach


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
gem install --local --install-dir .%{gem_dir} \
	    --force %{SOURCE0}

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
/usr/share/gems/gems/ruby-hmac-0.4.0/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt

%changelog
* Thu Jun 14 2012 jason - 0.4.0-1
- Initial package
