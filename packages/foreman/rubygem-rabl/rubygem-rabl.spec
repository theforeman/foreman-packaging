# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rabl
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.15.0
Release: 1%{?dist}
Summary: General ruby templating with json, bson, xml and msgpack support
Group: Development/Languages
License: MIT
URL: https://github.com/nesquena/rabl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activesupport) >= 2.3.14
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
General ruby templating with json, bson, xml and msgpack support.


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
