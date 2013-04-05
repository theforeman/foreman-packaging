%define rbname i18n
%define version 0.5.0
%define release 1

Summary: New wave Internationalization support for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/svenfuchs/i18n
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(i18n) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
New wave Internationalization support for Ruby.


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
%{gemdir}/gems/i18n-0.5.0/ci/Gemfile.no-rails
%{gemdir}/gems/i18n-0.5.0/ci/Gemfile.no-rails.lock
%{gemdir}/gems/i18n-0.5.0/ci/Gemfile.rails-2.3.x
%{gemdir}/gems/i18n-0.5.0/ci/Gemfile.rails-2.3.x.lock
%{gemdir}/gems/i18n-0.5.0/ci/Gemfile.rails-3.x
%{gemdir}/gems/i18n-0.5.0/ci/Gemfile.rails-3.x.lock
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/base.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/cache.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/cascade.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/chain.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/fallbacks.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/flatten.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/gettext.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/interpolation_compiler.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/key_value.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/memoize.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/metadata.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/pluralization.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/simple.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend/transliterator.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/backend.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/config.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/core_ext/hash.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/core_ext/kernel/surpress_warnings.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/core_ext/string/interpolate.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/exceptions.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/gettext/helpers.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/gettext/po_parser.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/gettext.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/interpolate/ruby.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/locale/fallbacks.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/locale/tag/parents.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/locale/tag/rfc4646.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/locale/tag/simple.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/locale/tag.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/locale.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/basics.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/defaults.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/interpolation.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/link.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/localization/date.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/localization/date_time.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/localization/procs.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/localization/time.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/localization.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/lookup.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/pluralization.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests/procs.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/tests.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n/version.rb
%{gemdir}/gems/i18n-0.5.0/lib/i18n.rb
%{gemdir}/gems/i18n-0.5.0/test/all.rb
%{gemdir}/gems/i18n-0.5.0/test/api/all_features_test.rb
%{gemdir}/gems/i18n-0.5.0/test/api/cascade_test.rb
%{gemdir}/gems/i18n-0.5.0/test/api/chain_test.rb
%{gemdir}/gems/i18n-0.5.0/test/api/fallbacks_test.rb
%{gemdir}/gems/i18n-0.5.0/test/api/key_value_test.rb
%{gemdir}/gems/i18n-0.5.0/test/api/memoize_test.rb
%{gemdir}/gems/i18n-0.5.0/test/api/pluralization_test.rb
%{gemdir}/gems/i18n-0.5.0/test/api/simple_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/cache_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/cascade_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/chain_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/exceptions_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/fallbacks_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/interpolation_compiler_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/key_value_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/memoize_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/metadata_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/pluralization_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/simple_test.rb
%{gemdir}/gems/i18n-0.5.0/test/backend/transliterator_test.rb
%{gemdir}/gems/i18n-0.5.0/test/core_ext/hash_test.rb
%{gemdir}/gems/i18n-0.5.0/test/core_ext/string/interpolate_test.rb
%{gemdir}/gems/i18n-0.5.0/test/gettext/api_test.rb
%{gemdir}/gems/i18n-0.5.0/test/gettext/backend_test.rb
%{gemdir}/gems/i18n-0.5.0/test/i18n/exceptions_test.rb
%{gemdir}/gems/i18n-0.5.0/test/i18n/interpolate_test.rb
%{gemdir}/gems/i18n-0.5.0/test/i18n/load_path_test.rb
%{gemdir}/gems/i18n-0.5.0/test/i18n_test.rb
%{gemdir}/gems/i18n-0.5.0/test/locale/fallbacks_test.rb
%{gemdir}/gems/i18n-0.5.0/test/locale/tag/rfc4646_test.rb
%{gemdir}/gems/i18n-0.5.0/test/locale/tag/simple_test.rb
%{gemdir}/gems/i18n-0.5.0/test/run_all.rb
%{gemdir}/gems/i18n-0.5.0/test/test_data/locales/de.po
%{gemdir}/gems/i18n-0.5.0/test/test_data/locales/en.rb
%{gemdir}/gems/i18n-0.5.0/test/test_data/locales/en.yml
%{gemdir}/gems/i18n-0.5.0/test/test_data/locales/invalid/empty.yml
%{gemdir}/gems/i18n-0.5.0/test/test_data/locales/plurals.rb
%{gemdir}/gems/i18n-0.5.0/test/test_helper.rb
%{gemdir}/gems/i18n-0.5.0/README.textile
%{gemdir}/gems/i18n-0.5.0/MIT-LICENSE
%{gemdir}/gems/i18n-0.5.0/CHANGELOG.textile


%doc %{gemdir}/doc/i18n-0.5.0
%{gemdir}/cache/i18n-0.5.0.gem
%{gemdir}/specifications/i18n-0.5.0.gemspec

%changelog
