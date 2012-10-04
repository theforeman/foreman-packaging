%define rbname has_many_polymorphs
%define version 3.0.0.beta1
%define release 3

Summary: An ActiveRecord plugin for self-referential and double-sided polymorphic associations.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://blog.evanweaver.com/files/doc/fauna/has_many_polymorphs/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-activerecord 
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(has_many_polymorphs) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description



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
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/support_methods.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/class_methods.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/autoload.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/railtie.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/association.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/rake_task_redefine_task.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/base.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/reflection.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs/debugging_tools.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/lib/has_many_polymorphs.rb
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/LICENSE
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/README
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/CHANGELOG
%{gemdir}/gems/has_many_polymorphs-3.0.0.beta1/Gemfile


%doc %{gemdir}/doc/has_many_polymorphs-3.0.0.beta1
%{gemdir}/cache/has_many_polymorphs-3.0.0.beta1.gem
%{gemdir}/specifications/has_many_polymorphs-3.0.0.beta1.gemspec

%changelog
