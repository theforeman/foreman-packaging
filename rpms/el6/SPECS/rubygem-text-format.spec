%define rbname text-format
%define version 1.0.0
%define release 1

Summary: Text::Format formats fixed-width text nicely.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://rubyforge.org/projects/text-format
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-text-hyphen => 1.0.0
Requires: rubygem-text-hyphen < 1.1
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(text-format) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Text::Format is provides the ability to nicely format fixed-width text with
knowledge of the writeable space (number of columns), margins, and indentation
settings. Text::Format can work with either TeX::Hyphen or Text::Hyphen to
hyphenate words when formatting.


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
%doc %{gemdir}/gems/text-format-1.0.0/Changelog
%doc %{gemdir}/gems/text-format-1.0.0/Install
%{gemdir}/gems/text-format-1.0.0/metaconfig
%{gemdir}/gems/text-format-1.0.0/pre-setup.rb
%{gemdir}/gems/text-format-1.0.0/Rakefile
%doc %{gemdir}/gems/text-format-1.0.0/README
%{gemdir}/gems/text-format-1.0.0/setup.rb
%{gemdir}/gems/text-format-1.0.0/ToDo
%{gemdir}/gems/text-format-1.0.0/lib/text/format.rb
%{gemdir}/gems/text-format-1.0.0/lib/text/format/alpha.rb
%{gemdir}/gems/text-format-1.0.0/lib/text/format/number.rb
%{gemdir}/gems/text-format-1.0.0/lib/text/format/roman.rb
%{gemdir}/gems/text-format-1.0.0/tests/tc_text_format.rb
%{gemdir}/gems/text-format-1.0.0/tests/testall.rb


%doc %{gemdir}/doc/text-format-1.0.0
%{gemdir}/cache/text-format-1.0.0.gem
%{gemdir}/specifications/text-format-1.0.0.gemspec

%changelog
