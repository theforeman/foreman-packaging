# Generated from foreman_ansible-3.0.0.gem by gem2rpm -*- rpm-spec -*-
# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_ansible
%global plugin_name ansible
%global foreman_min_version 1.22.0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.0
Release: 1%{?foremandist}%{?dist}
Summary: Ansible integration with Foreman (theforeman.org)
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface) < 2.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 1
Requires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 1.7.0
Requires: %{?scl_prefix}rubygem(foreman_remote_execution) < 2.0
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8.0
Requires: %{?scl_prefix}rubygem(ipaddress) < 1.0
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 1
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 1.7.0
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution) < 2.0
BuildRequires: %{?scl_prefix}rubygem(ipaddress) >= 0.8.0
BuildRequires: %{?scl_prefix}rubygem(ipaddress) < 1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
#BuildRequires: npm(babel-eslint) >= 8.2.1
#BuildRequires: npm(babel-eslint) < 9.0.0
BuildRequires: npm(babel-plugin-lodash) >= 3.3.2
BuildRequires: npm(babel-plugin-lodash) < 4.0.0
BuildRequires: npm(babel-plugin-transform-class-properties) >= 6.24.1
BuildRequires: npm(babel-plugin-transform-class-properties) < 7.0.0
BuildRequires: npm(babel-plugin-transform-object-assign) >= 6.22.0
BuildRequires: npm(babel-plugin-transform-object-assign) < 7.0.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) >= 6.26.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) < 7.0.0
BuildRequires: npm(babel-preset-env) >= 1.6.0
BuildRequires: npm(babel-preset-env) < 2.0.0
BuildRequires: npm(babel-preset-react) >= 6.24.1
BuildRequires: npm(babel-preset-react) < 7.0.0
#BuildRequires: npm(enzyme) >= 3.7.0
#BuildRequires: npm(enzyme) < 4.0.0
#BuildRequires: npm(enzyme-adapter-react-16) >= 1.7.0
#BuildRequires: npm(enzyme-adapter-react-16) < 2.0.0
#BuildRequires: npm(enzyme-to-json) >= 3.3.5
#BuildRequires: npm(enzyme-to-json) < 4.0.0
#BuildRequires: npm(eslint) >= 4.18.1
#BuildRequires: npm(eslint) < 5.0.0
#BuildRequires: npm(eslint-config-airbnb) >= 16.0.0
#BuildRequires: npm(eslint-config-airbnb) < 17.0.0
#BuildRequires: npm(eslint-plugin-import) >= 2.8.0
#BuildRequires: npm(eslint-plugin-import) < 3.0.0
#BuildRequires: npm(eslint-plugin-jest) >= 21.2.0
#BuildRequires: npm(eslint-plugin-jest) < 22.0.0
#BuildRequires: npm(eslint-plugin-jsx-a11y) >= 6.0.2
#BuildRequires: npm(eslint-plugin-jsx-a11y) < 7.0.0
#BuildRequires: npm(eslint-plugin-patternfly-react) >= 0.2.1
#BuildRequires: npm(eslint-plugin-patternfly-react) < 1.0.0
#BuildRequires: npm(eslint-plugin-react) >= 7.4.0
#BuildRequires: npm(eslint-plugin-react) < 8.0.0
BuildRequires: npm(identity-obj-proxy) >= 3.0.0
BuildRequires: npm(identity-obj-proxy) < 4.0.0
#BuildRequires: npm(jest) >= 23.6.0
#BuildRequires: npm(jest) < 24.0.0
#BuildRequires: npm(prettier) >= 1.16.4
#BuildRequires: npm(prettier) < 2.0.0
BuildRequires: npm(react-redux) >= 6.0.0
BuildRequires: npm(react-redux) < 7.0.0
#BuildRequires: npm(react-redux-test-utils) >= 0.1.1
#BuildRequires: npm(react-redux-test-utils) < 1.0.0
BuildRequires: npm(redux) >= 4.0.1
BuildRequires: npm(redux) < 5.0.0
BuildRequires: npm(redux-thunk) >= 2.3.0
BuildRequires: npm(redux-thunk) < 3.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: npm(babel-polyfill) >= 6.26.0
BuildRequires: npm(babel-polyfill) < 7.0.0
BuildRequires: npm(classnames) >= 2.2.6
BuildRequires: npm(classnames) < 3.0.0
BuildRequires: npm(lodash) = 4.17.10
BuildRequires: npm(patternfly) >= 3.58.0
BuildRequires: npm(patternfly) < 4.0.0
BuildRequires: npm(patternfly-react) >= 2.25.4
BuildRequires: npm(patternfly-react) < 3.0.0
BuildRequires: npm(prop-types) >= 15.7.2
BuildRequires: npm(prop-types) < 16.0.0
BuildRequires: npm(react) >= 16.6.3
BuildRequires: npm(react) < 17.0.0
BuildRequires: npm(react-bootstrap) >= 0.32.4
BuildRequires: npm(react-bootstrap) < 1.0.0
BuildRequires: npm(react-dom) >= 16.6.3
BuildRequires: npm(react-dom) < 17.0.0
BuildRequires: npm(react-json-tree) >= 0.11.0
BuildRequires: npm(react-json-tree) < 1.0.0
BuildRequires: npm(reselect) >= 3.0.1
BuildRequires: npm(reselect) < 4.0.0
BuildRequires: npm(seamless-immutable) = 7.1.2
# end package.json dependencies BuildRequires

%description
Ansible integration with Foreman.


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
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
* Thu Apr 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.0.0-1
- Update to 3.0.0-1

* Fri Apr 12 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.3-2
- Rebuild rubygem-foreman_ansible for webpack

* Thu Apr 11 2019 Marek Hulan <mhulan@redhat.com> 2.3.3-1
- Update to 2.3.3

* Thu Apr 04 2019 Marek Hulan - 2.3.2-4
- Rebuild Ansible for webpack

* Thu Mar 28 2019 Evgeni Golov - 2.3.2-3
- Rebuild Ansible for webpack

* Tue Mar 26 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.2-2
- Rebuild rubygem-foreman_ansible for webpack

* Thu Mar 07 2019 Marek Hulan <mhulan@redhat.com> 2.3.2-1
- Update to 2.3.2

* Mon Feb 25 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.1-4
- Rebuild rubygem-foreman_ansible for webpack

* Tue Feb 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.1-3
- Rebuild rubygem-foreman_ansible for webpack

* Thu Feb 14 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.1-2
- Rebuild rubygem-foreman_ansible for webpack

* Fri Jan 25 2019 Marek Hulan <mhulan@redhat.com> 2.3.1-1
- Update to 2.3.1

* Thu Jan 24 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-5
- Rebuild rubygem-foreman_ansible for webpack

* Mon Jan 21 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-4
- Rebuild for webpack

* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-3
- Rebuild for webpack

* Tue Jan 08 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-2
- Rebuild for webpack

* Thu Nov 22 2018 Marek Hulan <mhulan@redhat.com> 2.3.0-1
- Update to 2.3.0

* Mon Nov 19 2018 Marek Hulan <mhulan@redhat.com> 2.2.11-1
- Update to 2.2.11

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.9-3
- Revbump to correct source map handling

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.9-2
- Use the license macro
- Remove rpmlint warnings

* Tue Sep 25 2018 Marek Hulan <mhulan@redhat.com> 2.2.9-1
- Update to 2.2.9

* Thu Sep 13 2018 Marek Hulan <mhulan@redhat.com> 2.2.7-1
- Update to 2.2.7

* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.6-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Aug 15 2018 Sebastian Gräßl <mail@bastilian.me> 2.2.6-1
- Update to 2.2.6

* Wed Jul 25 2018 Marek Hulan <mhulan@redhat.com> 2.2.5-1
- Update to 2.2.5

* Fri Jul 13 2018 Marek Hulan <mhulan@redhat.com> 2.2.3-1
- Update to 2.2.3

* Thu Jul 12 2018 Marek Hulan <mhulan@redhat.com> 2.2.2-1
- Update to 2.2.2

* Wed Jul 04 2018 Marek Hulan <mhulan@redhat.com> 2.2.1-1
- Update to 2.2.1

* Mon Jul 02 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.2.0-1
- Update to 2.2.0

* Wed Jun 27 2018 Ondrej Prazak <oprazak@redhat.com> 2.1.2-2
- Plugin rebuild

* Fri Apr 06 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.0.4-1
- Update to 2.0.4

* Fri Apr 06 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.0.2-1
- Update to 2.0.2

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-1
- Bump foreman_ansible to 2.0.1 (me@daniellobato.me)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Apr 07 2017 Dominic Cleal <dominic@cleal.org> 1.4.5-1
- Update foreman_ansible to 1.4.5 (me@daniellobato.me)

* Tue Feb 14 2017 Dominic Cleal <dominic@cleal.org> 1.4.4-1
- Update foreman_ansible to 1.4.4 (me@daniellobato.me)

* Mon Jan 30 2017 Dominic Cleal <dominic@cleal.org> 1.4.2-1
- Update foreman-ansible to 1.4.2 (me@daniellobato.me)

* Fri Jan 20 2017 Dominic Cleal <dominic@cleal.org> 1.4.1-1
- Release foreman_ansible 1.4.1 (me@daniellobato.me)

* Wed Dec 21 2016 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update foreman_ansible to 1.3.1 (me@daniellobato.me)

* Mon Dec 05 2016 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update foreman-ansible to 1.3.0 (me@daniellobato.me)

* Mon Oct 03 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Update foreman-ansible to 1.2.1 (me@daniellobato.me)

* Fri Jul 08 2016 Dominic Cleal <dominic@cleal.org> 1.0-1
- plugins:foreman_ansible - 1.0.0 (elobatocs@gmail.com)

* Thu Feb 11 2016 Dominic Cleal <dcleal@redhat.com> 0.3-1
- plugins:foreman_ansible - Release 0.3 (elobatocs@gmail.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-2
- Obsolete ruby193 variant from 1.8/1.9 (dcleal@redhat.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Release 0.2.2 (elobatocs@gmail.com)

* Sat Jan 02 2016 Daniel Lobato <elobatocs@gmail.com> 0.2.1-1
- Initial package
