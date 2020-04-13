# Created by pyp2rpm-3.3.3
%global pypi_name aiohttp

Name:           python-%{pypi_name}
Version:        3.6.2
Release:        3%{?dist}
Summary:        Async http client/server framework (asyncio)

License:        Apache 2
URL:            https://github.com/aio-libs/aiohttp
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         allow-larger-headers.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-async-timeout < 4.0
Requires:       python3-async-timeout >= 3.0
Requires:       python3-attrs >= 17.3.0
Requires:       python3-chardet < 4.0
Requires:       python3-chardet >= 2.0
Requires:       python3-idna-ssl
Requires:       python3-multidict < 5.0
Requires:       python3-multidict >= 4.5
Requires:       python3-typing-extensions
Requires:       python3-yarl < 2.0
Requires:       python3-yarl >= 1.0

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
%license LICENSE.txt vendor/http-parser/LICENSE-MIT
%doc README.rst vendor/http-parser/README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 13 2020 Brian Bouterse <bmbouter@redhat.com> - 3.6.2-3
- Raised incoming http header size limits that aiohttp Server accepts

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.6.2-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.6.2-1
- Initial package.
