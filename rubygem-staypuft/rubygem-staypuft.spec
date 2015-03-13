%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name staypuft

%define _version 0.5.21
%define _summary OpenStack Foreman Installer
%define _url https://github.com/theforeman/staypuft
%define _license GPLv3

%define desc OpenStack Foreman Installer

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   1%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides:  foreman-plugin-staypuft

%if 0%{?fedora} > 18
Requires:  %{?scl_prefix}ruby(release)
%else
Requires:  %{?scl_prefix}ruby(abi)
%endif
Requires:  %{?scl_prefix}rubygems

Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(dynflow) >= 0.7.0
Requires: %{?scl_prefix}rubygem(dynflow) < 0.8.0
Requires: %{?scl_prefix}rubygem(foreman_discovery) >= 1.4.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.6.4
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 0.7.0
Requires: %{?scl_prefix}rubygem(ipaddress)
Requires: %{?scl_prefix}rubygem(wicked)

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi)
%endif
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: foreman-assets >= 1.7.0
BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 0.7.0
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 0.8.0
BuildRequires: %{?scl_prefix}rubygem(foreman_discovery)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.6.4
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 0.7.0
BuildRequires: %{?scl_prefix}rubygem(ipaddress)
BuildRequires: %{?scl_prefix}rubygem(wicked)

%description
%{desc}

%package   doc
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:   Documentation for %{pkg_name}

%description doc
This package contains documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%if 0%{?fedora} > 18
%gem_install
%else
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V --local --install-dir .%{gem_dir} --force --rdoc \
    %{gem_name}-%{version}.gem
%{?scl:"}
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/config
%{gem_instdir}/Rakefile
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_instdir}/test
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
* Fri Mar 13 2015 Brad P. Crochet <brad@redhat.com> 0.5.21-1
- Update staypuft to 0.5.21 (brad@redhat.com)

* Wed Mar 11 2015 Dominic Cleal <dcleal@redhat.com> 0.5.20-1
- Update staypuft to 0.5.20 (brad@redhat.com)

* Mon Feb 23 2015 Dominic Cleal <dcleal@redhat.com> 0.5.19-2
- Default options in foreman_precompile_plugin changed (rubygem-staypuft)
  (martin.bacovsky@gmail.com)

* Thu Feb 12 2015 Brad P. Crochet <brad@redhat.com> 0.5.19-1
- Update staypuft to 0.5.19 (brad@redhat.com)

* Mon Feb 09 2015 Dominic Cleal <dcleal@redhat.com> 0.5.18-1
- Update staypuft to 0.5.18 (dcleal@redhat.com)

* Tue Jan 27 2015 Dominic Cleal <dcleal@redhat.com> 0.5.17-1
- Update staypuft to version 0.5.17 (brad@redhat.com)

* Mon Jan 26 2015 Dominic Cleal <dcleal@redhat.com> 0.5.16-1
- Update staypuft to 0.5.16 (sseago@redhat.com)

* Thu Jan 22 2015 Dominic Cleal <dcleal@redhat.com> 0.5.14-1
- Update staypuft to 0.5.14 (dcleal@redhat.com)

* Wed Jan 21 2015 Lukas Zapletal <lzap+rpm@redhat.com> 0.5.13-1
- Removed discovery version hard dependency
- Updated package to 0.5.13

* Fri Jan 16 2015 Dominic Cleal <dcleal@redhat.com> 0.5.12-1
- Update staypuft to 0.5.12 (sseago@redhat.com)

* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.5.11-1
- Update staypuft to 0.5.11 (sseago@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 0.5.10-1
- Update staypuft to 0.5.10 (dcleal@redhat.com)

* Fri Jan 02 2015 Dominic Cleal <dcleal@redhat.com> 0.5.9-1
- Update staypuft to 0.5.9 (brad@redhat.com)

* Thu Dec 18 2014 Dominic Cleal <dcleal@redhat.com> 0.5.7-1
- Update staypuft to 0.5.7 (dcleal@redhat.com)

* Wed Dec 17 2014 Dominic Cleal <dcleal@redhat.com> 0.5.6-1
- Update staypuft to 0.5.6 (dcleal@redhat.com)

* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 0.5.5-1
- Update staypuft to 0.5.5 (dcleal@redhat.com)

* Wed Dec 10 2014 Dominic Cleal <dcleal@redhat.com> 0.5.4-1
- Update staypuft to 0.5.4 (dcleal@redhat.com)

* Tue Dec 09 2014 Dominic Cleal <dcleal@redhat.com> 0.5.3-1
- Update staypuft to 0.5.3 (brad@redhat.com)

* Mon Dec 08 2014 Dominic Cleal <dcleal@redhat.com> 0.5.2-1
- Update staypuft to 0.5.2 (brad@redhat.com)
- Modernise and have requires match gemspec (dcleal@redhat.com)

* Thu Nov 20 2014 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- Update staypuft to 0.5.0 (sseago@redhat.com)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.4.12-2
- Convert staypuft to use asset precompilation RPM macros (dcleal@redhat.com)

* Thu Oct 30 2014 Dominic Cleal <dcleal@redhat.com> 0.4.12-1
- Update staypuft to 0.4.12 (brad@redhat.com)

* Mon Oct 13 2014 Dominic Cleal <dcleal@redhat.com> 0.4.4-1
- Update staypuft to 0.4.4 (brad@redhat.com)
- Add ipaddress gem dependency (brad@redhat.com)

* Thu Sep 25 2014 Marek Hulan <mhulan@redhat.com> 0.3.9-1
- Update staypuft to 0.3.9 (mhulan@redhat.com)

* Wed Sep 10 2014 Marek Hulan <mhulan@redhat.com> 0.3.4-1
- Update staypuft to 0.3.4 (mhulan@redhat.com)

* Tue Sep 09 2014 Marek Hulan <mhulan@redhat.com> 0.3.2-1
- Update staypuft to 0.3.2 (mhulan@redhat.com)

* Thu Sep 04 2014 Marek Hulan <mhulan@redhat.com> 0.3.1-1
- Update staypuft to 0.3.1 (mhulan@redhat.com)

* Mon Aug 25 2014 Marek Hulan <mhulan@redhat.com> 0.3.0-1
- new package built with tito

* Tue Jul 22 2014 Marek Hulan <mhulan@redhat.com> 0.1.19-1
- Update staypuft (mhulan@redhat.com)

* Tue Jul 22 2014 Marek Hulan <mhulan@redhat.com> 0.1.18-1
- Update staypuft (mhulan@redhat.com)

* Wed Jul 16 2014 Marek Hulan <mhulan@redhat.com> 0.1.17-1
- Update staypuft (mhulan@redhat.com)

* Thu Jul 10 2014 Marek Hulan <mhulan@redhat.com> 0.1.9-1
- Update staypuft (mhulan@redhat.com)

* Thu Jul 03 2014 Marek Hulan <mhulan@redhat.com> 0.1.7-1
- Update staypuft (mhulan@redhat.com)

* Fri Jun 27 2014 Marek Hulan <mhulan@redhat.com> 0.1.5-2
- Add staypuft deps (mhulan@redhat.com)

* Thu Jun 26 2014 Marek Hulan <mhulan@redhat.com> 0.1.5-1
- Update staypuft (mhulan@redhat.com)

* Thu Jun 19 2014 Marek Hulan <mhulan@redhat.com> 0.1.4-2
- Update release (mhulan@redhat.com)
- Add missing gem (mhulan@redhat.com)

* Thu Jun 19 2014 Marek Hulan <mhulan@redhat.com> 0.1.4-1
- Update staypuft (mhulan@redhat.com)

* Mon Jun 16 2014 Marek Hulan <mhulan@redhat.com> 0.1.3-1
- Update staypuft (mhulan@redhat.com)

* Fri Jun 13 2014 Marek Hulan <mhulan@redhat.com> 0.1.2-1
- Update staypuft (mhulan@redhat.com)

* Fri Jun 06 2014 Marek Hulan <mhulan@redhat.com> 0.1.1-1
- Update staypuft to 0.1.1 (mhulan@redhat.com)

* Wed Jun 04 2014 Marek Hulan <mhulan@redhat.com> 0.1.0-1
- Update staypuft to 0.1.0 (mhulan@redhat.com)

* Thu May 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.16-1
- Update staypuft (mhulan@redhat.com)

* Thu May 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.15-1
- Update staypuft (mhulan@redhat.com)

* Tue May 20 2014 Marek Hulan <mhulan@redhat.com> 0.0.14-1
- Staypuft update (mhulan@redhat.com)

* Thu May 15 2014 Marek Hulan <mhulan@redhat.com> 0.0.13-1
- Update staypuft to 0.0.13 (mhulan@redhat.com)

* Fri May 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.12-1
- Update staypuft (mhulan@redhat.com)

* Wed Apr 23 2014 Marek Hulan <mhulan@redhat.com> 0.0.11-5
- Update staypuft to official 0.0.11 (mhulan@redhat.com)

* Tue Apr 22 2014 Eric D. Helms <ericdhelms@gmail.com> 0.0.11-4
- Staypuft update to 0.0.11 (ericdhelms@gmail.com)

* Tue Apr 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.10-3
- Update staypuft gem to released version (mhulan@redhat.com)

* Mon Apr 21 2014 Eric D. Helms <ericdhelms@gmail.com> 0.0.10-2
- Staypuft update to 0.0.10 (ericdhelms@gmail.com)

* Tue Apr 15 2014 Marek Hulan <mhulan@redhat.com> 0.0.9-1
- Staypuft update to 0.0.9 (mhulan@redhat.com)

* Mon Apr 14 2014 Marek Hulan <mhulan@redhat.com> 0.0.8-1
- Update staypuft to 0.0.8 (mhulan@redhat.com)

* Thu Apr 10 2014 Marek Hulan <mhulan@redhat.com> 0.0.7-1
- Update staypuft (mhulan@redhat.com)

* Thu Apr 10 2014 Marek Hulan <mhulan@redhat.com> 0.0.6-1
- Update staypuft (mhulan@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-3
- Fix requirement for packaged staypuft gemfile (mhulan@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-2
- Fix staypuft doc dependency (mhulan@redhat.com)
- Add foreman-plugin-staypuft provides (dcleal@redhat.com)
- Remove superfluous quotes (dcleal@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-1
- Update staypuft to 0.0.4 (mhulan@redhat.com)
- Precompile assets of staypuft (mhulan@redhat.com)

* Mon Apr 07 2014 Marek Hulan <mhulan@redhat.com> 0.0.3-1
- Update staypuft to 0.0.3 (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-4
- Hopefully last hack staypuft 0.0.2 version (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-3
- Another hacked version of staypuft (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-2
- Hacked staypuft version without oj dependency (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-1
- Update staypuft to 0.0.2 (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.1-2
- Integrate staypuft into foreman (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.1-1
- new package built with tito


