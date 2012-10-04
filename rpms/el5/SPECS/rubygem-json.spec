%define rbname json
%define version 1.6.6
%define release 2

Summary: JSON Implementation for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://flori.github.com/json
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildRequires: gcc
Provides: rubygem(json) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This is a JSON implementation as a Ruby extension in C.


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
%{gemdir}/gems/json-1.6.6/.gitignore
%{gemdir}/gems/json-1.6.6/.travis.yml
%{gemdir}/gems/json-1.6.6/CHANGES
%{gemdir}/gems/json-1.6.6/COPYING
%{gemdir}/gems/json-1.6.6/COPYING-json-jruby
%{gemdir}/gems/json-1.6.6/GPL
%{gemdir}/gems/json-1.6.6/Gemfile
%{gemdir}/gems/json-1.6.6/README-json-jruby.markdown
%doc %{gemdir}/gems/json-1.6.6/README.rdoc
%{gemdir}/gems/json-1.6.6/Rakefile
%{gemdir}/gems/json-1.6.6/TODO
%{gemdir}/gems/json-1.6.6/VERSION
%{gemdir}/gems/json-1.6.6/data/example.json
%{gemdir}/gems/json-1.6.6/data/index.html
%{gemdir}/gems/json-1.6.6/data/prototype.js
%{gemdir}/gems/json-1.6.6/diagrams/.keep
%{gemdir}/gems/json-1.6.6/ext/json/ext/fbuffer/fbuffer.h
%{gemdir}/gems/json-1.6.6/ext/json/ext/generator/extconf.rb
%{gemdir}/gems/json-1.6.6/ext/json/ext/generator/generator.c
%{gemdir}/gems/json-1.6.6/ext/json/ext/generator/generator.h
%{gemdir}/gems/json-1.6.6/ext/json/ext/parser/extconf.rb
%{gemdir}/gems/json-1.6.6/ext/json/ext/parser/parser.c
%{gemdir}/gems/json-1.6.6/ext/json/ext/parser/parser.h
%{gemdir}/gems/json-1.6.6/ext/json/ext/parser/parser.rl
%{gemdir}/gems/json-1.6.6/install.rb
%{gemdir}/gems/json-1.6.6/java/src/json/ext/ByteListTranscoder.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/Generator.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/GeneratorMethods.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/GeneratorService.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/GeneratorState.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/OptionsReader.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/Parser.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/Parser.rl
%{gemdir}/gems/json-1.6.6/java/src/json/ext/ParserService.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/RuntimeInfo.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/StringDecoder.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/StringEncoder.java
%{gemdir}/gems/json-1.6.6/java/src/json/ext/Utils.java
%{gemdir}/gems/json-1.6.6/json-java.gemspec
%{gemdir}/gems/json-1.6.6/json.gemspec
%{gemdir}/gems/json-1.6.6/json_pure.gemspec
%{gemdir}/gems/json-1.6.6/lib/json.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/bigdecimal.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/complex.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/core.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/date.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/date_time.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/exception.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/ostruct.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/range.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/rational.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/regexp.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/struct.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/symbol.rb
%{gemdir}/gems/json-1.6.6/lib/json/add/time.rb
%{gemdir}/gems/json-1.6.6/lib/json/common.rb
%{gemdir}/gems/json-1.6.6/lib/json/ext.rb
%{gemdir}/gems/json-1.6.6/lib/json/ext/.keep
%{gemdir}/gems/json-1.6.6/lib/json/pure.rb
%{gemdir}/gems/json-1.6.6/lib/json/pure/generator.rb
%{gemdir}/gems/json-1.6.6/lib/json/pure/parser.rb
%{gemdir}/gems/json-1.6.6/lib/json/version.rb
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail1.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail10.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail11.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail12.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail13.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail14.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail18.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail19.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail2.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail20.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail21.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail22.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail23.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail24.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail25.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail27.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail28.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail3.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail4.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail5.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail6.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail7.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail8.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/fail9.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/pass1.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/pass15.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/pass16.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/pass17.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/pass2.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/pass26.json
%{gemdir}/gems/json-1.6.6/tests/fixtures/pass3.json
%{gemdir}/gems/json-1.6.6/tests/setup_variant.rb
%{gemdir}/gems/json-1.6.6/tests/test_json.rb
%{gemdir}/gems/json-1.6.6/tests/test_json_addition.rb
%{gemdir}/gems/json-1.6.6/tests/test_json_encoding.rb
%{gemdir}/gems/json-1.6.6/tests/test_json_fixtures.rb
%{gemdir}/gems/json-1.6.6/tests/test_json_generate.rb
%{gemdir}/gems/json-1.6.6/tests/test_json_string_matching.rb
%{gemdir}/gems/json-1.6.6/tests/test_json_unicode.rb
%{gemdir}/gems/json-1.6.6/tools/fuzz.rb
%{gemdir}/gems/json-1.6.6/tools/server.rb
%{gemdir}/gems/json-1.6.6/ext/json/ext/generator/Makefile
%{gemdir}/gems/json-1.6.6/ext/json/ext/generator/generator.o
%{gemdir}/gems/json-1.6.6/ext/json/ext/generator/generator.so
%{gemdir}/gems/json-1.6.6/ext/json/ext/json/ext/generator.so
%{gemdir}/gems/json-1.6.6/ext/json/ext/json/ext/parser.so
%{gemdir}/gems/json-1.6.6/ext/json/ext/parser/Makefile
%{gemdir}/gems/json-1.6.6/ext/json/ext/parser/parser.o
%{gemdir}/gems/json-1.6.6/ext/json/ext/parser/parser.so

%doc %{gemdir}/doc/json-1.6.6
%{gemdir}/cache/json-1.6.6.gem
%{gemdir}/specifications/json-1.6.6.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 1.6.6-2
- Cleaned up spec file
