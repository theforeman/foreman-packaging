# template: default
%global gem_name rabl

Name: rubygem-%{gem_name}
Version: 0.17.0
Release: 1%{?dist}
Summary: General ruby templating with json, bson, xml and msgpack support
License: MIT
URL: https://github.com/nesquena/rabl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
General ruby templating with json, bson, xml and msgpack support.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Nov 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.17.0-1
- Update to 0.17.0

* Sun Oct 16 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.16.1-1
- Update to 0.16.1

* Fri Aug 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.16.0-1
- Update to 0.16.0

* Fri May 13 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.15.0-1
- Release rubygem-rabl 0.15.0

* Fri May 13 2022 Eric D. Helms <ericdhelms@gmail.com> 0.15.0-1
- Update to 0.15.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.14.3-2
- Rebuild against rh-ruby27

* Fri May 01 2020 Michel Moll <mmoll@mmoll.at> - 0.14.3-1
- Update rubygem-rabl to 0.14.3

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.13.1-4
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.13.1-3
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.13.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 0.13.1-1
- Bump rubygem-rabl to 0.13.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.12.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Fri Feb 26 2016 Dominic Cleal <dominic@cleal.org> 0.12.0-1
- Update rabl to 0.12.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.11.6-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.11.6-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jul 15 2015 Walden Raines <walden@redhat.com> 0.11.6-1
- Update rabl to 0.11.6 (walden@redhat.com)

* Tue Nov 25 2014 Dominic Cleal <dcleal@redhat.com> 0.11.4-1
- Update rabl to 0.11.4 (dcleal@redhat.com)

* Wed Jan 22 2014 Justin Sherrill <jsherril@redhat.com> 0.9.0-1
- upgrading to new rabl version 0.9.0 (jsherril@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.7.6-5
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.6-3
- new package built with tito

* Thu Nov 15 2012 Martin Bačovský <mbacovsk@redhat.com> 0.7.6-2
- Updated to 0.7.6 (mbacovsk@redhat.com)

* Mon Aug 20 2012 Ivan Necas <inecas@redhat.com> 0.7.1-1
- initial package
