# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_remote_execution
%global plugin_name remote_execution
%global foreman_min_version 1.17.0

Summary:    Plugin that brings remote execution capabilities to Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.5.3
Release:    2%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_remote_execution
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.0.1
Requires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
Requires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.13
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 1
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.0.1
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.13
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

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
#BuildRequires: npm(enzyme) >= 3.2.0
#BuildRequires: npm(enzyme) < 4.0.0
#BuildRequires: npm(enzyme-adapter-react-16) >= 1.1.0
#BuildRequires: npm(enzyme-adapter-react-16) < 2.0.0
#BuildRequires: npm(enzyme-to-json) >= 3.1.2
#BuildRequires: npm(enzyme-to-json) < 4.0.0
#BuildRequires: npm(eslint) >= 4.10.0
#BuildRequires: npm(eslint) < 5.0.0
#BuildRequires: npm(eslint-config-airbnb) >= 16.0.0
#BuildRequires: npm(eslint-config-airbnb) < 17.0.0
#BuildRequires: npm(eslint-plugin-import) >= 2.8.0
#BuildRequires: npm(eslint-plugin-import) < 3.0.0
#BuildRequires: npm(eslint-plugin-jest) >= 21.2.0
#BuildRequires: npm(eslint-plugin-jest) < 22.0.0
#BuildRequires: npm(eslint-plugin-jsx-a11y) >= 6.0.2
#BuildRequires: npm(eslint-plugin-jsx-a11y) < 7.0.0
#BuildRequires: npm(eslint-plugin-react) >= 7.4.0
#BuildRequires: npm(eslint-plugin-react) < 8.0.0
#BuildRequires: npm(jest) >= 21.2.1
#BuildRequires: npm(jest) < 22.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: npm(babel-polyfill) >= 6.26.0
BuildRequires: npm(babel-polyfill) < 7.0.0
BuildRequires: npm(prop-types) >= 15.6.0
BuildRequires: npm(prop-types) < 16.0.0
BuildRequires: npm(react) >= 16.2.0
BuildRequires: npm(react) < 17.0.0
BuildRequires: npm(react-dom) >= 16.2.0
BuildRequires: npm(react-dom) < 17.0.0
BuildRequires: npm(react-redux) >= 5.0.6
BuildRequires: npm(react-redux) < 6.0.0
BuildRequires: npm(redux) >= 3.7.2
BuildRequires: npm(redux) < 4.0.0
BuildRequires: npm(seamless-immutable) >= 7.1.3
BuildRequires: npm(seamless-immutable) < 8.0.0
BuildRequires: npm(urijs) >= 1.19.0
BuildRequires: npm(urijs) < 2.0.0
# end package.json dependencies BuildRequires

%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.

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
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.babelrc
%exclude %{gem_instdir}/.eslintignore
%exclude %{gem_instdir}/.eslintrc
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.hound.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.tx
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%exclude %{gem_instdir}/foreman_remote_execution.gemspec
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
%{gem_instdir}/Gemfile
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
* Mon Jun 18 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.5.3-2
- Regenerate spec file based on the current template

* Thu Jun 14 2018 Ivan Nečas <inecas@redhat.com> 1.5.3-1
- Update to 1.5.3

* Wed May 16 2018 Ivan Nečas <inecas@redhat.com> 1.5.2-1
- Update to 1.5.2

* Thu Apr 19 2018 Daniel Lobato Garcia <me@daniellobato.me> 1.5.1-1
- Update to 1.5.1

* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.5.0-1
- Update to 1.5.0

* Wed Mar 14 2018 Adam Ruzicka <aruzicka@redhat.com> 1.4.6-1
- Update foreman_remote_execution to 1.4.6 (aruzicka@redhat.com.com)

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.5-1
- Update foreman_remote_execution to 1.4.5 (mhulan@redhat.com)

* Mon Jan 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.2-1
- drop doc directory (aruzicka@redhat.com)
- Update rubygem-foreman_remote_execution to 1.4.2 (aruzicka@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jul 26 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.3-1
- Bump foreman_remote_execution to 1.3.3 (inecas@redhat.com)

* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.2-1
- Update foreman_remote_execution to 1.3.2 (inecas@redhat.com)

* Wed May 31 2017 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update foreman_remote_execution to 1.3.1 (inecas@redhat.com)

* Tue Apr 11 2017 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update foreman_remote_execution to 1.3.0 (aruzicka@redhat.com)

* Fri Jan 27 2017 Dominic Cleal <dominic@cleal.org> 1.2.2-1
- Update foreman_remote_execution to 1.2.2 (inecas@redhat.com)

* Tue Sep 20 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Update foreman_remote_execution to 1.2.1 (inecas@redhat.com)

* Tue Aug 23 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update foreman_remote_execution to 1.1.0 (inecas@redhat.com)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- Release foreman_remote_execution 1.0 (stephen@redhat.com)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-2
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 28 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-1
- Release foreman_remote_execution 0.3.2 (RPM) (stephen@redhat.com)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- Release foreman_remote_execution 0.3.0 (stbenjam@redhat.com)

* Fri Feb 12 2016 Dominic Cleal <dcleal@redhat.com> 0.2.3-1
- Release foreman_remote_execution 0.2.3 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Release foreman_remote_execution 0.2.2 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.2.1-1
- Release foreman_remote_execution 0.2.1 (stbenjam@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 13 2015 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- Update foreman_remote_execution to 0.1.1 (stbenjam@redhat.com)

* Mon Oct 12 2015 Dominic Cleal <dcleal@redhat.com> 0.0.10-1
- Update foreman_remote_execution to 0.0.10 (inecas@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Release foreman_remote_execution 0.0.7 (stbenjam@redhat.com)

* Mon Sep 14 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Release foreman_remote_execution 0.0.6 (stbenjam@redhat.com)

* Wed Sep 02 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release Remote Execution Plugins 0.0.5 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release foreman_remote_execution 0.0.4 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- Release foreman_remote_execution 0.0.3 (stbenjam@redhat.com)

* Tue Aug 18 2015 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial release of 0.0.2
