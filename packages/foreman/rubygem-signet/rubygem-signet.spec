# Generated from signet-0.11.0.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name signet

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.14.0
Release: 2%{?dist}
Summary: Signet is an OAuth 1.0 / OAuth 2.0 implementation
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/google/signet/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.4.0
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.5
Requires: %{?scl_prefix}rubygem(addressable) >= 2.3
Requires: %{?scl_prefix}rubygem(addressable) < 3
Requires: %{?scl_prefix}rubygem(faraday) >= 0.17.3
Requires: %{?scl_prefix}rubygem(faraday) < 2.0
Requires: %{?scl_prefix}rubygem(jwt) >= 1.5
Requires: %{?scl_prefix}rubygem(jwt) < 3.0
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.10
Requires: %{?scl_prefix}rubygem(multi_json) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.4.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.5
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Signet is an OAuth 1.0 / OAuth 2.0 implementation.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/website
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/signet.gemspec
%{gem_instdir}/spec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.14.0-2
- Rebuild against rh-ruby27

* Thu Oct 08 2020 Ondřej Ezr <oezr@redhat.com> 0.14.0-1
- Update to 0.14.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.11.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.11.0-2
- Update spec to remove the ror scl

* Mon Feb 25 2019 Evgeni Golov 0.11.0-1
- Update to 0.11.0-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.6.0-7
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.6.0-6
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.6.0-5
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.6.0-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.6.0-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.6.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 0.6.0-1
- Update signet to 0.6.0 (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- Update signet to 0.5.1 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.4.5-1
- new package built with tito
