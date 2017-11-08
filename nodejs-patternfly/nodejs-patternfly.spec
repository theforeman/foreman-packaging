%global npm_name patternfly
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 3.29.13
Release: 1%{?dist}
Summary: A reference implementation of PatternFly based on Bootstrap v3
License: Apache-2.0
URL: https://github.com/patternfly/patternfly
Source0: http://registry.npmjs.org/patternfly/-/patternfly-3.29.13.tgz
Source1: http://registry.npmjs.org/bootstrap-touchspin/-/bootstrap-touchspin-3.1.1.tgz
Source2: http://registry.npmjs.org/jquery/-/jquery-3.2.1.tgz
Source3: http://registry.npmjs.org/bootstrap-datepicker/-/bootstrap-datepicker-1.6.4.tgz
Source4: http://registry.npmjs.org/bootstrap/-/bootstrap-3.3.7.tgz
Source5: http://registry.npmjs.org/c3/-/c3-0.4.18.tgz
Source6: http://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source7: http://registry.npmjs.org/datatables.net-select/-/datatables.net-select-1.2.3.tgz
Source8: http://registry.npmjs.org/datatables.net-colreorder-bs/-/datatables.net-colreorder-bs-1.3.3.tgz
Source9: http://registry.npmjs.org/drmonty-datatables-colvis/-/drmonty-datatables-colvis-1.1.2.tgz
Source10: http://registry.npmjs.org/google-code-prettify/-/google-code-prettify-1.0.5.tgz
Source11: http://registry.npmjs.org/eonasdan-bootstrap-datetimepicker/-/eonasdan-bootstrap-datetimepicker-4.17.47.tgz
Source12: http://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source13: http://registry.npmjs.org/datatables.net/-/datatables.net-1.10.16.tgz
Source14: http://registry.npmjs.org/moment/-/moment-2.14.1.tgz
Source15: http://registry.npmjs.org/moment-timezone/-/moment-timezone-0.4.1.tgz
Source16: http://registry.npmjs.org/patternfly-bootstrap-combobox/-/patternfly-bootstrap-combobox-1.1.7.tgz
Source17: http://registry.npmjs.org/bootstrap-switch/-/bootstrap-switch-3.3.4.tgz
Source18: http://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-2.1.1.tgz
Source19: http://registry.npmjs.org/moment/-/moment-2.19.1.tgz
Source20: http://registry.npmjs.org/bootstrap-select/-/bootstrap-select-1.12.4.tgz
Source21: http://registry.npmjs.org/jquery-match-height/-/jquery-match-height-0.7.2.tgz
Source22: http://registry.npmjs.org/datatables.net/-/datatables.net-2.1.1.tgz
Source23: http://registry.npmjs.org/patternfly-bootstrap-treeview/-/patternfly-bootstrap-treeview-2.1.5.tgz
Source24: http://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.4.1.tgz
Source25: http://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.3.3.tgz
Source26: patternfly-3.29.13-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(patternfly) = 3.29.13
Provides: bundled-npm(bootstrap-touchspin) = 3.1.1
Provides: bundled-npm(jquery) = 3.2.1
Provides: bundled-npm(bootstrap-datepicker) = 1.6.4
Provides: bundled-npm(bootstrap) = 3.3.7
Provides: bundled-npm(c3) = 0.4.18
Provides: bundled-npm(font-awesome) = 4.7.0
Provides: bundled-npm(datatables.net-select) = 1.2.3
Provides: bundled-npm(datatables.net-colreorder-bs) = 1.3.3
Provides: bundled-npm(drmonty-datatables-colvis) = 1.1.2
Provides: bundled-npm(google-code-prettify) = 1.0.5
Provides: bundled-npm(eonasdan-bootstrap-datetimepicker) = 4.17.47
Provides: bundled-npm(d3) = 3.5.17
Provides: bundled-npm(datatables.net) = 1.10.16
Provides: bundled-npm(moment) = 2.14.1
Provides: bundled-npm(moment-timezone) = 0.4.1
Provides: bundled-npm(patternfly-bootstrap-combobox) = 1.1.7
Provides: bundled-npm(bootstrap-switch) = 3.3.4
Provides: bundled-npm(datatables.net-bs) = 2.1.1
Provides: bundled-npm(moment) = 2.19.1
Provides: bundled-npm(bootstrap-select) = 1.12.4
Provides: bundled-npm(jquery-match-height) = 0.7.2
Provides: bundled-npm(datatables.net) = 2.1.1
Provides: bundled-npm(patternfly-bootstrap-treeview) = 2.1.5
Provides: bundled-npm(datatables.net-colreorder) = 1.4.1
Provides: bundled-npm(datatables.net-colreorder) = 1.3.3
AutoReq: no
AutoProv: no

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done

%setup -T -q -a 26 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/patternfly
cp -pfr LICENSE.txt README.md dist package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf LICENSE.txt README.md LICENSE.txt ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE.txt
%doc LICENSE.txt
%doc README.md

%changelog
* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.29.13-1
- new package built with tito

