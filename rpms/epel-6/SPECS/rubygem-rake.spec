%define rbname rake
%define version 0.9.2.2
%define release 2

Summary: Ruby based make-like utility.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://rake.rubyforge.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.6
Requires: rubygems >= 1.3.7
BuildRequires: ruby >= 1.8.6
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: rubygem(rake) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies
arespecified in standard Ruby syntax.


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
%{_bindir}/rake
%{gemdir}/gems/rake-0.9.2.2/.gemtest
%{gemdir}/gems/rake-0.9.2.2/install.rb
%doc %{gemdir}/gems/rake-0.9.2.2/CHANGES
%doc %{gemdir}/gems/rake-0.9.2.2/MIT-LICENSE
%{gemdir}/gems/rake-0.9.2.2/Rakefile
%doc %{gemdir}/gems/rake-0.9.2.2/README.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/TODO
%{gemdir}/gems/rake-0.9.2.2/bin/rake
%{gemdir}/gems/rake-0.9.2.2/lib/rake/alt_system.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/application.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/classic_namespace.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/clean.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/cloneable.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/contrib/compositepublisher.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/contrib/ftptools.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/contrib/publisher.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/contrib/rubyforgepublisher.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/contrib/sshpublisher.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/contrib/sys.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/default_loader.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/dsl_definition.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/early_time.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/ext/core.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/ext/module.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/ext/string.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/ext/time.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/file_creation_task.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/file_list.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/file_task.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/file_utils.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/file_utils_ext.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/gempackagetask.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/invocation_chain.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/invocation_exception_mixin.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/loaders/makefile.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/multi_task.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/name_space.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/packagetask.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/pathmap.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/pseudo_status.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/rake_module.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/rake_test_loader.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/rdoctask.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/ruby182_test_unit_fix.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/rule_recursion_overflow_error.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/runtest.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/task.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/task_argument_error.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/task_arguments.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/task_manager.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/tasklib.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/testtask.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/version.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake/win32.rb
%{gemdir}/gems/rake-0.9.2.2/lib/rake.rb
%{gemdir}/gems/rake-0.9.2.2/test/file_creation.rb
%{gemdir}/gems/rake-0.9.2.2/test/helper.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_application.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_application_options.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_clean.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_definitions.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_directory_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_dsl.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_early_time.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_extension.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_file_creation_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_file_list.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_file_list_path_map.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_file_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_file_utils.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_ftp_file.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_functional.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_invocation_chain.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_makefile_loader.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_multi_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_name_space.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_package_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_path_map.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_path_map_explode.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_path_map_partial.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_pseudo_status.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_rake_test_loader.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_rdoc_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_require.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_rules.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_task_argument_parsing.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_task_arguments.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_task_lib.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_task_manager.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_task_manager_argument_resolution.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_task_with_arguments.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_test_task.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_top_level_functions.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_rake_win32.rb
%{gemdir}/gems/rake-0.9.2.2/test/test_sys.rb
%doc %{gemdir}/gems/rake-0.9.2.2/doc/command_line_usage.rdoc
%{gemdir}/gems/rake-0.9.2.2/doc/example/a.c
%{gemdir}/gems/rake-0.9.2.2/doc/example/b.c
%{gemdir}/gems/rake-0.9.2.2/doc/example/main.c
%{gemdir}/gems/rake-0.9.2.2/doc/example/Rakefile1
%{gemdir}/gems/rake-0.9.2.2/doc/example/Rakefile2
%doc %{gemdir}/gems/rake-0.9.2.2/doc/glossary.rdoc
%{gemdir}/gems/rake-0.9.2.2/doc/jamis.rb
%doc %{gemdir}/gems/rake-0.9.2.2/doc/proto_rake.rdoc
%{gemdir}/gems/rake-0.9.2.2/doc/rake.1.gz
%doc %{gemdir}/gems/rake-0.9.2.2/doc/rakefile.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/rational.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.4.14.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.4.15.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.5.0.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.5.3.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.5.4.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.6.0.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.7.0.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.7.1.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.7.2.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.7.3.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.8.0.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.8.2.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.8.3.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.8.4.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.8.5.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.8.6.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.8.7.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.9.0.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.9.1.rdoc
%doc %{gemdir}/gems/rake-0.9.2.2/doc/release_notes/rake-0.9.2.rdoc
%doc %{gemdir}/doc/rake-0.9.2.2
%{gemdir}/cache/rake-0.9.2.2.gem
%{gemdir}/specifications/rake-0.9.2.2.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.9.2.2-2
- Cleaned up spec file
