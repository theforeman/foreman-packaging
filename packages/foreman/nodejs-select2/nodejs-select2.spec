%global npm_name select2
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.5.2-browserify
Release: 1%{?dist}
Summary: Browserify-ed version of Select2
License: 
Group: Development/Libraries
URL: http://ivaynberg.github.io/select2
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr component.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2-bootstrap.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2-spinner.gif %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2.jquery.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2.png %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ar.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_az.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_bg.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ca.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_cs.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_da.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_de.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_el.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_en.js.template %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_es.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_et.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_eu.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_fa.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_fi.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_fr.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_gl.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_he.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_hr.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_hu.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_id.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_is.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_it.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ja.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ka.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ko.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_lt.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_lv.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_mk.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ms.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_nb.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_nl.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_no.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_pl.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_pt-BR.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_pt-PT.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ro.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_rs.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ru.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_sk.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_sv.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_th.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_tr.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_ug-CN.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_uk.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_vi.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_zh-CN.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2_locale_zh-TW.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select2x2.png %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CONTRIBUTING.md
%doc README.md

%changelog
* Thu Jun 07 2018 Tomas Strachota <tstrachota@redhat.com> 3.5.2-browserify-1
- Update to 3.5.2-browserify

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 3.5.2-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 3.5.2-2
- Include GIF files in package (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 3.5.2-1
- new package built with tito

