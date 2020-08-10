# Created by pyp2rpm-3.3.3
%global pypi_name Django
%global srcname django

Name:           python-%{srcname}
Version:        2.2.15
Release:        1%{?dist}
Summary:        A high-level Python Web framework that encourages rapid development and clean, pragmatic design

License:        BSD
URL:            https://www.djangoproject.com/
Source0:        https://files.pythonhosted.org/packages/source/D/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytz
BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlparse >= 0.2.2

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-pytz
Requires:       python3-setuptools
Requires:       python3-sqlparse >= 0.2.2

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# hard-code python3 in django-admin
pushd django
for file in bin/django-admin.py conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd

%build
%py3_build

%install
%py3_install

# rename django-admin so we don't conflict with python2-django
mv %{buildroot}%{_bindir}/django-admin %{buildroot}%{_bindir}/python3-django-admin

%files -n python3-%{srcname}
%license django/dispatch/license.txt django/contrib/gis/gdal/LICENSE django/contrib/gis/geos/LICENSE django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md django/contrib/admin/static/admin/fonts/LICENSE.txt django/contrib/admin/static/admin/img/LICENSE docs/_theme/djangodocs/static/fontawesome/LICENSE.txt LICENSE LICENSE.python
%doc django/contrib/admin/static/admin/fonts/README.txt django/contrib/admin/static/admin/img/README.txt docs/_theme/djangodocs/static/fontawesome/README.md tests/README.rst README.rst extras/README.TXT
%{_bindir}/python3-django-admin
%exclude %{_bindir}/django-admin.py
%{python3_sitelib}/django
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 10 2020 Evgeni Golov 2.2.15-1
- Update to 2.2.15

* Mon Jul 20 2020 Evgeni Golov 2.2.14-1
- Update to 2.2.14

* Thu Jun 04 2020 Evgeni Golov 2.2.13-1
- Update to 2.2.13

* Tue Apr 14 2020 Evgeni Golov 2.2.12-1
- Update to 2.2.12

* Wed Mar 18 2020 Samir Jha 2.2.11-1
- Update to 2.2.11

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.10-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov - 2.2.10-1
- Release python-django 2.2.10

* Wed Dec 18 2019 Evgeni Golov 2.2.9-1
- Update to 2.2.9

* Fri Dec 13 2019 Evgeni Golov 2.2.8-1
- Update to 2.2.8

* Mon Nov 18 2019 Evgeni Golov - 2.2.7-1
- Initial package.
