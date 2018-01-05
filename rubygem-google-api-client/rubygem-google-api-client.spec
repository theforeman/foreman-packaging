%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name google-api-client

Summary: Google API Ruby Client makes it trivial to access supported APIs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.8.2
Release: 6%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/google/google-api-ruby-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ror}rubygem(activesupport) >= 3.2
Requires: %{?scl_prefix}rubygem(addressable) >= 2.3
Requires: %{?scl_prefix}rubygem(addressable) < 3.0
Requires: %{?scl_prefix}rubygem(autoparse) >= 0.3
Requires: %{?scl_prefix}rubygem(autoparse) < 1.0
Requires: %{?scl_prefix}rubygem(extlib) >= 0.9
Requires: %{?scl_prefix}rubygem(extlib) < 1.0
Requires: %{?scl_prefix}rubygem(faraday) >= 0.9
Requires: %{?scl_prefix}rubygem(faraday) < 1.0
Requires: %{?scl_prefix}rubygem(launchy) >= 2.4
Requires: %{?scl_prefix}rubygem(launchy) < 3.0
Requires: %{?scl_prefix_ror}rubygem(multi_json) >= 1.10
Requires: %{?scl_prefix_ror}rubygem(multi_json) < 2.0
Requires: %{?scl_prefix}rubygem(retriable) >= 1.4
Requires: %{?scl_prefix}rubygem(retriable) < 2.0
Requires: %{?scl_prefix}rubygem(signet) >= 0.6
Requires: %{?scl_prefix}rubygem(signet) < 1.0
Requires: ca-certificates

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
The Google API Ruby Client makes it trivial to discover and access supported
APIs.

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
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# kill bundled cacert.pem
ln -sf /etc/pki/tls/cert.pem \
  %{buildroot}%{gem_libdir}/cacert.pem

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/google-api-client.gemspec
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.8.2-5
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.8.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.8.2-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.8.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Jan 12 2015 Dominic Cleal <dcleal@redhat.com> 0.8.2-1
- Update google-api-client to 0.8.2 (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 0.8.1.1-1
- Update google-api-client to 0.8.1.1 (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.7.1-1
- Update google-api-client to 0.7.1 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.6.4-1
- new package built with tito
