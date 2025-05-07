# template: default
%global gem_name ldap_fluff

Name: rubygem-%{gem_name}
Version: 0.9.0
Release: 1%{?dist}
Summary: LDAP querying tools for Active Directory, FreeIPA and POSIX-style
License: GPL-2.0-only
URL: https://github.com/theforeman/ldap_fluff
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Simple library for binding & group querying on top of various LDAP
implementations.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/test

%changelog
* Wed May 07 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.9.0-1
- Update to 0.9.0

* Sun Oct 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.8.0-1
- Update to 0.8.0

* Sun May 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.7.0-1
- Update to 0.7.0

* Fri Jun 25 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.6.0-1
- Update to 0.6.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.0-2
- Rebuild against rh-ruby27

* Wed Dec 16 2020 Lukas Zapletal <lzap+rpm@redhat.com> 0.5.0-1
- Update to 0.5.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.7-5
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.7-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.7-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.7-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 0.4.7-1
- Update ldap_fluff to 0.4.7 (mhulan@redhat.com)

* Wed Feb 22 2017 Dominic Cleal <dominic@cleal.org> 0.4.6-1
- Update ldap-fluff to 0.4.6 (me@daniellobato.me)

* Wed Jan 11 2017 Dominic Cleal <dominic@cleal.org> 0.4.5-1
- Update ldap_fluff to 0.4.5 (me@daniellobato.me)

* Fri Sep 30 2016 Dominic Cleal <dominic@cleal.org> 0.4.4-1
- Update ldap_fluff to 0.4.4 (mhulan@redhat.com)

* Mon Jun 20 2016 Dominic Cleal <dominic@cleal.org> 0.4.3-1
- Update ldap_fluff to 0.4.3 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.4.2-1
- Update ldap_fluff to 0.4.2 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.4.1-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Mar 03 2016 Dominic Cleal <dominic@cleal.org> 0.4.1-1
- Update ldap_fluff to 0.4.1 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 20 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-1
- Update ldap_fluff to 0.4.0 (dcleal@redhat.com)

* Wed Sep 09 2015 Dominic Cleal <dcleal@redhat.com> 0.3.7-1
- Update ldap_fluff to 0.3.7 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.3.6-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Jul 27 2015 Dominic Cleal <dcleal@redhat.com> 0.3.6-1
- Update ldap_fluff to 0.3.6 (dcleal@redhat.com)

* Wed May 13 2015 Dominic Cleal <dcleal@redhat.com> 0.3.5-1
- Update ldap_fluff to 0.3.5 (dcleal@redhat.com)

* Sun Mar 22 2015 Marek Hulan <mhulan@redhat.com> 0.3.4-1
- Update ldap_fluff to 0.3.4 (mhulan@redhat.com)

* Mon Nov 10 2014 Dominic Cleal <dcleal@redhat.com> 0.3.3-1
- update ldap_fluff to 0.3.3 (dcleal@redhat.com)

* Wed Oct 15 2014 Dominic Cleal <dcleal@redhat.com> 0.3.2-1
- update ldap_fluff to 0.3.2 (dcleal@redhat.com)

* Wed Aug 27 2014 Dominic Cleal <dcleal@redhat.com> 0.3.1-1
- update ldap_fluff to 0.3.1 (dcleal@redhat.com)

* Fri Aug 01 2014 Dominic Cleal <dcleal@redhat.com> 0.3.0-1
- update ldap_fluff to 0.3.0 (dcleal@redhat.com)

* Thu May 29 2014 Petr Chalupa <pchalupa@redhat.com> 0.2.5-1
- update ldap_fluff to 0.2.5 (pchalupa@redhat.com)

* Tue May 27 2014 Petr Chalupa <pchalupa@redhat.com> 0.2.4-1
- update ldap_fluff to 0.2.4 (pchalupa@redhat.com)

* Mon May 19 2014 Petr Chalupa <pchalupa@redhat.com> 0.2.3-1
- update ldap_fluff to 0.2.3 (pchalupa@redhat.com)

* Tue Aug 27 2013 Partha Aji <paji@redhat.com> 0.2.2-2
- Updated to use ruby release for f19 (paji@redhat.com)

* Thu May 30 2013 Marek Hulan <mhulan@redhat.com> 0.2.2-1
- Gem ldap_fluff upgraded to 0.2.2 (mhulan@redhat.com)

* Thu May 30 2013 Marek Hulan <mhulan@redhat.com> 0.2.1-2
- ldap_fluff does not create /etc/ldap_fluff.yml anymore (mhulan@redhat.com)

* Thu May 30 2013 Marek Hulan <mhulan@redhat.com> 0.2.1-1
- Ldap_fluff update to 0.2.1 (mhulan@redhat.com)

* Thu May 16 2013 Brad Buckingham <bbuckingham@redhat.com> 0.1.7-2
- ldap_fluff - bumping version (bbuckingham@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-3
- correct build directory in SC env

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-2
- new package built with tito

* Thu Nov 01 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.3-1
- update to ldap_fluff-0.1.3.gem and polish the spec (msuchy@redhat.com)

* Mon Jul 16 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.1-2
- cleanup spec file (msuchy@redhat.com)

* Tue Jul 10 2012 Jordan OMara <jomara@redhat.com> 0.1.1-1
- new package built with tito

* Fri Jul 06 2012 Jordan OMara <jomara@redhat.com> 0.1.1-1
- A few minor IPA bugs (jomara@redhat.com)
- Adding .rvmrc; unit tests only support 1.9.3 (jomara@redhat.com)

* Fri Jul 06 2012 Jordan OMara <jomara@redhat.com> 0.1.0-1
- Adding the rest of free ipa support - testing, configuration
  (jomara@redhat.com)
- Adding FreeIPA support (jomara@redhat.com)
- Fix for empty set return for missing ldap user (jomara@redhat.com)
- Removing files that shouldnt have been committed (jomara@redhat.com)

* Fri Jun 29 2012 Jordan OMara <jomara@redhat.com> 0.0.6-1
- Adding some heavy recursive tests (jomara@redhat.com)
- Updating README to fix formatting (jsomara@gmail.com)
- Adding anon_queries to AD config; Fixing AD recursive group walk
  (jomara@redhat.com)
- Fixing a posix merge_filter bug. NEEDS SOME TESTS (jomara@redhat.com)
- Fixing a few minor bugs (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.5-1
- Forgot to remove obsolete files from lib (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.4-1
- rdoc/task -> rake/rdoctask for older rpm support (jomara@redhat.com)
- Updating readme (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.3-1
- Automatic commit of package [rubygem-ldap_fluff] release [0.0.2-1].
  (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.2-1
- new package built with tito
