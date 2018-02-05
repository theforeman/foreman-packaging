# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name bastion

Summary:    UI plugin for Foreman providing AngularJS structure
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    6.1.8
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv2+
URL:        https://github.com/katello/bastion
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires: foreman >= 1.15.0
Requires: %{?scl_prefix}rubygem(angular-rails-templates) >= 1.0.2

BuildRequires: foreman-assets >= 1.17.0
BuildRequires: foreman-plugin >= 1.17.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(angular-rails-templates) >= 1.0.2


%description
Bastion serves as a plugin to Foreman that provides common
elements for an AngularJS based UI component for a feature.
The structure, common elements, and development tasks serve as
a basis for any plugin to quickly scaffold and create a UI that
takes advantage of the Foreman (or Foreman plugin) API to create
a modern UI.

%package doc
Summary:    Documentation for rubygem-%{gem_name}
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%package devel
Summary:   Provides asset compilation dependencies for %{scl_prefix}rubygem-%{gem_name}
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires:  %{?scl_prefix_ror}rubygem(uglifier)
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-devel}

%description devel
This package contains assets compilation dependencies for %{scl_prefix}rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/vendor
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{gem_instdir}/LICENSE
%{gem_instdir}/Rakefile

%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/.jshintrc
%exclude %{gem_instdir}/grunt
%exclude %{gem_instdir}/bastion.js
%exclude %{gem_instdir}/Gruntfile.js
%exclude %{gem_instdir}/bower.json
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/eslint.yaml
%exclude %{gem_instdir}/.eslintignore
%exclude %{gem_dir}/cache

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%files devel

%changelog
* Thu Feb 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.1.7-1
- Release rubygem-bastion 6.1.7 (ericdhelms@gmail.com)

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 6.1.5-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)

* Mon Nov 20 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.1.5-1
- Bump rubygem-bastion to 6.1.5 (ewoud@kohlvanwijngaarden.nl)

* Tue Oct 03 2017 Daniel Lobato Garcia <me@daniellobato.me> 6.0.0-1
- Release rubygem-bastion 6.0.0 (eric.d.helms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Aug 22 2017 Eric D. Helms <ericdhelms@gmail.com> 5.0.10-1
- Release rubygem-bastion 5.0.10 (ericdhelms@gmail.com)

* Sat Aug 19 2017 Michael Moll <kvedulv@kvedulv.de> 5.0.9-1
- Release rubygem-bastion 5.0.9 (eric.d.helms@gmail.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Tue Jun 13 2017 Eric D. Helms <ericdhelms@gmail.com> 5.0.6-1
- Update rubygem-bastion to 5.0.6 (ericdhelms@gmail.com)

* Wed Mar 29 2017 Eric D. Helms <ericdhelms@gmail.com> 5.0.0-1
- Update rubygem-bastion to 5.0.0 (ericdhelms@gmail.com)

* Mon Mar 27 2017 Eric D. Helms <ericdhelms@gmail.com> 4.3.0-1
- Bump rubygem-bastion to 4.3.0 (ericdhelms@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Jan 26 2017 Eric D Helms <ericdhelms@gmail.com> 4.2.2-1
- Update rubygem-bastion to 4.2.2 (ericdhelms@gmail.com)

* Thu Jan 26 2017 Eric D Helms <ericdhelms@gmail.com> 4.2.1-1
- Update rubygem-bastion to 4.2.1 (ericdhelms@gmail.com)

* Thu Dec 22 2016 Eric D Helms <ericdhelms@gmail.com> 4.0.0-1
- Bump bastion to 4.0.0 (ericdhelms@gmail.com)

* Sat Nov 19 2016 Eric D Helms <ericdhelms@gmail.com> 3.4.4-1
- Bump rubygem-bastion to 3.4.4 (ericdhelms@gmail.com)

* Mon Sep 12 2016 Dominic Cleal <dominic@cleal.org> 3.3.4-1
- Update rubygem-bastion to 3.3.4 (ericdhelms@gmail.com)

* Wed Aug 24 2016 Dominic Cleal <dominic@cleal.org> 3.3.2-1
- Update rubygem-bastion to 3.3.2 (ericdhelms@gmail.com)

* Tue Jul 12 2016 Dominic Cleal <dominic@cleal.org> 3.3.0-1
- Update rubygem-bastion to 3.3.0 (ericdhelms@gmail.com)

* Fri Jun 03 2016 Dominic Cleal <dominic@cleal.org> 3.2.2-2
- Bump to ensure EVR is higher than fm1_12

* Tue May 31 2016 Eric D Helms <ericdhelms@gmail.com> 3.2.2-1
- Update rubygem-bastion to 3.2.2 (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 3.2.1-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Fri Mar 18 2016 Dominic Cleal <dominic@cleal.org> 3.2.1-1
- Bump rubygem-bastion to 3.2.1 (ericdhelms@gmail.com)

* Mon Feb 22 2016 Dominic Cleal <dominic@cleal.org> 3.2.0-1
- Update rubygem-bastion to 3.2.0 (ericdhelms@gmail.com)

* Wed Jan 20 2016 Dominic Cleal <dcleal@redhat.com> 3.0.1-1
- Update rubygem-bastion to 3.0.1 (ericdhelms@gmail.com)

* Tue Jan 12 2016 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-1
- Update rubygem-bastion to 3.0.0 (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 2.0.4-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Dec 18 2015 Dominic Cleal <dcleal@redhat.com> 2.0.4-1
- Update bastion to 2.0.4 (ericdhelms@gmail.com)

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> 2.0.3-1
- Update rubygem-bastion to 2.0.3 (ericdhelms@gmail.com)

* Tue Sep 15 2015 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- Update rubygem-bastion to 2.0.1 (ericdhelms@gmail.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Converted to tfm SCL (dcleal@redhat.com)
- Better branched builds with Foreman version macro (dcleal@redhat.com)

* Wed Jun 17 2015 Eric D. Helms <ericdhelms@gmail.com> 2.0.0-1
- Update rubygem-bastion to 2.0.0 (ericdhelms@gmail.com)

* Fri May 29 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- Update 'rubygem-bastion' to 1.0.2 (ericdhelms@gmail.com)

* Mon Apr 13 2015 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update bastion to 1.0.1 (dcleal@redhat.com)

* Mon Apr 06 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-1
- Update 'rubygem-bastion' to 1.0.0 (ericdhelms@gmail.com)

* Mon Mar 30 2015 Dominic Cleal <dcleal@redhat.com> 0.3.1-1
- Update package 'rubygem-bastion' to 0.3.1 (ericdhelms@gmail.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-1
- Update rubygem-bastion to 0.3.0 (ericdhelms@gmail.com)

* Wed Mar 04 2015 Dominic Cleal <dcleal@redhat.com> 0.2.9-1
- Update package rubygem-bastion to 0.2.9 (ericdhelms@gmail.com)

* Fri Feb 27 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.8-1
- Update rubygem-bastion to 0.2.8 (ericdhelms@gmail.com)

* Tue Feb 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.7-1
- Update package rubygem-bastion to 0.2.7 (ericdhelms@gmail.com)

* Mon Feb 23 2015 Dominic Cleal <dcleal@redhat.com> 0.2.6-2
- Default options in foreman_precompile_plugin changed (rubygem-bastion)
  (martin.bacovsky@gmail.com)

* Wed Feb 18 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.6-1
- Update rubygem-bastion to 0.2.6 (ericdhelms@gmail.com)

* Thu Feb 12 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.5-1
- Update rubygem-bastion to 0.2.5 (ericdhelms@gmail.com)

* Mon Feb 09 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.2-1
- Remove angular-rails-templates version dependency on rubygem-bastion
  (ericdhelms@gmail.com)

* Tue Feb 03 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update bastion to 0.2.0 (ericdhelms@gmail.com)

* Tue Jan 13 2015 Dominic Cleal <dcleal@redhat.com> 0.1.13-1
- Update rubygem-bastion to 0.1.13 (ericdhelms@gmail.com)

* Tue Dec 09 2014 Eric D. Helms <ericdhelms@gmail.com> 0.1.12-1
- Update rubygem-bastion to 0.1.12 (ericdhelms@gmail.com)

* Mon Dec 01 2014 Eric D. Helms <ericdhelms@gmail.com> 0.1.10-1
- Update rubygem-bastion to 0.1.10 (ericdhelms@gmail.com)

* Tue Nov 18 2014 Dominic Cleal <dcleal@redhat.com> 0.1.9-1
- Update 'rubygem-bastion' to 0.1.9 (ericdhelms@gmail.com)

* Wed Nov 12 2014 Dominic Cleal <dcleal@redhat.com> 0.1.8-1
- Update 'rubygem-bastion' to 0.1.8 (ericdhelms@gmail.com)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.1.7-2
- Convert bastion to use asset precompilation RPM macros (dcleal@redhat.com)

* Tue Oct 28 2014 Dominic Cleal <dcleal@redhat.com> 0.1.7-1
- Update rubygem-bastion to 0.1.7 (ericdhelms@gmail.com)

* Wed Oct 22 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update bastion to 0.1.5 (dcleal@redhat.com)

* Tue Oct 21 2014 Dominic Cleal <dcleal@redhat.com> 0.1.4-1
- Update 'rubygem-bastion' 0.1.4 (ericdhelms@gmail.com)

* Fri Oct 17 2014 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- new package built with tito (ericdhelms@gmail.com)
