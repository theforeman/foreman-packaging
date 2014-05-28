# Generated from thor-0.14.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname thor
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A scripting framework that replaces rake, sake and rubigen
Name: rubygem-%{gemname}
Version: 0.14.6
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://yehudakatz.com
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: ruby(abi) = 1.8
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A scripting framework that replaces rake, sake and rubigen

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}

gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)

%{_bindir}/thor

%{_bindir}/rake2thor

%{gemdir}/gems/%{gemname}-%{version}/

%doc %{gemdir}/doc/%{gemname}-%{version}

%doc %{geminstdir}/CHANGELOG.rdoc

%doc %{geminstdir}/LICENSE

%doc %{geminstdir}/README.md

%doc %{geminstdir}/Thorfile

%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.14.6-2
- rebuild

* Mon Jan 17 2011 Shannon Hughes <shughes@redhat.com> 0.14.6-1
- rebuild for 0.14.6 (shughes@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 0.14.4-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 0.14.4-1
- Initial package
