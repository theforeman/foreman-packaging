# template: default
%global gem_name signet

Name: rubygem-%{gem_name}
Version: 0.17.0
Release: 1%{?dist}
Summary: Signet is an OAuth 1.0 / OAuth 2.0 implementation
License: Apache-2.0
URL: https://github.com/googleapis/signet
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel >= 1.3.5
BuildArch: noarch
# end specfile generated dependencies

%description
Signet is an OAuth 1.0 / OAuth 2.0 implementation.


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
%exclude %{gem_instdir}/.yardopts
%{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/SECURITY.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.17.0-1
- Update to 0.17.0

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
