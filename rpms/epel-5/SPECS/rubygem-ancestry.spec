%define rbname ancestry
%define version 1.3.0
%define release 1

Summary: Ancestry allows the records of a ActiveRecord model to be organised in a tree structure, using a single, intuitively formatted database column. It exposes all the standard tree structure relations (ancestors, parent, root, children, siblings, descendants) and all of them can be fetched in a single sql query. Additional features are named_scopes, integrity checking, integrity restoration, arrangement of (sub)tree into hashes and different strategies for dealing with orphaned records.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/stefankroes/ancestry
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-activerecord >= 2.2.2
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(ancestry) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Organise ActiveRecord model into a tree structure


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
%{gemdir}/gems/ancestry-%{version}/ancestry.gemspec
%{gemdir}/gems/ancestry-%{version}/init.rb
%{gemdir}/gems/ancestry-%{version}/install.rb
%{gemdir}/gems/ancestry-%{version}/lib/ancestry.rb
%{gemdir}/gems/ancestry-%{version}/lib/ancestry/has_ancestry.rb
%{gemdir}/gems/ancestry-%{version}/lib/ancestry/exceptions.rb
%{gemdir}/gems/ancestry-%{version}/lib/ancestry/class_methods.rb
%{gemdir}/gems/ancestry-%{version}/lib/ancestry/instance_methods.rb
%{gemdir}/gems/ancestry-%{version}/MIT-LICENSE
%{gemdir}/gems/ancestry-%{version}/README.rdoc


%doc %{gemdir}/doc/ancestry-%{version}
%{gemdir}/cache/ancestry-%{version}.gem
%{gemdir}/specifications/ancestry-%{version}.gemspec

%changelog
* Mon Feb 4 2013 shk@redhat.com 1.3.0-1
- Updated to 1.3.0
