# Created by pyp2rpm-3.3.3
%global pypi_name odfpy

Name:           python-%{pypi_name}
Version:        1.4.1
Release:        1%{?dist}
Summary:        Python API and tools to manipulate OpenDocument files

License:        None
URL:            https://github.com/eea/odfpy
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-defusedxml

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license APACHE-LICENSE-2.0.txt GPL-LICENSE-2.txt
%doc contrib/ODFFile/README.txt README.md
%{_bindir}/csv2ods
%{_bindir}/mailodf
%{_bindir}/odf2mht
%{_bindir}/odf2xhtml
%{_bindir}/odf2xml
%{_bindir}/odfimgimport
%{_bindir}/odflint
%{_bindir}/odfmeta
%{_bindir}/odfoutline
%{_bindir}/odfuserfield
%{_bindir}/xml2odf
%{_mandir}/*/csv2ods*
%{_mandir}/*/mailodf*
%{_mandir}/*/odf2mht*
%{_mandir}/*/odf2xhtml*
%{_mandir}/*/odf2xml*
%{_mandir}/*/odfimgimport*
%{_mandir}/*/odflint*
%{_mandir}/*/odfmeta*
%{_mandir}/*/odfoutline*
%{_mandir}/*/odfuserfield*
%{_mandir}/*/xml2odf*
%{python3_sitelib}/odf
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov - 1.4.1-1
- Initial package.
