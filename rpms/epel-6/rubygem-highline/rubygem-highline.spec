%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname highline
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary:        HighLine is a high-level command-line IO library
Name:           rubygem-%{gemname}
Version:        1.4.0
Release:        2%{?dist}
Group:          Development/Languages
License:        GPLv2+ or Ruby
URL:            http://highline.rubyforge.org
Source0:        http://rubyforge.org/frs/download.php/23791/%{gemname}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       rubygems
Requires:       ruby(abi) = 1.8
BuildRequires:  rubygems
BuildRequires:  rubygem-rake
BuildRequires:  zip
BuildArch:      noarch
Provides:       rubygem(%{gemname}) = %{version}

%description
A high-level IO library that provides validation, type conversion, and more
for command-line interfaces. HighLine also includes a complete menu system
that can crank out anything from simple list selection to complete shells with
just minutes of work.

%prep
%setup -q -n %{gemname}-%{version}
expr="s|/usr/local/bin/ruby|`which ruby`|"
sed -i -e $expr `find test/ examples/ lib/ -name '*.rb'`

%build
rake package

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc pkg/%{gemname}-%{version}.gem

cd %{buildroot}%{gemdir}/gems/%{gemname}-%{version}/
find test/ examples/ lib/ -name '*.rb' -exec chmod ugo+x {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/INSTALL
%doc %{geminstdir}/TODO
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/LICENSE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Sep 08 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.4.0-2
- Add ruby(abi) = 1.8 requires

* Sun Jul 13 2008 root <root@oss1-repo.usersys.redhat.com> - 1.4.0-1
- Initial package
