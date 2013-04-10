%define rbname polyglot
%define version 0.3.3
%define release 1

Summary: Augment 'require' to load non-Ruby file types
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/cjheath/polyglot
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(polyglot) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
The Polyglot library allows a Ruby module to register a loader
for the file type associated with a filename extension, and it
augments 'require' to find and load matching files.


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
%{gemdir}/gems/polyglot-0.3.3/History.txt
%{gemdir}/gems/polyglot-0.3.3/License.txt
%doc %{gemdir}/gems/polyglot-0.3.3/README.txt
%{gemdir}/gems/polyglot-0.3.3/Rakefile
%{gemdir}/gems/polyglot-0.3.3/lib/polyglot.rb
%{gemdir}/gems/polyglot-0.3.3/lib/polyglot/version.rb


%doc %{gemdir}/doc/polyglot-0.3.3
%{gemdir}/cache/polyglot-0.3.3.gem
%{gemdir}/specifications/polyglot-0.3.3.gemspec

%changelog
