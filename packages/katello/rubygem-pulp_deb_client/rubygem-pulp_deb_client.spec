# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name pulp_deb_client
%global gem_require_name %{gem_name}

%global release 1
# %%global prerelease b1
# %%global prereleaserpm %{?prerelease:.}%{?prerelease}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.17.1

Release: %{?prereleaserpm:0.}%{release}%{?prereleaserpm}%{?dist}
Summary: Pulp 3 DEB plugin API Ruby Gem
Group: Development/Languages
License: GPL-2.0+
URL: https://github.com/pulp/pulp_deb/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9
Requires: %{?scl_prefix_ruby}ruby(rubygems) > 1.3.1
Requires: %{?scl_prefix}rubygem(faraday) >= 0.14.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1
Requires: %{?scl_prefix_ruby}rubygem(json) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9
BuildRequires: %{?scl_prefix_ruby}rubygems-devel > 1.3.1
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Client bindings for the pulp_deb pulp3 plugin

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

%setup -q -D -T -n  %{gem_name}-%{version}%{?prerelease}

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
%exclude %{gem_instdir}/git_push.sh
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

#workaround for https://pulp.plan.io/issues/8950
%exclude %{gem_instdir}/dist
%exclude %{gem_instdir}/build
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/pulpcore
%exclude %{gem_instdir}/pulp_deb_client.egg-info
%exclude %{gem_instdir}/*.txt
%exclude %{gem_instdir}/*.cfg
%exclude %{gem_instdir}/*.ini
%exclude %{gem_instdir}/setup.py*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/pulp_deb_client.gemspec
%{gem_instdir}/spec

%changelog
* Thu Apr 21 2022 ianballou <ianballou67@gmail.com> 2.17.1-1
- Update to 2.17.1

* Tue Nov 02 2021 ianballou <ianballou67@gmail.com> 2.16.0-1
- Update to 2.16.0

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 2.15.0-1
- Update to 2.15.0

* Tue Sep 14 2021 Justin Sherrill <jsherril@redhat.com> 2.13.1-1
- Update to 2.13.1

* Tue Jul 06 2021 James Jeffers <jjeffers@redhat.com> 2.13.0-1
- Update to 2.13.0

* Tue Apr 27 2021 Quirin Pamp <pamp@atix.de> 2.11.1-1
- Update to 2.11.1

* Mon Apr 12 2021 Justin Sherrill <jsherril@redhat.com> 2.10.0-1
- Update to 2.10.0

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.8.0-2
- Rebuild for Ruby 2.7

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 2.8.0-1
- Update to 2.8.0

* Thu Oct 15 2020 Justin Sherrill <jsherril@redhat.com> 2.7.0-1
- Update to 2.7.0

* Wed May 13 2020 Markus Bucher <bucher@atix.de> - 2.3.0-0.1.b1
- Add rubygem-pulp_deb_client generated by gem2rpm using the scl template
