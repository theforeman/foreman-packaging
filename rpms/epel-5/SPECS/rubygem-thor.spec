%define rbname thor
%define version 0.14.6
%define release 2

Summary: A scripting framework that replaces rake, sake and rubigen
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/wycats/thor
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(thor) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A scripting framework that replaces rake, sake and rubigen


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
%{_bindir}/rake2thor
%{_bindir}/thor
%{gemdir}/gems/thor-0.14.6/bin/rake2thor
%{gemdir}/gems/thor-0.14.6/bin/thor
%{gemdir}/gems/thor-0.14.6/lib/thor.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/actions.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/actions/create_file.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/actions/create_link.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/actions/directory.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/actions/empty_directory.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/actions/file_manipulation.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/actions/inject_into_file.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/base.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/core_ext/file_binary_read.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/core_ext/hash_with_indifferent_access.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/core_ext/ordered_hash.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/error.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/group.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/invocation.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/parser.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/parser/argument.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/parser/arguments.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/parser/option.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/parser/options.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/rake_compat.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/runner.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/shell.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/shell/basic.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/shell/color.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/shell/html.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/task.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/util.rb
%{gemdir}/gems/thor-0.14.6/lib/thor/version.rb
%{gemdir}/gems/thor-0.14.6/spec/actions/create_file_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/actions/directory_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/actions/empty_directory_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/actions/file_manipulation_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/actions/inject_into_file_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/actions_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/base_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/core_ext/hash_with_indifferent_access_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/core_ext/ordered_hash_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/fixtures/application.rb
%{gemdir}/gems/thor-0.14.6/spec/fixtures/bundle/execute.rb
%{gemdir}/gems/thor-0.14.6/spec/fixtures/bundle/main.thor
%{gemdir}/gems/thor-0.14.6/spec/fixtures/doc/%file_name%.rb.tt
%{gemdir}/gems/thor-0.14.6/spec/fixtures/doc/README
%{gemdir}/gems/thor-0.14.6/spec/fixtures/doc/block_helper.rb
%{gemdir}/gems/thor-0.14.6/spec/fixtures/doc/components/.empty_directory
%{gemdir}/gems/thor-0.14.6/spec/fixtures/doc/config.rb
%{gemdir}/gems/thor-0.14.6/spec/fixtures/group.thor
%{gemdir}/gems/thor-0.14.6/spec/fixtures/invoke.thor
%{gemdir}/gems/thor-0.14.6/spec/fixtures/script.thor
%{gemdir}/gems/thor-0.14.6/spec/fixtures/task.thor
%{gemdir}/gems/thor-0.14.6/spec/group_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/invocation_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/parser/argument_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/parser/arguments_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/parser/option_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/parser/options_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/rake_compat_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/register_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/runner_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/shell/basic_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/shell/color_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/shell/html_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/shell_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/spec_helper.rb
%{gemdir}/gems/thor-0.14.6/spec/task_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/thor_spec.rb
%{gemdir}/gems/thor-0.14.6/spec/util_spec.rb
%doc %{gemdir}/gems/thor-0.14.6/CHANGELOG.rdoc
%doc %{gemdir}/gems/thor-0.14.6/LICENSE
%doc %{gemdir}/gems/thor-0.14.6/README.md
%doc %{gemdir}/gems/thor-0.14.6/Thorfile
"%{gemdir}/gems/thor-0.14.6/spec/fixtures/path with spaces"
%doc %{gemdir}/doc/thor-0.14.6
%{gemdir}/cache/thor-0.14.6.gem
%{gemdir}/specifications/thor-0.14.6.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.14.6-2
- Cleaned up spec file

