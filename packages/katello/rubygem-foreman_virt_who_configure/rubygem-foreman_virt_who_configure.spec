# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_virt_who_configure
%global plugin_name virt_who_configure
%global foreman_min_version 1.20

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.5
Release: 2%{?foremandist}%{?dist}
Summary: A plugin to make virt-who configuration easy
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_virt_who_configure
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(katello)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(katello)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
A plugin to make virt-who configuration easy.


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

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.5-2
- Rebuild for Ruby 2.7

* Mon Dec 14 2020 Jonathon Turel <jturel@gmail.com> 0.5.5-1
- Update to 0.5.5

* Mon Nov 30 2020 Jonathon Turel <jturel@gmail.com> 0.5.4-1
- Update to 0.5.4

* Thu Sep 10 2020 Jonathon Turel <jturel@gmail.com> 0.5.3-1
- Update to 0.5.3

* Mon Mar 02 2020 Marek Hulan <mhulan@redhat.com> 0.5.2-1
- Update to 0.5.2

* Tue Feb 25 2020 Marek Hulan <mhulan@redhat.com> 0.5.1-1
- Update to 0.5.1

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.5.0-2
- Drop migrate, seed and restart posttans

* Tue Nov 19 2019 Marek Hulan <mhulan@redhat.com> 0.5.0-1
- Update to 0.5.0

* Tue Oct 22 2019 Marek Hulan <mhulan@redhat.com> 0.4.5-1
- Update to 0.4.5

* Thu Sep 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.4-2
- Regenerate the spec file based on the latest foreman_plugin template

* Mon Sep 09 2019 Marek Hulan <mhulan@redhat.com> 0.4.4-1
- Update to 0.4.4

* Tue Aug 20 2019 Marek Hulan <mhulan@redhat.com> 0.4.3-1
- Update to 0.4.3

* Thu May 23 2019 Marek Hulan <mhulan@redhat.com> 0.4.1-1
- Update to 0.4.1

* Wed Feb 27 2019 Marek Hulan <mhulan@redhat.com> 0.4.0-1
- Update to 0.4.0

* Tue Jan 15 2019 Marek Hulan <mhulan@redhat.com> 0.3.2-1
- Update to 0.3.2

* Fri Nov 23 2018 Marek Hulan <mhulan@redhat.com> 0.3.0-1
- Update to 0.3.0

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.2.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jun 15 2018 Marek Hulan <mhulan@redhat.com> 0.2.2-1
- Update to 0.2.2

* Wed May 30 2018 Marek Hulan <mhulan@redhat.com> 0.2.1-1
- Update to 0.2.1

* Tue Apr 10 2018 Marek Hulan <mhulan@redhat.com> 0.2.0-1
- Update to 0.2.0

* Thu Dec 28 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.9-1
- new package built with tito

* Thu Oct 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.8-2
- Fixes #21455 - generate apipie cache during build (mhulan@redhat.com)

* Thu Oct 12 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.8-1
- Update foreman_virt_who_configure to 0.1.8 (mhulan@redhat.com)

* Tue Sep 26 2017 Justin Sherrill <jsherril@redhat.com> 0.1.7-1
- Update foreman_virt_who_configure to 0.1.7 (mhulan@redhat.com)

* Thu Aug 24 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.5-1
- Update foreman_virt_who_configure to 0.1.5 (mhulan@redhat.com)
- Update foreman_virt_who_configure to 0.1.4 (mhulan@redhat.com)

* Mon Jun 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.3-1
- Update foreman_virt_who_configure to 0.1.3 (mhulan@redhat.com)

* Tue Jun 13 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.2-1
- Update foreman_virt_who_configure to 0.1.2 (mhulan@redhat.com)

* Fri May 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.1-1
- Update foreman_virt_who_configure to 0.1.1 (mhulan@redhat.com)

* Thu May 18 2017 Justin Sherrill <jsherril@redhat.com> 0.1.0-1
- Update foreman_virt_who_configure to 0.1.0 (mhulan@redhat.com)

* Wed May 03 2017 Justin Sherrill <jsherril@redhat.com> 0.0.2-2
- Rebuild virt_who_configure for proper tagging (jsherril@redhat.com)

* Wed May 03 2017 Justin Sherrill <jsherril@redhat.com> 0.0.2-1
- Update foreman_virt_who_configure to 0.0.2 (mhulan@redhat.com)

* Thu Apr 06 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.1-2
-

* Thu Apr 06 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.1-1
- new package built with tito

