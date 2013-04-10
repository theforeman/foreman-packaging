%define rbname formatador
%define version 0.2.1
%define release 1

Summary: Ruby STDOUT text formatting
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/geemus/NAME
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(formatador) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
STDOUT text formatting


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
%{gemdir}/gems/formatador-0.2.1/Gemfile
%doc %{gemdir}/gems/formatador-0.2.1/README.rdoc
%{gemdir}/gems/formatador-0.2.1/Rakefile
%{gemdir}/gems/formatador-0.2.1/formatador.gemspec
%{gemdir}/gems/formatador-0.2.1/lib/formatador.rb
%{gemdir}/gems/formatador-0.2.1/lib/formatador/progressbar.rb
%{gemdir}/gems/formatador-0.2.1/lib/formatador/table.rb
%{gemdir}/gems/formatador-0.2.1/tests/basic_tests.rb
%{gemdir}/gems/formatador-0.2.1/tests/table_tests.rb
%{gemdir}/gems/formatador-0.2.1/tests/tests_helper.rb


%doc %{gemdir}/doc/formatador-0.2.1
%{gemdir}/cache/formatador-0.2.1.gem
%{gemdir}/specifications/formatador-0.2.1.gemspec

%changelog
