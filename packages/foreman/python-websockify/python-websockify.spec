# Created by pyp2rpm-3.3.8
%global pypi_name websockify
%global summary WSGI based adapter for the Websockets protocol

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        1%{?dist}
Summary:        %{summary}

License:        LGPLv3
URL:            https://github.com/novnc/websockify
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# TODO: Have the following handle multi line entries
# numpy is listed as install_requires in setup.py however it is optional
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/websockify

%changelog
* Thu Sep 01 2022 Eric D. Helms <ericdhelms@gmail.com> 0.10.0-4
- Update to build against Python 3.9

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.11

* Fri Feb 04 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Yatin Karel <ykarel@redhat.com> - 0.9.0-1
- Update to 0.9.0 (Resolves #1816608)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-14
- Rebuilt for Python 3.8

* Sun Aug 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-13
- Subpackage python2-websockify has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-9
- Rebuilt for Python 3.7

* Fri Feb 16 2018 2018 Lumír Balhar <lbalhar@redhat.com> - 0.8.0-8
- Fix directory ownership

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuild for Python 3.6

* Mon Aug 29 2016 Jan Beran <jberan@redhat.com> - 0.8.0-3
- Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 19 2016 Solly Ross <sross@redhat.com> - 0.8.0-1
- Update to release 0.8.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Pádraig Brady <pbrady@redhat.com> - 0.6.0-2
- Support big endian systems - rhbz#1216219

* Mon Mar 23 2015 Nikola Đipanov <ndipanov@redhat.com> - 0.6.0-1
- Update to release 0.6.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Nikola Đipanov <ndipanov@redhat.com> - 0.5.1-1
- Update to release 0.5.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Pádraig Brady <P@draigBrady.com> - 0.4.1-1
- Update to release 0.4.1

* Tue Mar 12 2013 Pádraig Brady <P@draigBrady.com> - 0.2.0-4
- Add runtime dependency on setuptools

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 31 2012 Pádraig Brady <P@draigBrady.com> - 0.2.0-2
- Remove hard dependency on numpy

* Mon Oct 22 2012 Nikola Đipanov <ndipanov@redhat.com> - 0.2.0-1
- Moving to the upstream version 0.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 6 2012 Adam Young <ayoung@redhat.com> - 0.1.0-4
- Added Description
- Added Manpage

* Fri May 11 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.1.0-2
- spec cleanup

* Thu May 10 2012 Adam Young <ayoung@redhat.com> - 0.1.0-1
- Initial RPM release.
