%define rbname foremancli
%define version 1.0
%define release 1

Summary: This is the CLI for Foreman, which is a provisioning tool and node classifier for sysadmins.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ohadlevy/foreman/blob/master/extras/cli/foremancli
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-rest-client => 1.4
Requires: rubygem-rest-client < 2

Requires: rubygem-json => 1.4
Requires: rubygem-json < 2
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(foremancli) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This is the CLI for Foreman, which is a provisioning tool and node classifier
for sysadmins.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/foremancli
%{gemdir}/gems/foremancli-1.0/bin/foremancli
%{gemdir}/gems/foremancli-1.0/foremancli.gemspec
%{gemdir}/gems/foremancli-1.0/lib/foremancli/version.rb


%doc %{gemdir}/doc/foremancli-1.0
%{gemdir}/cache/foremancli-1.0.gem
%{gemdir}/specifications/foremancli-1.0.gemspec

%changelog
