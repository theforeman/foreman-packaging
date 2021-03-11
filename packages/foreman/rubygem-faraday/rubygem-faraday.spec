# Generated from faraday-0.15.4.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name faraday

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.17.3
Release: 2%{?dist}
Summary: HTTP/REST API client library
Group: Development/Languages
License: MIT
URL: https://github.com/lostisland/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(multipart-post) >= 1.2
Requires: %{?scl_prefix}rubygem(multipart-post) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
HTTP/REST API client library.


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
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.17.3-2
- Rebuild against rh-ruby27

* Thu Oct 08 2020 Ondřej Ezr <oezr@redhat.com> 0.17.3-1
- Update to 0.17.3

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.15.4-2
- Bump to release for EL8

* Thu Mar 14 2019 kgaikwad <kavitagaikwad103@gmail.com> 0.15.4-1
- Update to 0.15.4

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.9.1-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.9.1-5
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Refs #18123 revert "change multipart-post dep to RPM name from virtual"
  (github@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Wed Jan 18 2017 Dominic Cleal <dominic@cleal.org> 0.9.1-4
- Change multipart-post dep to RPM name from virtual (#18123)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.9.1-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.9.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 0.9.1-1
- Update faraday to 0.9.1 (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.9.0-1
- Update faraday to 0.9.0 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.8.8-1
- new package built with tito
