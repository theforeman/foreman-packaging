%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name net-ldap

Summary: Net::LDAP for Ruby implements client access LDAP protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.17.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/ruby-ldap/ruby-net-ldap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
#BuildRequires: %{?scl_prefix}rubygem(flexmock)
BuildRequires: %{?scl_prefix_ruby}rubygem(test-unit)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# this package obsoletes rubygem-ruby-net-ldap
Provides: %{?scl_prefix}rubygem(ruby-net-ldap) = %{version}-%{release}
Provides: %{?scl_prefix}rubygem-ruby-net-ldap = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
Obsoletes: %{?scl_prefix}rubygem-ruby-net-ldap < 0.0.4-7

%description
Net::LDAP for Ruby (also called net-ldap) implements client access for the
Lightweight Directory Access Protocol (LDAP), an IETF standard protocol for
accessing distributed directory services. Net::LDAP is written completely in
Ruby with no external dependencies. It supports most LDAP client features and
a subset of server features as well.
Net::LDAP has been tested against modern popular LDAP servers including
OpenLDAP and Active Directory. The current release is mostly compliant with
earlier versions of the IETF LDAP RFCs (2251–2256, 2829–2830, 3377, and
3771).
Our roadmap for Net::LDAP 1.0 is to gain full client compliance with
the most recent LDAP RFCs (4510–4519, plus portions of 4520–4532).


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
# Disabled due to no flexmock
#ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
%{?scl:EOF}
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/License.rdoc
%{gem_libdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Contributors.rdoc
%doc %{gem_instdir}/Hacking.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.17.0-2
- Rebuild against rh-ruby27

* Wed Dec 16 2020 Ondřej Ezr <oezr@redhat.com> 0.17.0-1
- Update to 0.17.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.16.1-2
- Bump to release for EL8

* Wed Jun 26 2019 Marek Hulan <mhulan@redhat.com> 0.16.1-1
- Update to 0.16.1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.15.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.15.0-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Jul 29 2016 Dominic Cleal <dominic@cleal.org> 0.15.0-1
- Update net-ldap to 0.15.0 (dominic@cleal.org)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.14.0-1
- Update net-ldap to 0.14.0 (dominic@cleal.org)

* Wed Jan 20 2016 Dominic Cleal <dcleal@redhat.com> 0.13.0-1
- Update net-ldap to 0.13.0 (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.12.0-2
- Fix build errors and modernise specs (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Oct 29 2015 Dominic Cleal <dcleal@redhat.com> 0.12.0-1
- Update net-ldap to 0.12.0 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.11-3
- Converted to tfm SCL (dcleal@redhat.com)

* Wed May 13 2015 Dominic Cleal <dcleal@redhat.com> 0.11-2
- Build net-ldap for Fedora (dcleal@redhat.com)

* Wed May 13 2015 Dominic Cleal <dcleal@redhat.com> 0.11-1
- Update net-ldap to 0.11 (dcleal@redhat.com)

* Wed Dec 10 2014 Dominic Cleal <dcleal@redhat.com> 0.10.0-1
- Update net-ldap to 0.10.0 (dcleal@redhat.com)

* Fri May 30 2014 Dominic Cleal <dcleal@redhat.com> 0.3.1-2
- Modernise spec for EL7 (dcleal@redhat.com)

* Wed May 29 2013 Marek Hulan <mhulan@redhat.com> 0.3.1-1
- Net-ldap gem updated to 0.3.1 (mhulan@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.2-5
- new package built with tito

* Mon Nov 26 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.2-4
- fix requires (msuchy@redhat.com)

* Mon Nov 26 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.2-3
- rebase to net-ldap-0.2.2.gem (msuchy@redhat.com)

* Tue Feb 28 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-3
- Properly obsolete rubygem-ruby-net-ldap (now really).

* Wed Feb 22 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-2
- Properly obsolete rubygem-ruby-net-ldap.

* Mon Feb 06 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-1
- Initial package
