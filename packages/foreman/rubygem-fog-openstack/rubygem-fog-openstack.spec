# Generated from fog-openstack-1.0.8.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-openstack

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.8
Release: 4%{?dist}
Summary: OpenStack fog provider gem
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-openstack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.2.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-core) >= 2.1
Requires: %{?scl_prefix}rubygem(fog-core) < 3
Requires: %{?scl_prefix}rubygem(fog-json) >= 1.0
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
OpenStack fog provider gem.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.hound.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.ruby-gemset
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.zuul.yaml
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/playbooks
%{gem_instdir}/supported.md
%{gem_instdir}/unit
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docker-compose.yml
%doc %{gem_instdir}/docs
%{gem_instdir}/examples
%{gem_instdir}/fog-openstack.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.8-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.8-3
- Bump to release for EL8

* Thu Mar 28 2019 Evgeni Golov 1.0.8-2
- Regen SPEC based on GEM and new template

* Wed Mar 20 2019 Marek Hulan <mhulan@redhat.com> 1.0.8-1
- Update to 1.0.8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.25-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jun 06 2018 Daniel Lobato Garcia <me@daniellobato.me> 0.1.25-1
- Update to 0.1.25

* Tue Jan 23 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.23-1
- Update fog-openstack to 0.1.23 (me@daniellobato.me)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.18-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Jan 04 2017 Dominic Cleal <dominic@cleal.org> 0.1.18-1
- Update fog-openstack to 0.1.18 (dominic@cleal.org)

* Mon Sep 05 2016 Dominic Cleal <dominic@cleal.org> 0.1.12-1
- Update fog-openstack to 0.1.12 (dominic@cleal.org)

* Wed Aug 10 2016 Dominic Cleal <dominic@cleal.org> 0.1.11-1
- Update fog-openstack to 0.1.11 (dominic@cleal.org)

* Thu Aug 04 2016 Dominic Cleal <dominic@cleal.org> 0.1.10-1
- Update fog-openstack to 0.1.10 (dominic@cleal.org)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 0.1.8-1
- Update fog-openstack to 0.1.8 (dominic@cleal.org)

* Thu Mar 31 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- new package built with tito

