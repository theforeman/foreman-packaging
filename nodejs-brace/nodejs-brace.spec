# FIXME
# Remove nodejs_symlink_deps if installing bundled module with NPM

%global npm_name brace
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.10.0
Release: 1%{?dist}
Summary: browserify compatible version of the ace editor
License: MIT
URL: https://github.com/thlorenz/brace
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
cp -pfr .npmignore LICENSE README.md assets example ext index.d.ts index.js keybinding mode package.json snippets test theme worker %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
