%define rbname hirb-unicode
%define version 0.0.5
%define release 1

Summary: Unicode support for hirb
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-hirb => 0.5
Requires: rubygem-hirb < 1

Requires: rubygem-unicode-display_width => 0.1.1
Requires: rubygem-unicode-display_width < 0.2
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(hirb-unicode) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Unicode support for hirb


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
%{gemdir}/gems/hirb-unicode-0.0.5/.gitignore
%{gemdir}/gems/hirb-unicode-0.0.5/Gemfile
%{gemdir}/gems/hirb-unicode-0.0.5/MIT-LICENSE
%{gemdir}/gems/hirb-unicode-0.0.5/README.md
%{gemdir}/gems/hirb-unicode-0.0.5/Rakefile
%{gemdir}/gems/hirb-unicode-0.0.5/hirb-unicode.gemspec
%{gemdir}/gems/hirb-unicode-0.0.5/lib/hirb-unicode.rb
%{gemdir}/gems/hirb-unicode-0.0.5/lib/hirb/unicode.rb
%{gemdir}/gems/hirb-unicode-0.0.5/lib/hirb/unicode/string_util.rb
%{gemdir}/gems/hirb-unicode-0.0.5/lib/hirb/unicode/version.rb
%{gemdir}/gems/hirb-unicode-0.0.5/test/string_test.rb
%{gemdir}/gems/hirb-unicode-0.0.5/test/test_helper.rb


%doc %{gemdir}/doc/hirb-unicode-0.0.5
%{gemdir}/cache/hirb-unicode-0.0.5.gem
%{gemdir}/specifications/hirb-unicode-0.0.5.gemspec

%changelog
