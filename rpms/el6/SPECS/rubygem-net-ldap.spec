%define rbname net-ldap
%define version 0.3.1
%define release 1

Summary: Net::LDAP for Ruby (also called net-ldap) implements client access for the Lightweight Directory Access Protocol (LDAP), an IETF standard protocol for accessing distributed directory services
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://rubyldap.com/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(net-ldap) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Net::LDAP for Ruby (also called net-ldap) implements client access for the
Lightweight Directory Access Protocol (LDAP), an IETF standard protocol for
accessing distributed directory services. Net::LDAP is written completely in
Ruby with no external dependencies. It supports most LDAP client features and
a
subset of server features as well.
Net::LDAP has been tested against modern popular LDAP servers including
OpenLDAP and Active Directory. The current release is mostly compliant with
earlier versions of the IETF LDAP RFCs (2251–2256, 2829–2830, 3377, and
3771).
Our roadmap for Net::LDAP 1.0 is to gain full <em>client</em> compliance with
the most recent LDAP RFCs (4510–4519, plus portions of 4520–4532).


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/net-ldap-0.3.1/.autotest
%{gemdir}/gems/net-ldap-0.3.1/.rspec
%doc %{gemdir}/gems/net-ldap-0.3.1/Contributors.rdoc
%doc %{gemdir}/gems/net-ldap-0.3.1/Hacking.rdoc
%doc %{gemdir}/gems/net-ldap-0.3.1/History.rdoc
%doc %{gemdir}/gems/net-ldap-0.3.1/License.rdoc
%doc %{gemdir}/gems/net-ldap-0.3.1/Manifest.txt
%doc %{gemdir}/gems/net-ldap-0.3.1/README.rdoc
%{gemdir}/gems/net-ldap-0.3.1/Rakefile
%{gemdir}/gems/net-ldap-0.3.1/autotest/discover.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net-ldap.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/ber_parser.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/core_ext.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/core_ext/array.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/core_ext/bignum.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/core_ext/false_class.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/core_ext/fixnum.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/core_ext/string.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ber/core_ext/true_class.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ldap.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ldap/dataset.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ldap/dn.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ldap/entry.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ldap/filter.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ldap/password.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/ldap/pdu.rb
%{gemdir}/gems/net-ldap-0.3.1/lib/net/snmp.rb
%{gemdir}/gems/net-ldap-0.3.1/net-ldap.gemspec
%{gemdir}/gems/net-ldap-0.3.1/spec/integration/ssl_ber_spec.rb
%{gemdir}/gems/net-ldap-0.3.1/spec/spec.opts
%{gemdir}/gems/net-ldap-0.3.1/spec/spec_helper.rb
%{gemdir}/gems/net-ldap-0.3.1/spec/unit/ber/ber_spec.rb
%{gemdir}/gems/net-ldap-0.3.1/spec/unit/ber/core_ext/string_spec.rb
%{gemdir}/gems/net-ldap-0.3.1/spec/unit/ldap/dn_spec.rb
%{gemdir}/gems/net-ldap-0.3.1/spec/unit/ldap/entry_spec.rb
%{gemdir}/gems/net-ldap-0.3.1/spec/unit/ldap/filter_spec.rb
%{gemdir}/gems/net-ldap-0.3.1/spec/unit/ldap_spec.rb
%{gemdir}/gems/net-ldap-0.3.1/test/common.rb
%{gemdir}/gems/net-ldap-0.3.1/test/test_entry.rb
%{gemdir}/gems/net-ldap-0.3.1/test/test_filter.rb
%{gemdir}/gems/net-ldap-0.3.1/test/test_ldap_connection.rb
%{gemdir}/gems/net-ldap-0.3.1/test/test_ldif.rb
%{gemdir}/gems/net-ldap-0.3.1/test/test_password.rb
%{gemdir}/gems/net-ldap-0.3.1/test/test_rename.rb
%{gemdir}/gems/net-ldap-0.3.1/test/test_snmp.rb
%{gemdir}/gems/net-ldap-0.3.1/test/testdata.ldif
%{gemdir}/gems/net-ldap-0.3.1/testserver/ldapserver.rb
%{gemdir}/gems/net-ldap-0.3.1/testserver/testdata.ldif
%{gemdir}/gems/net-ldap-0.3.1/.gemtest


%doc %{gemdir}/doc/net-ldap-0.3.1
%{gemdir}/cache/net-ldap-0.3.1.gem
%{gemdir}/specifications/net-ldap-0.3.1.gemspec

%changelog
