%define rbname activemodel
%define version 3.0.15
%define release 1

Summary: A toolkit for building modeling frameworks (part of Rails).
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10

Requires: rubygem-activesupport = 3.0.15

Requires: rubygem-builder => 2.1.2
Requires: rubygem-builder < 2.2

Requires: rubygem-i18n => 0.5.0
Requires: rubygem-i18n < 0.6
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(activemodel) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A toolkit for building modeling frameworks like Active Record and Active
Resource. Rich support for attributes, callbacks, validations, observers,
serialization, internationalization, and testing.


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
%{gemdir}/gems/activemodel-3.0.15/CHANGELOG
%{gemdir}/gems/activemodel-3.0.15/MIT-LICENSE
%{gemdir}/gems/activemodel-3.0.15/README.rdoc
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/attribute_methods.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/callbacks.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/conversion.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/deprecated_error_methods.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/dirty.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/errors.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/lint.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/locale/en.yml
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/mass_assignment_security/permission_set.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/mass_assignment_security/sanitizer.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/mass_assignment_security.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/naming.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/observing.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/railtie.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/serialization.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/serializers/json.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/serializers/xml.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/test_case.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/translation.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/acceptance.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/callbacks.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/confirmation.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/exclusion.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/format.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/inclusion.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/length.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/numericality.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/presence.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/validates.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations/with.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validations.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/validator.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model/version.rb
%{gemdir}/gems/activemodel-3.0.15/lib/active_model.rb


%doc %{gemdir}/doc/activemodel-3.0.15
%{gemdir}/cache/activemodel-3.0.15.gem
%{gemdir}/specifications/activemodel-3.0.15.gemspec

%changelog
