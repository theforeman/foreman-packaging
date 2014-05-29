%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name net-ldap
%if 0%{?rhel} == 6 || 0%{?fedora} < 17
%global gem_libdir %{gem_instdir}/lib
%endif

Summary: Net::LDAP for Ruby implements client access LDAP protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://net-ldap.rubyforge.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems-devel
# specs need metaid gem that is not in Fedora yet
#BuildRequires: %{?scl_prefix}rubygem(rspec-core)
#BuildRequires: %{?scl_prefix}rubygem(flexmock)
BuildRequires: %{?scl_prefix}rubygem(minitest)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# this package obsoletes rubygem-ruby-net-ldap
Provides: %{?scl_prefix}rubygem(ruby-net-ldap) = %{version}-%{release}
Provides: %{?scl_prefix}rubygem-ruby-net-ldap = %{version}-%{release}
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

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
testrb -Ilib test
%{?scl:"}
%{?scl:scl enable %{scl} "}
#rspec spec
%{?scl:"}
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/License.rdoc
%exclude %{gem_instdir}/.autotest
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/.rspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/Contributors.rdoc
%doc %{gem_instdir}/Hacking.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/autotest
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/test
%{gem_instdir}/testserver

%changelog
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
