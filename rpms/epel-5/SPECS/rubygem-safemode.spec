%define rbname safemode
%define version 1.2.0
%define release 1

Summary: A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/svenfuchs/safemode
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby
Requires: rubygems >= 1.8.10

Requires: rubygem-ruby2ruby >= 2.0.1
Requires: rubygem-sexp_processor >= 4.1.2

Requires: rubygem-ruby_parser 
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(safemode) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A library for safe evaluation of Ruby code based on RubyParser and Ruby2Ruby.
Provides Rails ActionView template handlers for ERB and Haml.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/safemode-%{version}/Gemfile
%{gemdir}/gems/safemode-%{version}/Gemfile.lock
%{gemdir}/gems/safemode-%{version}/LICENCSE
%doc %{gemdir}/gems/safemode-%{version}/README.markdown
%{gemdir}/gems/safemode-%{version}/Rakefile
%{gemdir}/gems/safemode-%{version}/VERSION
%{gemdir}/gems/safemode-%{version}/demo.rb
%{gemdir}/gems/safemode-%{version}/init.rb
%{gemdir}/gems/safemode-%{version}/lib/action_view/template_handlers/safe_erb.rb
%{gemdir}/gems/safemode-%{version}/lib/action_view/template_handlers/safe_haml.rb
%{gemdir}/gems/safemode-%{version}/lib/action_view/template_handlers/safemode_handler.rb
%{gemdir}/gems/safemode-%{version}/lib/haml/safemode.rb
%{gemdir}/gems/safemode-%{version}/lib/ruby_parser_string_io_patch.diff
%{gemdir}/gems/safemode-%{version}/lib/rubyparser_bug.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode/blankslate.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode/core_ext.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode/core_jails.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode/exceptions.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode/jail.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode/parser.rb
%{gemdir}/gems/safemode-%{version}/lib/safemode/scope.rb
%{gemdir}/gems/safemode-%{version}/safemode.gemspec
%{gemdir}/gems/safemode-%{version}/test/test_all.rb
%{gemdir}/gems/safemode-%{version}/test/test_erb_eval.rb
%{gemdir}/gems/safemode-%{version}/test/test_helper.rb
%{gemdir}/gems/safemode-%{version}/test/test_jail.rb
%{gemdir}/gems/safemode-%{version}/test/test_safemode_eval.rb
%{gemdir}/gems/safemode-%{version}/test/test_safemode_parser.rb


%doc %{gemdir}/doc/safemode-%{version}
%{gemdir}/cache/safemode-%{version}.gem
%{gemdir}/specifications/safemode-%{version}.gemspec

%changelog
