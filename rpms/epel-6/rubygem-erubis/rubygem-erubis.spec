%define rbname erubis
%define version 2.6.6
%define release 1

Summary: a fast and extensible eRuby implementation which supports multi-language
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.kuwata-lab.com/erubis/
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-abstract >= 1.0.0
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(erubis) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Erubis is an implementation of eRuby and has the following features:
* Very fast, almost three times faster than ERB and about 10% faster than
eruby.
* Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript)
* Auto escaping support
* Auto trimming spaces around '<% %>'
* Embedded pattern changeable (default '<% %>')
* Enable to handle Processing Instructions (PI) as embedded pattern (ex. '<?rb
... ?>')
* Context object available and easy to combine eRuby template with YAML
datafile
* Print statement available
* Easy to extend and customize in subclass
* Ruby on Rails support


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
%{_bindir}/erubis
%{gemdir}/gems/erubis-2.6.6/lib/erubis/context.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/converter.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/ec.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/ejava.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/ejavascript.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/enhanced.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/eperl.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/ephp.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/eruby.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/escheme.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine/optimized.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/engine.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/enhancer.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/error.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/evaluator.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/generator.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/helper.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/helpers/rails_form_helper.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/helpers/rails_helper.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/local-setting.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/main.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/preprocessing.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis/tiny.rb
%{gemdir}/gems/erubis-2.6.6/lib/erubis.rb
%{gemdir}/gems/erubis-2.6.6/bin/erubis
%{gemdir}/gems/erubis-2.6.6/examples/basic/example.ec
%{gemdir}/gems/erubis-2.6.6/examples/basic/example.ejava
%{gemdir}/gems/erubis-2.6.6/examples/basic/example.ejs
%{gemdir}/gems/erubis-2.6.6/examples/basic/example.eperl
%{gemdir}/gems/erubis-2.6.6/examples/basic/example.ephp
%{gemdir}/gems/erubis-2.6.6/examples/basic/example.eruby
%{gemdir}/gems/erubis-2.6.6/examples/basic/example.escheme
%{gemdir}/gems/erubis-2.6.6/examples/basic/Makefile
%{gemdir}/gems/erubis-2.6.6/examples/pi/example.ec
%{gemdir}/gems/erubis-2.6.6/examples/pi/example.ejava
%{gemdir}/gems/erubis-2.6.6/examples/pi/example.ejs
%{gemdir}/gems/erubis-2.6.6/examples/pi/example.eperl
%{gemdir}/gems/erubis-2.6.6/examples/pi/example.ephp
%{gemdir}/gems/erubis-2.6.6/examples/pi/example.eruby
%{gemdir}/gems/erubis-2.6.6/examples/pi/example.escheme
%{gemdir}/gems/erubis-2.6.6/examples/pi/Makefile
%{gemdir}/gems/erubis-2.6.6/test/assert-text-equal.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/array_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/arraybuffer_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/bipattern-example.rhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/bipattern_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/context.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/context.yaml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/def_method.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/def_method.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/escape_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example.ec
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/Example.ejava
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example.ejs
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example.eperl
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example.ephp
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example.escheme
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example1.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example1.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example1.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example10.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example10.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example10.xhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example10_x.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example11.php
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example11.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example11.rhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example11_C.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example11_N.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example11_php.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example11_U.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example1_x.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example2.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example2.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example2.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example2_trim.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example2_x.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example3.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example3.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example31.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example32.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example3_e.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example4.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example4.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example4.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example4_x.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example5.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example5.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example5.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example6.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example6.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example7.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example71.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example72.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example8.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example8_ruby.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example8_yaml.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example9.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example9.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example9.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example91.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example92.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example_c.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example_java.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example_js.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example_perl.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example_php.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example_scheme.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/example_scheme_display.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/fasteruby.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/fasteruby.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/fasteruby.rhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/headerfooter-example.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/headerfooter-example2.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/headerfooter-example2.rhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/headerfooter_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/headerfooter_example2.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/interpolation_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/main_program1.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/main_program1.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/main_program2.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/main_program2.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/nocode-example.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/nocode-php.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/nocode_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/normal-eruby-test.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/normal_eruby_test.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/notext-example.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/notext-example.php
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/notext-php.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/notext_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/percentline-example.rhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/percentline_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/printenable_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/printenabled-example.eruby
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/printenabled-example.rb
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/printstatement_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/simplify_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/stderr.log
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/stdout_exmple.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/stringbuffer_example.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/tail_260.result
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/tailnewline.rhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/template1.rhtml
%{gemdir}/gems/erubis-2.6.6/test/data/users-guide/template2.rhtml
%{gemdir}/gems/erubis-2.6.6/test/test-engines.rb
%{gemdir}/gems/erubis-2.6.6/test/test-enhancers.rb
%{gemdir}/gems/erubis-2.6.6/test/test-erubis.rb
%{gemdir}/gems/erubis-2.6.6/test/test-main.rb
%{gemdir}/gems/erubis-2.6.6/test/test-users-guide.rb
%{gemdir}/gems/erubis-2.6.6/test/test.rb
%{gemdir}/gems/erubis-2.6.6/test/testutil.rb
%{gemdir}/gems/erubis-2.6.6/doc/docstyle.css
%{gemdir}/gems/erubis-2.6.6/doc/users-guide.html
%{gemdir}/gems/erubis-2.6.6/README.txt
%{gemdir}/gems/erubis-2.6.6/CHANGES.txt
%{gemdir}/gems/erubis-2.6.6/MIT-LICENSE
%{gemdir}/gems/erubis-2.6.6/setup.rb
%{gemdir}/gems/erubis-2.6.6/contrib/erubis
%{gemdir}/gems/erubis-2.6.6/contrib/erubis-run.rb
%{gemdir}/gems/erubis-2.6.6/contrib/inline-require
%{gemdir}/gems/erubis-2.6.6/benchmark/bench.rb
%{gemdir}/gems/erubis-2.6.6/benchmark/bench_context.yaml
%{gemdir}/gems/erubis-2.6.6/benchmark/Makefile
%{gemdir}/gems/erubis-2.6.6/benchmark/templates/_footer.html
%{gemdir}/gems/erubis-2.6.6/benchmark/templates/_header.html
%{gemdir}/gems/erubis-2.6.6/benchmark/templates/bench_erb.rhtml
%{gemdir}/gems/erubis-2.6.6/benchmark/templates/bench_erubis.rhtml
%{gemdir}/gems/erubis-2.6.6/benchmark/templates/bench_eruby.rhtml
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/ActionView/TemplateHandlers/ErubisHandler.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/ActionView.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/ERB.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/ArrayBufferEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/ArrayBufferEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/ArrayEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/ArrayEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Basic/Converter.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Basic/Engine.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Basic.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/BiPatternEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/BiPatternEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/CGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/CommandOptionError.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Context.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Converter.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/DeleteIndentEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/DeleteIndentEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Ec.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Ejava.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Ejavascript.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Engine.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Eperl.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Ephp.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/ErboutEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/ErboutEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/ErubisError.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Eruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapedEc.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapedEjava.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapedEjavascript.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapedEperl.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapedEphp.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapedEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapedEscheme.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/EscapeEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Escheme.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Evaluator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/FastEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Generator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/HeaderFooterEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/HeaderFooterEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Helpers/RailsFormHelper.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Helpers/RailsHelper/TemplateConverter.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Helpers/RailsHelper.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Helpers.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/InterpolationEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/InterpolationEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/JavaGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/JavascriptGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/Main.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/NoCodeEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/NoCodeEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/NoTextEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/NoTextEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/NotSupportedError.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/OptimizedEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/OptimizedGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/OptimizedXmlEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PercentLineEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PercentLineEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PerlGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PhpGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Converter.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Ec.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Ejava.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Ejavascript.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Engine.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Eperl.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Ephp.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Eruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/Escheme.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI/TinyEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PI.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PreprocessingEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PreprocessingHelper.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PrintEnabledEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PrintEnabledEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PrintOutEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PrintOutEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/PrintOutSimplifiedEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/RubyEvaluator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/RubyGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/SchemeGenerator.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/SimplifiedEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/SimplifyEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/StdoutEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/StdoutEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/StdoutSimplifiedEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/StringBufferEnhancer.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/StringBufferEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/StringIOEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/TinyEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/XmlEruby.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis/XmlHelper.html
%{gemdir}/gems/erubis-2.6.6/doc-api/classes/Erubis.html
%{gemdir}/gems/erubis-2.6.6/doc-api/created.rid
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/context_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/converter_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/ec_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/ejava_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/ejavascript_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/enhanced_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/eperl_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/ephp_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/eruby_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/escheme_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine/optimized_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/engine_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/enhancer_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/error_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/evaluator_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/generator_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/helper_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/helpers/rails_form_helper_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/helpers/rails_helper_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/local-setting_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/main_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/preprocessing_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis/tiny_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/erubis_rb.html
%{gemdir}/gems/erubis-2.6.6/doc-api/files/README_txt.html
%{gemdir}/gems/erubis-2.6.6/doc-api/fr_class_index.html
%{gemdir}/gems/erubis-2.6.6/doc-api/fr_file_index.html
%{gemdir}/gems/erubis-2.6.6/doc-api/fr_method_index.html
%{gemdir}/gems/erubis-2.6.6/doc-api/index.html
%{gemdir}/gems/erubis-2.6.6/doc-api/rdoc-style.css


%doc %{gemdir}/doc/erubis-2.6.6
%{gemdir}/cache/erubis-2.6.6.gem
%{gemdir}/specifications/erubis-2.6.6.gemspec

%changelog
