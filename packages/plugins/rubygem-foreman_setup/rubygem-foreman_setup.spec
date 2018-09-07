# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_setup
%global plugin_name setup
%global foreman_min_version 1.17.0

Summary:    Helps set up Foreman for provisioning
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    6.0.0
Release:    3%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_setup
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Plugin for Foreman that helps set up provisioning.


%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{pkg_name}

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

%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.tx
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_restart}
exit 0

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 6.0.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 6.0.0-2
- Regenerate spec file based on the current template

* Mon Apr 02 2018 Michael Moll <mmoll@moll.at> 6.0.0-1
- Update foreman_setup to 6.0.0 (mmoll@moll.at)

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.0-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Aug 04 2016 Dominic Cleal <dominic@cleal.org> 5.0.0-1
- Update foreman_setup to 5.0.0 (dominic@cleal.org)

* Fri Jul 01 2016 Dominic Cleal <dominic@cleal.org> 4.0.0-1
- Update foreman_setup to 4.0.0 (dominic@cleal.org)

* Wed Jun 01 2016 Dominic Cleal <dominic@cleal.org> 3.1.1-1
- Update foreman_setup to 3.1.1 (dominic@cleal.org)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 3.1.0-1
- Update foreman_setup to 3.1.0 (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.2-1
- Update foreman_setup to 3.0.2 (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Jul 30 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-1
- Update foreman_setup to 3.0.1 (dcleal@redhat.com)

* Mon Jul 06 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-1
- Update foreman_setup to 3.0.0 (dcleal@redhat.com)

* Thu Nov 20 2014 Dominic Cleal <dcleal@redhat.com> 2.1.1-1
- Update to v2.1.1 (dcleal@redhat.com)

* Mon Sep 22 2014 Dominic Cleal <dcleal@redhat.com> 2.1.0-1
- Update to v2.1.0 (dcleal@redhat.com)

* Thu May 08 2014 Dominic Cleal <dcleal@redhat.com> 2.0.4-1
- Update to v2.0.4 (dcleal@redhat.com)

* Thu Apr 24 2014 Dominic Cleal <dcleal@redhat.com> 2.0.3-1
- Update to v2.0.3 (dcleal@redhat.com)

* Mon Apr 07 2014 Lukas Zapletal <lzap+git@redhat.com> 2.0.2-5
- Dropping some requires for foreman_setup (lzap+git@redhat.com)

* Mon Apr 07 2014 Lukas Zapletal <lzap+git@redhat.com> 2.0.2-4
- Fixed build requires and assets for foreman_setup (lzap+git@redhat.com)

* Fri Apr 04 2014 Lukas Zapletal <lzap+git@redhat.com> 2.0.2-3
- Adding asset building to foreman_setup (lzap+git@redhat.com)

* Fri Apr 04 2014 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.2-2
- Added asset precompilation

* Thu Apr 03 2014 Dominic Cleal <dcleal@redhat.com> 2.0.2-1
- Update to v2.0.2 (dcleal@redhat.com)
- Add ugilifier dep as workaround for issue #12 (dcleal@redhat.com)

* Wed Mar 05 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to v2.0.0, Foreman 1.5 (dcleal@redhat.com)

* Thu Jan 30 2014 Dominic Cleal <dcleal@redhat.com> 1.0.4-1
- Update to v1.0.4 (dcleal@redhat.com)

* Tue Jan 28 2014 Dominic Cleal <dcleal@redhat.com> 1.0.3-1
- Update to v1.0.3 (dcleal@redhat.com)

* Thu Nov 21 2013 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- Update to v1.0.2 (dcleal@redhat.com)

* Tue Oct 29 2013 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update to v1.0.1 (dcleal@redhat.com)

* Tue Oct 29 2013 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- new package built with tito
