%define rbname builder
%define version 2.1.2
%define release 1

Summary: Builders for MarkUp.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://onestepback.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(builder) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Builder provides a number of builder objects that make creating structured
data simple to do.  Currently the following builder objects are supported:  *
XML Markup * XML Events


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0} --no-rdoc --no-ri

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/builder-2.1.2/lib/blankslate.rb
%{gemdir}/gems/builder-2.1.2/lib/builder.rb
%{gemdir}/gems/builder-2.1.2/lib/builder/blankslate.rb
%{gemdir}/gems/builder-2.1.2/lib/builder/xchar.rb
%{gemdir}/gems/builder-2.1.2/lib/builder/xmlbase.rb
%{gemdir}/gems/builder-2.1.2/lib/builder/xmlevents.rb
%{gemdir}/gems/builder-2.1.2/lib/builder/xmlmarkup.rb
%{gemdir}/gems/builder-2.1.2/test/performance.rb
%{gemdir}/gems/builder-2.1.2/test/preload.rb
%{gemdir}/gems/builder-2.1.2/test/test_xchar.rb
%{gemdir}/gems/builder-2.1.2/test/testblankslate.rb
%{gemdir}/gems/builder-2.1.2/test/testeventbuilder.rb
%{gemdir}/gems/builder-2.1.2/test/testmarkupbuilder.rb
%{gemdir}/gems/builder-2.1.2/scripts/publish.rb
%doc %{gemdir}/gems/builder-2.1.2/CHANGES
%doc %{gemdir}/gems/builder-2.1.2/Rakefile
%doc %{gemdir}/gems/builder-2.1.2/README
%doc %{gemdir}/gems/builder-2.1.2/doc/releases/builder-1.2.4.rdoc
%doc %{gemdir}/gems/builder-2.1.2/doc/releases/builder-2.0.0.rdoc
%doc %{gemdir}/gems/builder-2.1.2/doc/releases/builder-2.1.1.rdoc


%{gemdir}/cache/builder-2.1.2.gem
%{gemdir}/specifications/builder-2.1.2.gemspec

%changelog
