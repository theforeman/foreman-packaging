# Created by pyp2rpm-3.3.3
%global pypi_name diff-match-patch

Name:           python-%{pypi_name}
Version:        20181111
Release:        1%{?dist}
Summary:        Repackaging of Google's Diff Match and Patch libraries

License:        Apache
URL:            https://github.com/diff-match-patch-python/diff-match-patch
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools >= 38.6.0

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

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
%license LICENSE
%doc README.md
%{python3_sitelib}/diff_match_patch
%{python3_sitelib}/diff_match_patch-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov - 20181111-1
- Initial package.
