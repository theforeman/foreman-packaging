%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name signet
%global rubyabi 1.9.1

Summary: Signet is an OAuth 1.0 / OAuth 2.0 implementation
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.0
Release: 2%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/google/signet/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(addressable) >= 2.3
Requires: %{?scl_prefix}rubygem(addressable) < 3.0
Requires: %{?scl_prefix}rubygem(extlib) >= 0.9
Requires: %{?scl_prefix}rubygem(extlib) < 1.0
Requires: %{?scl_prefix}rubygem(faraday) >= 0.9
Requires: %{?scl_prefix}rubygem(faraday) < 1.0
Requires: %{?scl_prefix}rubygem(jwt) >= 1.0
Requires: %{?scl_prefix}rubygem(jwt) < 2.0
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.10
Requires: %{?scl_prefix}rubygem(multi_json) < 2.0

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Signet is an OAuth 1.0 / OAuth 2.0 implementation.

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
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

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
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/Gemfile*
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/signet.gemspec
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/tasks

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/website

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.6.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Update signet to 0.6.0 (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- Update signet to 0.5.1 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.4.5-1
- new package built with tito
