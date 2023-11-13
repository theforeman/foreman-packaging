Name:		puppetlabs-stdlib
Version:	9.4.1
Release:	1%{?dist}
Summary:	Puppet Labs Standard Library
License:	ASL 2.0
URL:		https://github.com/puppetlabs/puppetlabs-stdlib
Source0:	https://forge.puppet.com/v3/files/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	((puppet-agent >= 7 with puppet-agent < 9) or (puppet >= 7 with puppet < 9))

%description
Puppet Labs Standard Library module.

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/puppet/modules/stdlib
cp -rp functions/ lib/ manifests/ types/ metadata.json %{buildroot}%{_datadir}/puppet/modules/stdlib/


%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{_datadir}/puppet/modules/stdlib

%changelog
* Mon Nov 13 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 9.4.1-1
- Update to 9.4.1

* Mon May 11 2020 <zhunting@redhat.com> - 5.2.0-1
- Update Puppetlabs-stdlib to 5.2.0

* Thu May 10 2018 Andrea Veri <averi@fedoraproject.org> - 4.25.1-1
- New upstream release.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-7.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-6.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-5.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-3.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Andrea Veri <averi@fedoraproject.org> - 4.5.1-2.20150121git7a91f20
- Make sure metadata.json gets installed correctly for Puppet to actually
  recognize the module release version. Thanks Simon Lukasik for the patch.

* Wed Jan 21 2015 Andrea Veri <averi@fedoraproject.org> - 4.5.1-1.20150121git7a91f20
- New upstream release. (Fixes CVE-2015-1029, Red Hat's BZ #1182578)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2.20140510git08b00d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Andrea Veri <averi@fedoraproject.org> - 4.2.1-1.20140510git08b00d9
- New upstream release.

* Fri May 09 2014 Andrea Veri <averi@fedoraproject.org> - 4.2.0-1.20140509gitf3be3b6
- New upstream release.
- Drop add-missing-shebangs.patch as it was applied upstream.

* Wed May 07 2014 Andrea Veri <averi@fedoraproject.org> - 4.1.0-1.20140507gite962b95
- Initial package release.
