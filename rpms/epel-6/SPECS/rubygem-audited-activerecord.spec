%define rbname audited-activerecord
%define version 3.0.0.rc1
%define release 1

Summary: Log all changes to your ActiveRecord models
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/collectiveidea/audited
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-audited = 3.0.0.rc1

Requires: rubygem-activerecord => 3.0
Requires: rubygem-activerecord < 4
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(audited-activerecord) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Log all changes to your ActiveRecord models


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
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/audited-activerecord.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/audited/adapters/active_record.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/audited/adapters/active_record/audit.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/install_generator.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/templates/add_association_to_audits.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/templates/add_comment_to_audits.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/templates/add_remote_address_to_audits.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/templates/install.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/templates/rename_association_to_associated.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/templates/rename_changes_to_audited_changes.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/templates/rename_parent_to_association.rb
%{gemdir}/gems/audited-activerecord-3.0.0.rc1/lib/generators/audited/upgrade_generator.rb


%doc %{gemdir}/doc/audited-activerecord-3.0.0.rc1
%{gemdir}/cache/audited-activerecord-3.0.0.rc1.gem
%{gemdir}/specifications/audited-activerecord-3.0.0.rc1.gemspec

%changelog
