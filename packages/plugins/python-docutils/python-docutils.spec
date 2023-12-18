%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.8
%global pypi_name docutils

Name:           python-%{pypi_name}
Version:        0.19
Release:        2%{?dist}
Summary:        Docutils -- Python Documentation Utilities

License:        public domain, Python, 2-Clause BSD, GPL 3 (see COPYING.txt)
URL:            https://docutils.sourceforge.io/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING.txt
%doc README.txt docutils/parsers/rst/include/README.txt docutils/writers/s5_html/themes/README.txt test/functional/README.txt test/functional/output/README.txt tools/dev/README.txt tools/editors/README.txt tools/editors/emacs/README.txt tools/editors/emacs/tests/README.txt
%exclude %{_bindir}/docutils
%exclude %{_bindir}/rst2html.py
%exclude %{_bindir}/rst2html4.py
%exclude %{_bindir}/rst2html5.py
%exclude %{_bindir}/rst2latex.py
%exclude %{_bindir}/rst2man.py
%exclude %{_bindir}/rst2odt.py
%exclude %{_bindir}/rst2odt_prepstyles.py
%exclude %{_bindir}/rst2pseudoxml.py
%exclude %{_bindir}/rst2s5.py
%exclude %{_bindir}/rst2xetex.py
%exclude %{_bindir}/rst2xml.py
%exclude %{_bindir}/rstpep2html.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Dec 01 2023 Odilon Sousa <osousa@redhat.com> - 0.19-2
- Rebuild against python 3.11

* Wed Aug 31 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.19-1
- Initial package.
