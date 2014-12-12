%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_api

Summary: Ruby bindings for Forman's rest API
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.11
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/theforeman/foreman_api
Source0:  http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires: %{?scl_prefix}ruby(abi)
%else
Requires: %{?scl_prefix}ruby(release)
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(json)
Requires: %{?scl_prefix}rubygem(rest-client) >= 1.6.1
Requires: %{?scl_prefix}rubygem(oauth)
%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
BuildRequires: %{?scl_prefix}ruby(abi)
%else
BuildRequires: %{?scl_prefix}ruby(release)
%endif
BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Helps you to use Foreman's API calls from your app.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -c -T -n  %{gem_name}-%{version}


%build
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --no-rdoc --no-ri %{SOURCE0}
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mv %{buildroot}%{gem_instdir}/{MIT-LICENSE,README.rdoc} ./
mkdir -p %{buildroot}%{gem_docdir}
mv %{buildroot}%{gem_instdir}/doc %{buildroot}%{gem_docdir}
rm -f %{buildroot}%{gem_instdir}/.yardopts
rm -f %{buildroot}%{gem_instdir}/.gitignore

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%doc MIT-LICENSE README.rdoc

%files doc
%doc %{gem_docdir}

%changelog
* Fri Dec 12 2014 Dominic Cleal <dcleal@redhat.com> 0.1.11-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Mon Jan 27 2014 Martin Bačovský <mbacovsk@redhat.com> 0.1.11-1
- Bump to 0.1.11 (mbacovsk@redhat.com)

* Thu Jan 23 2014 Martin Bačovský <mbacovsk@redhat.com> 0.1.10-1
- Bump to 0.1.10 (mbacovsk@redhat.com)

* Thu Dec 19 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.9-1
- Bump to 0.1.9 (mbacovsk@redhat.com)

* Thu Oct 31 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.8-1
- Version bumped to 0.1.8 (mbacovsk@redhat.com)
- fixed methods in puppet class imports
- updated hosts create parameters

* Mon Oct 21 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.7-1
- Version bumped to 0.1.7 (mbacovsk@redhat.com)

* Mon Aug 26 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.6-1
- Version bump to 0.1.7 (mbacovsk@redhat.com)
- updated api for hosts and media

* Tue Jul 30 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.5-2
- Fixed deps for F19 (mbacovsk@redhat.com)

* Tue Jul 30 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.5-1
- Version bump to 0.1.5 (mbacovsk@redhat.com)
- fixed issue 8: Remove escaped character from generated documentation in rb file
- updated to latest API

* Thu Jun 27 2013 Lukas Zapletal <lzap+git@redhat.com> 0.1.4-3
- adding non-SCL RHEL6 support (lzap+git@redhat.com)

* Thu Jun 27 2013 Lukas Zapletal <lzap+git@redhat.com> 0.1.4-2
- removing hard Rubi ABI requirement (lzap+git@redhat.com)

* Thu Jun 20 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.4-1
- Updated to 0.1.4 (mbacovsk@redhat.com)
- updated API (Foreman 1.2)
- fixed docs (lzap@redhat.com)
- fixed headers options handling (tstracho@redhat.com)


* Tue Apr 09 2013 Ivan Necas <inecas@redhat.com> 0.1.3-1
- Update to new version (inecas@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.1-2
- new package built with tito

* Wed Feb 13 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.1-1
- Bump to 0.1.1 (mbacovsk@redhat.com)
- Added support for extra options for restclient resource

* Wed Feb 06 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.0-1
- Updated to 0.1.0 (mbacovsk@redhat.com)
- Added support for API V2
- Removed unnecessary dependency on apipie-rails

* Thu Jan 24 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.11-1
- Updated to 0.0.11 (mbacovsk@redhat.com)
- generator is part of the package
- yard docs

* Tue Jan 15 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.10-1
- Fixed params handeling (mbacovsk@redhat.com)

* Fri Jan 11 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.9-1
- Bump to 0.0.9 (mbacovsk@redhat.com) ( compute_resource domain environment host
   common_parameter hostgroup image medium operating_system ptable
   puppetclass role template_kind )


* Thu Nov 22 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.8-1
- Updated to 0.0.8 (mbacovsk@redhat.com)

* Thu Nov 22 2012 Martin Bacovsky <mbacovsk@redhat.com> 0.0.8-1
- support for full foreman API

* Wed Oct 17 2012 Ivan Necas <inecas@redhat.com> 0.0.7-2
- Fix apipie-rails dependency (inecas@redhat.com)

* Tue Oct 09 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.7-1
- Rebuilt with apipie 0.0.12 (mbacovsk@redhat.com)

* Tue Sep 11 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.6-1
- Updated to 0.0.6 (mbacovsk@redhat.com)
- support for subnets

* Tue Aug 28 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.5-1
- Updated bindings to 0.0.5 (mbacovsk@redhat.com)

* Tue Aug 14 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.4-2
- Updated to v 0.0.4 (mbacovsk@redhat.com)
- added domains, config_templates

* Tue Aug 14 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.2-1
- Updated gem to 0.0.2 (mbacovsk@redhat.com)

* Mon Aug 13 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.1-4
- for rubyabi do s/1.9/1.9.1/ (msuchy@redhat.com)

* Mon Aug 13 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.1-3
- Fixed failing spec removal (mbacovsk@redhat.com)

* Mon Aug 13 2012 Martin Bačovský <mbacovsk@redhat.com> 0.0.1-2
- new package built with tito

* Wed Aug 08 2012 Martin Bacovsky <mbacovsk@redhat.com> - 0.0.1-1
- Initial package
