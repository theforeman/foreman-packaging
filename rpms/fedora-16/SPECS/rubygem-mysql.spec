# Generated from mysql-2.8.1.gem by gem2rpm -*- rpm-spec -*-
%global gemname mysql

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: This is the MySQL API module for Ruby
Name: rubygem-%{gemname}
Version: 2.8.1
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://mysql-win.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.6
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby >= 1.8.6
Provides: rubygem(%{gemname}) = %{version}

%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby
programs that the MySQL C API provides for C programs.
This is a conversion of tmtm's original extension into a proper RubyGems.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gemdir} \
            -V \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%{gemdir}/gems/mysql-2.8.1/COPYING
%{gemdir}/gems/mysql-2.8.1/COPYING.ja
%{gemdir}/gems/mysql-2.8.1/Rakefile
%{gemdir}/gems/mysql-2.8.1/extra/README.html
%{gemdir}/gems/mysql-2.8.1/extra/README_ja.html
%{gemdir}/gems/mysql-2.8.1/extra/tommy.css
%{gemdir}/gems/mysql-2.8.1/tasks/gem.rake
%{gemdir}/gems/mysql-2.8.1/tasks/native.rake
%{gemdir}/gems/mysql-2.8.1/tasks/vendor_mysql.rake
%{gemdir}/gems/mysql-2.8.1/test/test_mysql.rb


%changelog
* Tue May 08 2012 jmontleo@redhat.com - 2.8.1-2
- Cleaned up spec file
* Tue Apr 10 2012 jason - 2.8.1-1
- Initial package
