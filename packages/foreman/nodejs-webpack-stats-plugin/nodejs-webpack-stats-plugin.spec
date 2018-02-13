# FIXME
# Remove nodejs_symlink_deps if installing bundled module with NPM

%global npm_name webpack-stats-plugin
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.1.5
Release: 1%{?dist}
Summary: Webpack stats plugin
License: MIT
URL: https://github.com/FormidableLabs/webpack-stats-plugin/issues
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%{?nodejs_find_provides_and_requires}

%description
%{summary}

%prep
%setup -q -n package

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr HISTORY.md LICENSE.txt README.md index.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE.txt
%doc HISTORY.md
%doc LICENSE.txt
%doc README.md

%changelog
* Tue Jul 18 2017 Michael Moll <kvedulv@kvedulv.de> 0.1.5-1
- Replace nodejs-stats-webpack-plugin with nodejs-webpack-stats-plugin

