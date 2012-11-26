%define rbname safemode
%define version 1.0.1
%define release 1

Summary: A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/svenfuchs/safemode
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-ruby2ruby 

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
%{gemdir}/gems/safemode-1.0.1/Gemfile
%{gemdir}/gems/safemode-1.0.1/Gemfile.lock
%{gemdir}/gems/safemode-1.0.1/LICENCSE
%doc %{gemdir}/gems/safemode-1.0.1/README.markdown
%{gemdir}/gems/safemode-1.0.1/Rakefile
%{gemdir}/gems/safemode-1.0.1/VERSION
%{gemdir}/gems/safemode-1.0.1/demo.rb
%{gemdir}/gems/safemode-1.0.1/init.rb
%{gemdir}/gems/safemode-1.0.1/lib/action_view/template_handlers/safe_erb.rb
%{gemdir}/gems/safemode-1.0.1/lib/action_view/template_handlers/safe_haml.rb
%{gemdir}/gems/safemode-1.0.1/lib/action_view/template_handlers/safemode_handler.rb
%{gemdir}/gems/safemode-1.0.1/lib/haml/safemode.rb
%{gemdir}/gems/safemode-1.0.1/lib/ruby_parser_string_io_patch.diff
%{gemdir}/gems/safemode-1.0.1/lib/rubyparser_bug.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode/blankslate.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode/core_ext.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode/core_jails.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode/exceptions.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode/jail.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode/parser.rb
%{gemdir}/gems/safemode-1.0.1/lib/safemode/scope.rb
%{gemdir}/gems/safemode-1.0.1/safemode.gemspec
%{gemdir}/gems/safemode-1.0.1/test/test_all.rb
%{gemdir}/gems/safemode-1.0.1/test/test_erb_eval.rb
%{gemdir}/gems/safemode-1.0.1/test/test_helper.rb
%{gemdir}/gems/safemode-1.0.1/test/test_jail.rb
%{gemdir}/gems/safemode-1.0.1/test/test_safemode_eval.rb
%{gemdir}/gems/safemode-1.0.1/test/test_safemode_parser.rb


%doc %{gemdir}/doc/safemode-1.0.1
%{gemdir}/cache/safemode-1.0.1.gem
%{gemdir}/specifications/safemode-1.0.1.gemspec

%changelog
