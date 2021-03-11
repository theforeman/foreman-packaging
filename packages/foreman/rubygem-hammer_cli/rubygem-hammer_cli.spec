# template: hammer_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hammer_cli

%global release 2
%global prereleasesource pre.develop
%global prerelease %{?prereleasesource:.}%{?prereleasesource}

%{!?_root_bindir:%global _root_bindir %{_bindir}}
%{!?_root_mandir:%global _root_mandir %{_mandir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}
%global hammer_confdir %{_root_sysconfdir}/hammer

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.5.0
Release: %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary: Universal command-line interface
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/hammer-cli
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(clamp) >= 1.1
Requires: %{?scl_prefix}rubygem(clamp) < 1.2.0
Requires: %{?scl_prefix}rubygem(logging)
Requires: %{?scl_prefix}rubygem(unicode-display_width)
Requires: %{?scl_prefix}rubygem(unicode)
Requires: %{?scl_prefix}rubygem(amazing_print)
Requires: %{?scl_prefix}rubygem(highline)
Requires: %{?scl_prefix}rubygem(fast_gettext)
Requires: %{?scl_prefix}rubygem(locale) >= 2.0.6
Requires: %{?scl_prefix}rubygem(apipie-bindings) >= 0.2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Hammer cli provides universal extendable CLI interface for ruby apps.


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

sed -i '1s@/.*@/usr/bin/%{?scl_prefix}ruby@' .%{_bindir}/*
mkdir -p %{buildroot}%{_root_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_root_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_root_sysconfdir}/bash_completion.d
mv %{buildroot}%{gem_instdir}/config/hammer.completion %{buildroot}%{_root_sysconfdir}/bash_completion.d/%{gem_name}

mkdir -p %{buildroot}%{_root_mandir}/man1
mv %{buildroot}%{gem_instdir}/man/hammer.1.gz %{buildroot}%{_root_mandir}/man1/
rm -f %{buildroot}%{gem_instdir}/man/*.asciidoc

mkdir -p %{buildroot}%{hammer_confdir}/cli.modules.d
install -m 0644 .%{gem_instdir}/config/cli_config.template.yml \
                %{buildroot}%{hammer_confdir}/cli_config.yml

%files
%dir %{gem_instdir}
%{_root_bindir}/hammer
%{_root_bindir}/hammer-complete
%doc %{_root_mandir}/man1/hammer.1.gz
%{_root_sysconfdir}/bash_completion.d/%{gem_name}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{hammer_confdir}/cli.modules.d
%config %{hammer_confdir}/cli_config.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config
%doc %{gem_instdir}/doc
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.5.0-0.2.pre.develop
- Rebuild against rh-ruby27

* Tue Feb 02 2021 Evgeni Golov - 2.5.0-0.1.pre.develop
- Bump version to 2.5-develop

* Mon Nov 02 2020 Patrick Creech <pcreech@redhat.com> - 2.4.0-0.1.pre.develop
- Bump version to 2.4-develop

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-0.1.pre.develop
- Bump version to 2.3-develop

* Wed Jun 03 2020 Evgeni Golov - 2.2.0-0.3.pre.develop
- Regenerate spec file based on recent template

* Mon May 18 2020 Michael Moll <mmoll@mmoll.at> - 2.2.0-0.2.pre.develop
- Change awesome_print dependency to amazing_print

* Thu May 14 2020 Shira Maximov <shiramaximov@gmail.com> - 2.2.0-0.1.pre.develop
- Bumped to 2.2.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-0.2.pre.develop
- Bump to release for EL8

* Thu Feb 13 2020 Tomer Brisker <tbrisker@gmail.com> - 2.1.0-0.1.pre.develop
- bump to 2.1-develop

* Sun Feb 09 2020 Tomer Brisker <tbrisker@gmail.com> - 2.0.0-0.1.pre.develop
- bump to 2.0-develop

* Fri Jan 03 2020 Ondrej Prazak - 0.20-0.3.pre.develop
- Fix path to autocomplete script

* Mon Nov 18 2019 Evgeni Golov - 0.20-0.2.pre.develop
- Unify prerelease macro handling

* Mon Oct 28 2019 Evgeni Golov - 0.20-0.1.pre.develop
- Bump to 0.20-develop

* Fri Aug 02 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.19-0.1.pre.develop
- Bump to 0.19-develop

* Wed Jul 17 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.18-0.2.pre.develop
- Do not install configs as executable files (#27326)

* Thu Apr 25 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.18-0.1.pre.develop
- Bump to 0.18-develop

* Fri Jan 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.17-0.1.pre.develop
- Bump to 0.17-develop

* Thu Oct 25 2018 Adam Price <komidore64@gmail.com> - 0.16-0.2.pre.develop
- add nightly macro

* Thu Oct 25 2018 Adam Price <komidore64@gmail.com> - 0.16-0.1.pre.develop
- bump version to 0.16

* Wed Sep 12 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.15-0.2.pre.develop
- Add prerelease support

* Mon Aug 27 2018 Martin Bacovsky <mbacovsk@redhat.com> 0.14.0-1
- Update to 0.14.0

* Thu Aug 16 2018 Martin Bacovsky <mbacovsk@redhat.com> 0.13.1-1
- Update to 0.13.1

* Thu May 10 2018 Martin Bacovsky <mbacovsk@redhat.com> 0.13.0-1
- Update to 0.13.0

* Tue Feb 20 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.12.0-1
- Update rubygem-hammer_cli to 0.12.0 (martin.bacovsky@gmail.com)
- Restructure foreman packages to prepare for obal (pcreech@redhat.com)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.11.0-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Add rubygem-unicode (github@kohlvanwijngaarden.nl)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.11.0-1
- Update hammer_cli to 0.11.0 (tstrachota@redhat.com)

* Fri May 05 2017 Dominic Cleal <dominic@cleal.org> 0.10.2-1
- Update hammer-cli to 0.10.2 (tstrachota@redhat.com)

* Tue Apr 25 2017 Dominic Cleal <dominic@cleal.org> 0.10.1-1
- Update hammer_cli to 0.10.1 (dominic@cleal.org)
- refs #19083 - require apipie-bindings >= 0.2.0 (dominic@cleal.org)

* Wed Mar 29 2017 Eric D. Helms <ericdhelms@gmail.com> 0.10.0-1
- Update hammer_cli to 0.10.0 (tstrachota@redhat.com)
- Add LICENSE file, clarify doc/license tags (dominic@cleal.org)
- Remove table_print (dominic@cleal.org)

* Mon Dec 19 2016 Dominic Cleal <dominic@cleal.org> 0.9.0-1
- Update hammer_cli to 0.9.0 (dominic@cleal.org)

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> 0.8.0-1
- Update hammer_cli to 0.8.0 (dominic@cleal.org)
- Package man page from gem into mandir (#7453, dominic@cleal.org)

* Fri Jun 17 2016 Dominic Cleal <dominic@cleal.org> 0.7.0-1
- Update hammer_cli to 0.7.0 (dominic@cleal.org)

* Fri May 27 2016 Dominic Cleal <dominic@cleal.org> 0.6.1-2
- Use gem_install macro (dominic@cleal.org)

* Tue Mar 15 2016 Dominic Cleal <dominic@cleal.org> 0.6.1-1
- Update hammer_cli to 0.6.1 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.5.1-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Dec 15 2015 Tomas Strachota <tstrachota@redhat.com> 0.5.1-1
- Update hammer_cli to 0.5.1 (tstrachota@redhat.com)

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-1
- Update hammer_cli to 0.4.0 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-2
- Use tfm-ruby in shebang line (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)
- Increase range of non-SCL obsoletes to cover 1.9 versions (dcleal@redhat.com)

* Tue Aug 04 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-1
- Update hammer_cli to 0.3.0 (dcleal@redhat.com)
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)
- Require clamp >=1.0.0 (dcleal@redhat.com)

* Mon Apr 27 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update hammer_cli to 0.2.0 (dcleal@redhat.com)
- refs #10154 - require locale 2.0.6 (dcleal@redhat.com)
- Refresh hammer-cli dep versions (dcleal@redhat.com)
- refs #8829 - use config/ template from gem (dcleal@redhat.com)

* Fri Dec 12 2014 Dominic Cleal <dcleal@redhat.com> 0.1.4-1
- Update hammer_cli to 0.1.4 (martin.bacovsky@gmail.com)
- Added rb-readline dependency to rubygem-hammer_cli
  (martin.bacovsky@gmail.com)
- Refresh Hammer cli_config file (dcleal@redhat.com)

* Thu Aug 21 2014 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- Update rubygem-hammer_cli to 0.1.3 (martin.bacovsky@gmail.com)

* Thu Aug 14 2014 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Update rubygem-hammer_cli to 0.1.2 (martin.bacovsky@gmail.com)

* Tue May 20 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.1.1-1
- Rebased hammer_cli to 0.1.1 (martin.bacovsky@gmail.com)

* Wed Mar 26 2014 Martin Bačovský <martin.bacovsky@gmail.com> 0.1.0-1
- Bump to 0.1.0 (martin.bacovsky@gmail.com)
- hammer_cli - new config location and dependencies (tstrachota@redhat.com)

* Wed Jan 29 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.18-1
- Bump to 0.0.18 (mbacovsk@redhat.com)

* Thu Jan 23 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.16-1
- Bump to 0.0.16 (mbacovsk@redhat.com)

* Tue Jan 21 2014 Martin Bačovský <mbacovsk@redhat.com> 0.0.15-1
- Bump to 0.0.15 (mbacovsk@redhat.com)

* Tue Jan 07 2014 Dominic Cleal <dcleal@redhat.com> 0.0.14-2
- Require fastercsv and mime-types on Fedora to avoid gemspec conflict
  (dcleal@redhat.com)

* Thu Dec 19 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.14-1
- Bump to 0.0.14 (mbacovsk@redhat.com)

* Wed Dec 18 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.13-1
- Bump to 0.0.13 (mbacovsk@redhat.com)

* Thu Dec 05 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.12-1
- Bump to 0.0.12 (mbacovsk@redhat.com)

* Tue Nov 26 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.11-1
- Bump to 0.0.11 (mbacovsk@redhat.com)

* Fri Nov 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.9-1
- Bumped to 0.0.9 (mbacovsk@redhat.com)

* Tue Oct 29 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.8-1
- Update to Hammer CLI Foreman 0.0.8

* Wed Oct 09 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.7-1
- Bumped to 0.0.7 (mbacovsk@redhat.com)
- fixed error handling while loading hammer modules

* Tue Oct 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.6-2
- Added depenedency on fastercsv on ruby 1.8 (mbacovsk@redhat.com)

* Tue Oct 08 2013 Tomas Strachota <tstrachota@redhat.com> 0.0.6-1
- fixes #3184 - update hammer dependencies

* Thu Sep 26 2013 Sam Kottler <shk@redhat.com> 0.0.5-1
- Cherry pick hammer_cli version bump (shk@redhat.com)

* Tue Aug 27 2013 Dominic Cleal <dcleal@redhat.com> 0.0.3-4
- Install bash completion extension (dcleal@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-3
- Fix typo in macro (shk@redhat.com)
- Use macros provided by rubygems-devel on Fedora (shk@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-2
- Add configuration example to packaged files (shk@redhat.com)
- Fix readme path (shk@redhat.com)
- Add docs and other files that are new in the 0.0.3 release (shk@redhat.com)
- Add docs and other files that are new in the 0.0.3 release (shk@redhat.com)
- Bump hammer_cli version to 0.0.3 (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.2-15
- Remove SCL conditional (shk@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 0.0.2-14
- Add multi_json dependency to hammer and fix gem_dir (shk@redhat.com)
- Fix changelog (shk@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 0.0.2-13
- Add logging requirement (shk@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 0.0.2-10
- Rebuilding on RHEL

* Mon Aug 12 2013 Sam Kottler <shk@redhat.com> 0.0.2-9
- Bump version

* Mon Aug 12 2013 Sam Kottler <shk@redhat.com> 0.0.2-8
- Bump hammer version (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.0.1-7
- Add a missing %% (shk@redhat.com)
- Remove ruby(abi) for f19 (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.0.1-6
- Fix bindir (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.0.1-5
- Don't require ruby-abi on F19+ (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.0.1-4
- Rebuild

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.0.1-3
- Removed abi version for hammer_cli deps (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.0.1-2
- Initial package with tito
* Wed Jul 31 2013  <shk@redhat.com> - 0.0.1-1
- Initial package
