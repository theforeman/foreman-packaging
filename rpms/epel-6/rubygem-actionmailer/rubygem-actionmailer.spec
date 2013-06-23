%define rbname actionmailer
%define version 3.2.13
%define release 1

Summary: Email composition, delivery, and receiving framework (part of Rails).
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
Requires: rubygem-actionpack = %{version}
Requires: rubygem-mail => 2.5.3
Requires: rubygem-mail < 2.6

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10

BuildArch: noarch

Provides: rubygem(actionmailer) = %{version}

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/actionmailer-%{version}/CHANGELOG.md
%{gemdir}/gems/actionmailer-%{version}/README.rdoc
%{gemdir}/gems/actionmailer-%{version}/MIT-LICENSE
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/base.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/collector.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/delivery_methods.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/log_subscriber.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/mail_helper.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/railtie.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/test_case.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/test_helper.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer/version.rb
%{gemdir}/gems/actionmailer-%{version}/lib/action_mailer.rb
%{gemdir}/gems/actionmailer-%{version}/lib/rails/generators/mailer/mailer_generator.rb
%{gemdir}/gems/actionmailer-%{version}/lib/rails/generators/mailer/templates/mailer.rb
%{gemdir}/gems/actionmailer-%{version}/lib/rails/generators/mailer/USAGE


%doc %{gemdir}/doc/actionmailer-%{version}
%{gemdir}/cache/actionmailer-%{version}.gem
%{gemdir}/specifications/actionmailer-%{version}.gemspec

%changelog
* Fri Apr 12 2013 shk@redhat.com 3.2.13-1
- Updated to 3.2.13
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
