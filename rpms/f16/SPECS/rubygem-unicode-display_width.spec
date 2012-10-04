%define rbname unicode-display_width
%define version 0.1.1
%define release 1

Summary: Support for east_asian_width string widths.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/janlelis/unicode-display_width
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(unicode-display_width) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This gem adds String#display_size to get the display size of a string using
EastAsianWidth.txt.


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
%{gemdir}/gems/unicode-display_width-0.1.1/lib/unicode/display_size.rb
%{gemdir}/gems/unicode-display_width-0.1.1/lib/unicode/display_width.rb
%doc %{gemdir}/gems/unicode-display_width-0.1.1/LICENSE.txt
%doc %{gemdir}/gems/unicode-display_width-0.1.1/README.rdoc
%{gemdir}/gems/unicode-display_width-0.1.1/data/EastAsianWidth.txt
%{gemdir}/gems/unicode-display_width-0.1.1/data/EastAsianWidth.index
%{gemdir}/gems/unicode-display_width-0.1.1/Rakefile
%{gemdir}/gems/unicode-display_width-0.1.1/.gemspec


%doc %{gemdir}/doc/unicode-display_width-0.1.1
%{gemdir}/cache/unicode-display_width-0.1.1.gem
%{gemdir}/specifications/unicode-display_width-0.1.1.gemspec

%changelog
