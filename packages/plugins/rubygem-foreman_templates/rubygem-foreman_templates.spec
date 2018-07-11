# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_templates
%global plugin_name templates
%global foreman_min_version 1.18.0

Summary:    Template-syncing engine for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    6.0.3
Release:    1%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_templates
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: git
BuildRequires: git
# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(diffy)
Requires: %{?scl_prefix}rubygem(git)
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(diffy)
BuildRequires: %{?scl_prefix}rubygem(git)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Engine to synchronise provisioning templates from GitHub.


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
%foreman_precompile_plugin -a

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
* Wed Jul 11 2018 Marek Hulan <mhulan@redhat.com> 6.0.3-1
- Update to 6.0.3

* Wed Jul 04 2018 Marek Hulan <mhulan@redhat.com> 6.0.2-1
- Update to 6.0.2

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 6.0.1-2
- Regenerate spec file based on the current template

* Thu May 17 2018 Marek Hulan <mhulan@redhat.com> 6.0.1-1
- Update to 6.0.1

* Tue Apr 10 2018 Marek Hulan <mhulan@redhat.com> 6.0.0-1
- Update to 6.0.0

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.1-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 31 2017 Dominic Cleal <dominic@cleal.org> 5.0.1-1
- Update foreman_templates to 5.0.1 (mhulan@redhat.com)

* Wed Apr 26 2017 Dominic Cleal <dominic@cleal.org> 5.0.0-1
- Update foreman_templates to 5.0.0 (mhulan@redhat.com)

* Fri Apr 21 2017 Dominic Cleal <dominic@cleal.org> 4.0.2-1
- Update foreman_templates to 4.0.2 (mhulan@redhat.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Fri Feb 03 2017 Dominic Cleal <dominic@cleal.org> 4.0.1-1
- templates: 4.0.1 release (greg.sutcliffe@gmail.com)

* Tue Oct 04 2016 Dominic Cleal <dominic@cleal.org> 3.1.0-1
- templates: 3.1.0 release (greg.sutcliffe@gmail.com)

* Thu Sep 08 2016 Dominic Cleal <dominic@cleal.org> 3.0.0-1
- templates: 3.0.0 release (greg.sutcliffe@gmail.com)

* Thu May 12 2016 Dominic Cleal <dominic@cleal.org> 2.1.0-1
- Update foreman_templates to 2.1.0 (gsutclif@redhat.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.0.3-1
- Update foreman_templates to 2.0.3 (dcleal@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 2.0.1-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Dec 02 2015 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- Update foreman_templates to 2.0.1 (dcleal@redhat.com)
- Add foremandist macro (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Jul 06 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update foreman_templates to 2.0.0 (dcleal@redhat.com)

* Wed Mar 18 2015 Dominic Cleal <dcleal@redhat.com> 1.5.0-1
- Update foreman_templates to 1.5.0 (dcleal@redhat.com)

* Wed Feb 26 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-2
- Add git dependency (dcleal@redhat.com)

* Thu Jan 30 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-1
- Update to foreman_templates 1.4.0 (dcleal@redhat.com)

* Fri Dec 06 2013 Dominic Cleal <dcleal@redhat.com> 1.3.2-1
- Update to foreman_templates 1.3.2 (dcleal@redhat.com)

* Fri Dec 06 2013 Dominic Cleal <dcleal@redhat.com> 1.3.1-1
- Update to foreman_templates 1.3.1 (dcleal@redhat.com)

* Thu Dec 05 2013 Dominic Cleal <dcleal@redhat.com> 1.3.0-1
- Update to foreman_templates 1.3.0 (dcleal@redhat.com)

* Wed Nov 20 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- new package built with tito
