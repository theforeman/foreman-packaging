%define rbname activesupport
%define version 3.2.13
%define release 1

Summary: A toolkit of support libraries and Ruby core extensions extracted from the Rails framework.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
Requires: rubygem-i18n = 0.6.1
Requires: rubygem-multi_json => 1.0
Requires: rubygem-multi_json < 2

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildRequires: rubygem-rdoc

BuildArch: noarch

Provides: rubygem(activesupport) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.


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
%{gemdir}/gems/activesupport-%{version}/CHANGELOG.md
%{gemdir}/gems/activesupport-%{version}/MIT-LICENSE
%{gemdir}/gems/activesupport-%{version}/README.rdoc
%{gemdir}/gems/activesupport-%{version}/lib/active_support/all.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/backtrace_cleaner.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/base64.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/basic_object.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/benchmarkable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/buffered_logger.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/builder.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/cache/file_store.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/cache/mem_cache_store.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/cache/memory_store.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/cache/null_store.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/cache/strategy/local_cache.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/cache.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/callbacks.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/concern.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/configurable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/access.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/extract_options.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/grouping.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/prepend_and_append.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/random_access.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/uniq_by.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array/wrap.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/array.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/benchmark.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/big_decimal/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/big_decimal.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/class/attribute.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/class/attribute_accessors.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/class/delegating_attributes.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/class/subclasses.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/class.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date/acts_like.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date/calculations.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date/freeze.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date/zones.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date_time/acts_like.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date_time/calculations.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date_time/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/date_time/zones.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/enumerable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/exception.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/file/atomic.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/file/path.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/file.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/float/rounding.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/float.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/deep_dup.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/deep_merge.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/diff.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/except.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/indifferent_access.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/keys.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/reverse_merge.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash/slice.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/hash.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/integer/inflections.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/integer/multiple.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/integer/time.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/integer.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/io.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/kernel/agnostics.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/kernel/debugger.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/kernel/reporting.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/kernel/singleton_class.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/kernel.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/load_error.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/logger.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/aliasing.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/anonymous.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/attr_internal.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/attribute_accessors.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/delegation.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/deprecation.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/introspection.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/method_names.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/qualified_const.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/reachable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/remove_method.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module/synchronization.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/module.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/name_error.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/numeric/bytes.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/numeric/time.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/numeric.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/acts_like.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/blank.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/duplicable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/inclusion.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/instance_variables.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/to_json.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/to_param.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/to_query.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/try.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object/with_options.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/object.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/proc.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/process/daemon.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/process.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/range/blockless_step.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/range/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/range/cover.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/range/include_range.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/range/overlaps.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/range.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/regexp.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/rexml.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/access.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/behavior.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/encoding.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/exclude.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/filters.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/inflections.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/inquiry.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/interpolation.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/multibyte.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/output_safety.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/starts_ends_with.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/strip.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string/xchar.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/string.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/time/acts_like.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/time/calculations.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/time/conversions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/time/marshal.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/time/publicize_conversion_methods.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/time/zones.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext/uri.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/core_ext.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/dependencies/autoload.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/dependencies.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/deprecation/behaviors.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/deprecation/method_wrappers.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/deprecation/proxy_wrappers.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/deprecation/reporting.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/deprecation.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/descendants_tracker.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/duration.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/file_update_checker.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/file_watcher.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/gzip.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/hash_with_indifferent_access.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/i18n.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/i18n_railtie.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/inflections.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/inflector/inflections.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/inflector/methods.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/inflector/transliterate.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/inflector.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/json/decoding.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/json/encoding.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/json/variable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/json.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/lazy_load_hooks.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/locale/en.yml
%{gemdir}/gems/activesupport-%{version}/lib/active_support/log_subscriber/test_helper.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/log_subscriber.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/memoizable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/message_encryptor.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/message_verifier.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/multibyte/chars.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/multibyte/exceptions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/multibyte/unicode.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/multibyte/utils.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/multibyte.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/notifications/fanout.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/notifications/instrumenter.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/notifications.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/option_merger.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/ordered_hash.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/ordered_options.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/railtie.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/rescuable.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/ruby/shim.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/string_inquirer.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/tagged_logging.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/test_case.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/assertions.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/declarative.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/deprecation.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/isolation.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/mochaing.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/pending.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/performance/jruby.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/performance/rubinius.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/performance/ruby/mri.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/performance/ruby/yarv.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/performance/ruby.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/performance.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/testing/setup_and_teardown.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/time/autoload.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/time.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/time_with_zone.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/values/time_zone.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/values/unicode_tables.dat
%{gemdir}/gems/activesupport-%{version}/lib/active_support/version.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/whiny_nil.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/xml_mini/jdom.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/xml_mini/libxml.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/xml_mini/libxmlsax.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/xml_mini/nokogiri.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/xml_mini/nokogirisax.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/xml_mini/rexml.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support/xml_mini.rb
%{gemdir}/gems/activesupport-%{version}/lib/active_support.rb


%doc %{gemdir}/doc/activesupport-%{version}
%{gemdir}/cache/activesupport-%{version}.gem
%{gemdir}/specifications/activesupport-%{version}.gemspec

%changelog
* Fri Apr 12 2013 shk@redhat.com 3.2.13-1
- Updated to 3.2.13
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
