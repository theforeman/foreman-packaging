%define rbname bundler
%define version 1.0.15
%define release 1

Summary: The best way to manage your application's dependencies
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://gembundler.com
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(bundler) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/bundle
%{gemdir}/gems/bundler-1.0.15/.gitignore
%{gemdir}/gems/bundler-1.0.15/CHANGELOG.md
%{gemdir}/gems/bundler-1.0.15/ISSUES.md
%{gemdir}/gems/bundler-1.0.15/LICENSE
%{gemdir}/gems/bundler-1.0.15/README.md
%{gemdir}/gems/bundler-1.0.15/Rakefile
%{gemdir}/gems/bundler-1.0.15/UPGRADING.md
%{gemdir}/gems/bundler-1.0.15/bin/bundle
%{gemdir}/gems/bundler-1.0.15/bundler.gemspec
%{gemdir}/gems/bundler-1.0.15/lib/bundler.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/capistrano.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/cli.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/definition.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/dependency.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/deployment.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/dsl.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/environment.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/gem_helper.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/gem_tasks.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/graph.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/index.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/installer.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/lazy_specification.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/lockfile_parser.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/remote_specification.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/resolver.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/rubygems_ext.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/rubygems_integration.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/runtime.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/settings.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/setup.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/shared_helpers.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/source.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/spec_set.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/Executable
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/Gemfile
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/newgem/Gemfile.tt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/newgem/Rakefile.tt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/newgem/bin/newgem.tt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/newgem/gitignore.tt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/newgem/lib/newgem.rb.tt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/newgem/lib/newgem/version.rb.tt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/templates/newgem/newgem.gemspec.tt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/ui.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/actions.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/actions/create_file.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/actions/directory.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/actions/empty_directory.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/actions/file_manipulation.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/actions/inject_into_file.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/base.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/core_ext/file_binary_read.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/core_ext/hash_with_indifferent_access.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/core_ext/ordered_hash.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/error.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/invocation.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/parser.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/parser/argument.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/parser/arguments.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/parser/option.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/parser/options.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/shell.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/shell/basic.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/shell/color.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/shell/html.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/task.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/util.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vendor/thor/version.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/version.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/vlad.rb
%{gemdir}/gems/bundler-1.0.15/man/bundle-config.ronn
%{gemdir}/gems/bundler-1.0.15/man/bundle-exec.ronn
%{gemdir}/gems/bundler-1.0.15/man/bundle-install.ronn
%{gemdir}/gems/bundler-1.0.15/man/bundle-package.ronn
%{gemdir}/gems/bundler-1.0.15/man/bundle-update.ronn
%{gemdir}/gems/bundler-1.0.15/man/bundle.ronn
%{gemdir}/gems/bundler-1.0.15/man/gemfile.5.ronn
%{gemdir}/gems/bundler-1.0.15/man/index.txt
%{gemdir}/gems/bundler-1.0.15/spec/cache/gems_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/cache/git_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/cache/path_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/cache/platform_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/deploy_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/deprecated_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/c_ext_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/env_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/flex_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/groups_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/packed_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/platform_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/resolving_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/simple_case_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/sudo_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gems/win32_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/gemspec_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/git_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/invalid_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/path_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/install/upgrade_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/lock/git_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/lock/lockfile_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/check_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/config_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/console_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/exec_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/ext_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/gem_helper_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/help_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/init_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/newgem_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/open_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/other/show_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/pack/gems_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/quality_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/resolver/basic_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/resolver/platform_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/runtime/executable_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/runtime/load_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/runtime/platform_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/runtime/require_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/runtime/setup_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/runtime/with_clean_env_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/spec_helper.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/builders.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/helpers.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/indexes.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/matchers.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/path.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/platforms.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/ruby_ext.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/rubygems_ext.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/rubygems_hax/platform.rb
%{gemdir}/gems/bundler-1.0.15/spec/support/sudo.rb
%{gemdir}/gems/bundler-1.0.15/spec/update/gems_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/update/git_spec.rb
%{gemdir}/gems/bundler-1.0.15/spec/update/source_spec.rb
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-benchmark
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-benchmark.txt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-config
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-config.txt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-exec
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-exec.txt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-install
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-install.txt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-package
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-package.txt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-update
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle-update.txt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/bundle.txt
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/gemfile.5
%{gemdir}/gems/bundler-1.0.15/lib/bundler/man/gemfile.5.txt


%doc %{gemdir}/doc/bundler-1.0.15
%{gemdir}/cache/bundler-1.0.15.gem
%{gemdir}/specifications/bundler-1.0.15.gemspec

%changelog
