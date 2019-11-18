# Created by pyp2rpm-3.3.3
%global pypi_name uritemplate

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        URI templates

License:        BSD 3-Clause License or Apache License, Version 2.0
URL:            https://uritemplate.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
uritemplate Documentation_ -- GitHub_ -- BitBucket_ -- Travis-CI_Simple python
library to deal with URI Templates_. The API looks like.. code-block:: python
from uritemplate import URITemplate, expand NOTE: URI params must be strings
not integers gist_uri ' t URITemplate(gist_uri)
print(t.expand(gist_id'123456')) > or print(expand(gist_uri, gist_id'123456'))
also t.expand({'gist_id':...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
uritemplate Documentation_ -- GitHub_ -- BitBucket_ -- Travis-CI_Simple python
library to deal with URI Templates_. The API looks like.. code-block:: python
from uritemplate import URITemplate, expand NOTE: URI params must be strings
not integers gist_uri ' t URITemplate(gist_uri)
print(t.expand(gist_id'123456')) > or print(expand(gist_uri, gist_id'123456'))
also t.expand({'gist_id':...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst tests/fixtures/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 3.0.0-1
- Initial package.
