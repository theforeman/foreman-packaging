%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%bcond tests 0

Name:           python-onigurumacffi
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python cffi bindings for the Oniguruma regex engine

License:        MIT
URL:            https://github.com/asottile/onigurumacffi
Source:         %{url}/archive/v%{version}/onigurumacffi-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3.12-cffi
BuildRequires:  python3.12-wheel
Buildrequires:  pkgconfig(oniguruma)

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
onigurumacffi provides Python cffi bindings for the Oniguruma regex engine.}

%description %{_description}

%package -n python3-onigurumacffi
Summary:    %{summary}

%description -n python3-onigurumacffi %{_description}

%prep
%autosetup -n onigurumacffi-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l onigurumacffi

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-onigurumacffi -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_onigurumacffi.abi3.so

%changelog
* Mon Nov 10 2025 Maximilian Kolb <kolb@atix.de> - 1.3.0-1
- Release python-onigurumacffi 1.3.0
