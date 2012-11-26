%define rbname awesome_print
%define version 1.0.2
%define release 1

Summary: Pretty print Ruby objects with proper indentation and colors
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/michaeldv/awesome_print
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(awesome_print) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Great Ruby dubugging companion: pretty print Ruby objects to visualize their
structure. Supports custom object formatting via plugins


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
%{gemdir}/gems/awesome_print-1.0.2/CHANGELOG
%{gemdir}/gems/awesome_print-1.0.2/Gemfile
%{gemdir}/gems/awesome_print-1.0.2/Gemfile.lock
%{gemdir}/gems/awesome_print-1.0.2/LICENSE
%{gemdir}/gems/awesome_print-1.0.2/Rakefile
%{gemdir}/gems/awesome_print-1.0.2/README.md
%{gemdir}/gems/awesome_print-1.0.2/lib/ap.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/core_ext/array.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/core_ext/class.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/core_ext/kernel.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/core_ext/logger.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/core_ext/method.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/core_ext/object.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/core_ext/string.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/ext/action_view.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/ext/active_record.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/ext/active_support.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/ext/mongo_mapper.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/ext/mongoid.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/ext/nokogiri.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/formatter.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/inspector.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print/version.rb
%{gemdir}/gems/awesome_print-1.0.2/lib/awesome_print.rb
%{gemdir}/gems/awesome_print-1.0.2/spec/colors_spec.rb
%{gemdir}/gems/awesome_print-1.0.2/spec/formats_spec.rb
%{gemdir}/gems/awesome_print-1.0.2/spec/methods_spec.rb
%{gemdir}/gems/awesome_print-1.0.2/spec/objects_spec.rb
%{gemdir}/gems/awesome_print-1.0.2/spec/spec_helper.rb
%{gemdir}/gems/awesome_print-1.0.2/.gitignore


%doc %{gemdir}/doc/awesome_print-1.0.2
%{gemdir}/cache/awesome_print-1.0.2.gem
%{gemdir}/specifications/awesome_print-1.0.2.gemspec

%changelog
