# Created by pyp2rpm-3.3.3
%global pypi_name createrepo-c
%global srcname createrepo_c

Name:           python-%{srcname}
Version:        0.15.10
Release:        1%{?dist}
Summary:        C implementation of createrepo

License:        GPLv2+
URL:            https://github.com/rpm-software-management
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/createrepo_c-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires: make
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: bzip2-devel
BuildRequires: expat-devel
BuildRequires: file-devel
BuildRequires: glib2-devel
BuildRequires: libcurl-devel
%if 0%{?rhel} == 7
BuildRequires: libmodulemd2-devel
%else
BuildRequires: libmodulemd-devel
%endif
BuildRequires: libxml2-devel
BuildRequires: rpm-devel
BuildRequires: openssl-devel
BuildRequires: sqlite-devel
BuildRequires: xz-devel
# not available on EL
# BuildRequires: zchunk-devel
BuildRequires: zlib-devel

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-setuptools

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n createrepo_c-%{version}
mkdir build

%build
pushd build
  %cmake .. -DPYTHON_DESIRED:FILEPATH=%{__python3} -DWITH_ZCHUNK=OFF -DENABLE_DRPM=OFF -DENABLE_BASHCOMP=OFF
  make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}"
popd

%install
pushd build
  make install DESTDIR=%{buildroot}
popd

%files -n python3-%{srcname}
%doc README.md
%{_bindir}/createrepo_c
%{_bindir}/mergerepo_c
%{_bindir}/modifyrepo_c
%{_bindir}/sqliterepo_c
%{python3_sitearch}/createrepo_c
%{python3_sitearch}/createrepo_c-%{version}-py%{python3_version}.egg-info
%{_libdir}/libcreaterepo_c*
%exclude %{_includedir}/createrepo_c/
%exclude %{_libdir}/pkgconfig/createrepo_c.pc
%exclude %{_mandir}/man8/createrepo_c.*
%exclude %{_mandir}/man8/mergerepo_c.*
%exclude %{_mandir}/man8/modifyrepo_c.*
%exclude %{_mandir}/man8/sqliterepo_c.*

%changelog
* Thu Apr 30 2020 Evgeni Golov - 0.15.10-1
- Initial package.
