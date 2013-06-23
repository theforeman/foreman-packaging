%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from ruby-hmac-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-hmac

Summary: This module provides common interface to HMAC functionality
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 8%{?dist}
Group: Development/Languages
License: MIT and Ruby
URL: http://ruby-hmac.rubyforge.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(ruby-hmac) = %{version}
Provides:  %{?scl_prefix}rubygem(hmac) = %{version}-%{release}
Obsoletes: %{?scl_prefix}rubygem(hmac) < 0.4.0-6

%description
This module provides common interface to HMAC functionality. HMAC is a kind of
"Message Authentication Code" (MAC) algorithm whose standard is documented in
RFC2104. Namely, a MAC provides a way to check the integrity of information
transmitted over or stored in an unreliable medium, based on a secret key.
Originally written by Daiki Ueno. Converted to a RubyGem by Geoffrey
Grosenbach


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} --force --rdoc --ri %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd %{buildroot}/%{gem_instdir}
%{?scl:scl enable %{scl} "}
ruby test/test_hmac.rb
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_libdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%doc %{gem_instdir}/test
%doc %{gem_docdir}
%{gem_cache}
%{gem_spec}

%changelog
* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.0-8
- new package built with tito

* Tue Aug 07 2012 Mo Morsi <mmorsi@redhat.com> - 0.4.0-7
- small fixes for fedora compliance:
- renamed spec
- added obsoletes

* Thu Aug 02 2012 Mo Morsi <mmorsi@redhat.com> - 0.4.0-6
- renamed rubygem-hmac to rubygem-ruby-hmac

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.0-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Chris Lalancette <clalance@redhat.com> - 0.4.0-2
- Updates from review

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.4.0-1
- Initial package
