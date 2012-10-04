%define rbname actionmailer
%define version 3.0.17
%define release 1

Summary: Email composition, delivery, and receiving framework (part of Rails).
Name: rubygem-%{rbname}
Epoch: 1
Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: %{rbname}-%{version}.gem
Patch0: ./0001-rubygem-actionmailer-fix-dep-versions.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10

Requires: rubygem-actionpack = 3.0.17

Requires: rubygem-mail => 2.2.19
Requires: rubygem-mail > 2.3
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(actionmailer) = %{version}
Provides: rubygem-actionmailer = %{version}
%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Email on Rails. Compose, deliver, receive, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
cd %{gembuilddir}
cp %{PATCH0} ./
patch -p0 < ./0001-rubygem-actionmailer-fix-dep-versions.patch
rm ./0001-rubygem-actionmailer-fix-dep-versions.patch

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/actionmailer-3.0.17/CHANGELOG
%{gemdir}/gems/actionmailer-3.0.17/README.rdoc
%{gemdir}/gems/actionmailer-3.0.17/MIT-LICENSE
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/adv_attr_accessor.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/base.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/collector.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/delivery_methods.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/deprecated_api.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/log_subscriber.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/mail_helper.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/old_api.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/railtie.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/test_case.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/test_helper.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/tmail_compat.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer/version.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/action_mailer.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/rails/generators/mailer/mailer_generator.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/rails/generators/mailer/templates/mailer.rb
%{gemdir}/gems/actionmailer-3.0.17/lib/rails/generators/mailer/USAGE


%doc %{gemdir}/doc/actionmailer-3.0.17
%{gemdir}/cache/actionmailer-3.0.17.gem
%{gemdir}/specifications/actionmailer-3.0.17.gemspec

%changelog
