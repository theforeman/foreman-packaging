%global		revision	fcd686f1
%{expand:	%%global	archivename	gyp-%{version}%{?revision:-git%{revision}}}
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%if 0%{?rhel} == 5
%global __python2 /usr/bin/python26
%global __os_install_post %__multiple_python_os_install_post
%endif
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		gyp
Version:	0.1
Release:	0.33%{?revision:.%{revision}git}%{?dist}.1
Summary:	Generate Your Projects

License:	BSD
URL:		https://gyp.gsrc.io
# No released tarball avaiable. so the tarball was generated
# from svn as following:
#
# 1. git clone https://chromium.googlesource.com/external/gyp
# 2. cd gyp
# 3. version=$(grep version= setup.py|cut -d\' -f2)
# 4. revision=$(git log --oneline|head -1|cut -d' ' -f1)
# 5. tar -a --exclude-vcs -cf /tmp/gyp-$version-git$revision.tar.xz *
Source0:	%{archivename}.tar.xz
Patch0:		gyp-rpmoptflags.patch
Patch1:		gyp-ninja-build.patch
Patch2:		gyp-python3.patch
Patch3:		gyp-python38.patch
Patch4:		gyp-fix-cmake.patch

%if 0%{?rhel}
%if 0%{?rhel} == 5
BuildRequires:	python26-devel
%elif 0%{?rhel} < 8
BuildRequires:	python2-devel
%else
BuildRequires:	python3-devel
%endif
%if 0%{?rhel} < 8
BuildRequires:	python2-setuptools
Requires:	python2-setuptools
%else
BuildRequires:	python3-setuptools
Requires:	python3-setuptools
%endif
%else
BuildRequires:	python3-devel python3-setuptools
Requires:	python3-setuptools
%endif
BuildRequires:	gcc gcc-c++ ninja-build
BuildArch:	noarch

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons
and/or make build files from a platform-independent input format.

Its syntax is a universal cross-platform build representation
that still allows sufficient per-platform flexibility to accommodate
irreconcilable differences.


%prep
%autosetup -p1 -c -n %{archivename}
for i in $(find pylib -name '*.py'); do
	sed -e '\,#![ \t]*/.*python,{d}' $i > $i.new && touch -r $i $i.new && mv $i.new $i
done

%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --root $RPM_BUILD_ROOT --skip-build


%check
%{__python3} gyptest.py test/hello/gyptest-all.py


%files
%license LICENSE
%doc AUTHORS
%{_bindir}/gyp
%{python3_sitelib}/*


%changelog
* Thu Oct  3 2019 Akira TAGOH <tagoh@redhat.com> - 0.1-0.33.fcd686f1git.1
- Fix BR.

* Fri Aug 23 2019 Akira TAGOH <tagoh@redhat.com> - 0.1-0.33.fcd686f1git
- Fix the build issue with cmake. (#1744037)
- Fix the build issue with Python 3.8.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.32.fcd686f1git
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Akira TAGOH <tagoh@redhat.com> - 0.1-0.31.fcd686f1git
- Rebase to fcd686f1.
- Requires python3 instead of python2 (#1737984)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.30.920ee58git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.29.920ee58git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.28.920ee58git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Akira TAGOH <tagoh@redhat.com> - 0.1-0.26.920ee58git
- Modernize the spec file.

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1-0.25.920ee58git
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.920ee58git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.920ee58git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.920ee58git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Akira TAGOH <tagoh@redhat.com> - 0.1-0.21.920ee58git
- Rebase to 920ee58
- Call ninja-build instead of ninja (#1385423)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.20.0bb6747git
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.0bb6747git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.18.0bb6747git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May  1 2015 Akira TAGOH <tagoh@redhat.com> - 0.1-0.17.0bb6747git
- Rebase to 0bb6747.
- Add R: python-setuptools (#1217358)

* Mon Mar  2 2015 Akira TAGOH <tagoh@redhat.com> - 0.1-0.16.2037svn
- Rebase to r2037.

* Wed Jun 25 2014 Akira TAGOH <tagoh@redhat.com> - 0.1-0.15.1617svn
- Update rpm macros to the latest guidelines.
- Build against python26 for EPEL5.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.12.1617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.11.1617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Akira TAGOH <tagoh@redhat.com> - 0.1-0.10.1617svn
- Rebase to r1617

* Tue Feb 12 2013 Akira TAGOH <tagoh@redhat.com> - 0.1-0.9.1569svn
- Rebase to r1569 (#908983)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.8.1010svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.1010svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Akira TAGOH <tagoh@redhat.com> - 0.1-0.6.1010svn
- Rebase to r1010.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.840svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Akira TAGOH <tagoh@redhat.com> - 0.1-0.4.840svn
- Rebase to r840.
- generate Makefile with RPM_OPT_FLAGS in CCFLAGS.

* Fri Aug  6 2010 Akira TAGOH <tagoh@redhat.com> - 0.1-0.3.839svn
- Drop the unnecessary macro.

* Thu Aug  5 2010 Akira TAGOH <tagoh@redhat.com. - 0.1-0.2.839svn
- Update the spec file according to the suggestion in rhbz#621242.

* Wed Aug  4 2010 Akira TAGOH <tagoh@redhat.com> - 0.1-0.1.839svn
- Initial packaging.

