{{ data.credit_line }}
{% from 'macros.spec' import dependencies, for_python_versions, underscored_or_pypi, macroed_url -%}
%global pypi_name {{ data.name }}
{%- if data.srcname %}
%global srcname {{ data.srcname }}
{%- endif %}

Name:           {{ data.pkg_name|macroed_pkg_name(data.srcname) }}
Version:        {{ data.version }}
Release:        1%{?dist}
Summary:        {{ data.summary }}

License:        {{ data.license }}
URL:            {{ data.home_page }}
Source0:        {{ data.source0|replace(data.name, '%{pypi_name}')|replace(data.version, '%{version}') }}

{%- if not data.has_extension %}
BuildArch:      noarch
{%- endif %}
{%- for pv in data.sorted_python_versions %}
{{ dependencies(data.build_deps, False, pv, data.base_python_version, False) }}
{%- endfor %}

%description
%{summary}
{% for pv in data.sorted_python_versions %}
%package -n     {{data.pkg_name|macroed_pkg_name(data.srcname)|name_for_python_version(pv, True) }}
Summary:        %{summary}
%{?python_provide:%python_provide {{data.pkg_name|macroed_pkg_name(data.srcname)|name_for_python_version(pv, True)}}}
{{- dependencies(data.runtime_deps, True, pv, pv) }}

%description -n {{data.pkg_name|macroed_pkg_name(data.srcname)|name_for_python_version(pv, True) }}
%{summary}
{%- endfor %}

%prep
%autosetup -n {{ data.dirname|replace(data.name, '%{pypi_name}')|replace(data.version, '%{version}')|default('%{pypi_name}-%{version}', true) }}
{%- if data.has_bundled_egg_info %}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
{%- endif %}

%build
{%- for pv in data.sorted_python_versions %}
%py{{ pv }}_build
{%- endfor %}

%install
{%- if data.python_versions|length > 0 %}
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
{%- endif %}
{%- for pv in data.python_versions + [data.base_python_version] %}
{%- if pv == data.base_python_version and data.python_versions and data.scripts %}
rm -rf %{buildroot}%{_bindir}/*
{%- endif %}
%py{{ pv }}_install
{% endfor -%}

{% for pv in data.sorted_python_versions %}
%files -n {{ data.pkg_name|macroed_pkg_name(data.srcname)|name_for_python_version(pv, True) }}
{%- if data.doc_license %}
%license {{data.doc_license|join(' ')}}
{%- endif %}
{%- if data.doc_files %}
%doc {{data.doc_files|join(' ') }}
{%- endif %}
{%- if pv == data.base_python_version %}
{%- for script in data.scripts %}
%{_bindir}/{{ script }}
{%- endfor %}
{%- endif %}
{%- if data.py_modules %}
{%- for module in data.py_modules -%}
{%- if pv == '3' %}
%{python{{ pv }}_sitelib}/__pycache__/*
{%- endif %}
%{python{{ pv }}_sitelib}/{{ data.name | module_to_path(module) }}.py{% if pv != '3'%}*{% endif %}
{%- endfor %}
{%- endif %}
{%- if data.has_extension %}
{%- if data.has_packages %}
{%- for package in data.packages %}
%{python{{ pv }}_sitearch}/{{ package | package_to_path(data.name) }}
{%- endfor %}
{%- endif %}
{%- if data.has_pth %}
%{python{{ pv }}_sitearch}/{{ underscored_or_pypi(data.name, data.underscored_name) }}-%{version}-py%{python{{ pv }}_version}-*.pth
{%- endif %}
%{python{{ pv }}_sitearch}/{{ underscored_or_pypi(data.name, data.underscored_name) }}-%{version}-py%{python{{ pv }}_version}.egg-info
{%- else %}
{%- if data.has_packages %}
{%- for package in data.packages %}
%{python{{ pv }}_sitelib}/{{ package | package_to_path(data.name) }}
{%- endfor %}
{%- endif %}
{%- if data.has_pth %}
%{python{{ pv }}_sitelib}/{{ underscored_or_pypi(data.name, data.underscored_name) }}-%{version}-py%{python{{ pv }}_version}-*.pth
{%- endif %}
%{python{{ pv }}_sitelib}/{{ underscored_or_pypi(data.name, data.underscored_name) }}-%{version}-py%{python{{ pv }}_version}.egg-info
{%- endif %}
{% endfor %}
%changelog
* {{ data.changelog_date_packager }} - {{ data.version }}-1
- Initial package.
