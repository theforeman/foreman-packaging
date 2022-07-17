# template: default
%global gem_name faraday

Name: rubygem-%{gem_name}
Version: 2.3.0
Release: 1%{?dist}
Summary: HTTP/REST API client library
License: MIT
URL: https://lostisland.github.io/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
HTTP/REST API client library.


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
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Sun Jul 17 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.3.0-1
- Update to 2.3.0

* Wed Jul 13 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.8.0-1
- Update to 1.8.0

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
