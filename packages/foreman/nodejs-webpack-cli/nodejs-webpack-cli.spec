%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name webpack-cli

Name: %{?scl_prefix}nodejs-webpack-cli
Version: 5.0.1
Release: 1%{?dist}
Summary: CLI for webpack & friends
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/webpack-cli/tree/master/packages/webpack-cli
Source0: https://registry.npmjs.org/@discoveryjs/json-ext/-/json-ext-0.5.7.tgz
Source1: https://registry.npmjs.org/@webpack-cli/configtest/-/configtest-2.1.1.tgz
Source2: https://registry.npmjs.org/@webpack-cli/info/-/info-2.0.2.tgz
Source3: https://registry.npmjs.org/@webpack-cli/serve/-/serve-2.0.5.tgz
Source4: https://registry.npmjs.org/clone-deep/-/clone-deep-4.0.1.tgz
Source5: https://registry.npmjs.org/colorette/-/colorette-2.0.20.tgz
Source6: https://registry.npmjs.org/commander/-/commander-9.5.0.tgz
Source7: https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.3.tgz
Source8: https://registry.npmjs.org/envinfo/-/envinfo-7.11.0.tgz
Source9: https://registry.npmjs.org/fastest-levenshtein/-/fastest-levenshtein-1.0.16.tgz
Source10: https://registry.npmjs.org/find-up/-/find-up-4.1.0.tgz
Source11: https://registry.npmjs.org/flat/-/flat-5.0.2.tgz
Source12: https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
Source13: https://registry.npmjs.org/hasown/-/hasown-2.0.0.tgz
Source14: https://registry.npmjs.org/import-local/-/import-local-3.1.0.tgz
Source15: https://registry.npmjs.org/interpret/-/interpret-3.1.1.tgz
Source16: https://registry.npmjs.org/is-core-module/-/is-core-module-2.13.1.tgz
Source17: https://registry.npmjs.org/is-plain-object/-/is-plain-object-2.0.4.tgz
Source18: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source19: https://registry.npmjs.org/isobject/-/isobject-3.0.1.tgz
Source20: https://registry.npmjs.org/kind-of/-/kind-of-6.0.3.tgz
Source21: https://registry.npmjs.org/locate-path/-/locate-path-5.0.0.tgz
Source22: https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz
Source23: https://registry.npmjs.org/p-locate/-/p-locate-4.1.0.tgz
Source24: https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz
Source25: https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz
Source26: https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz
Source27: https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz
Source28: https://registry.npmjs.org/pkg-dir/-/pkg-dir-4.2.0.tgz
Source29: https://registry.npmjs.org/rechoir/-/rechoir-0.8.0.tgz
Source30: https://registry.npmjs.org/resolve/-/resolve-1.22.8.tgz
Source31: https://registry.npmjs.org/resolve-cwd/-/resolve-cwd-3.0.0.tgz
Source32: https://registry.npmjs.org/resolve-from/-/resolve-from-5.0.0.tgz
Source33: https://registry.npmjs.org/shallow-clone/-/shallow-clone-3.0.1.tgz
Source34: https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz
Source35: https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz
Source36: https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz
Source37: https://registry.npmjs.org/webpack-cli/-/webpack-cli-5.0.1.tgz
Source38: https://registry.npmjs.org/webpack-merge/-/webpack-merge-5.10.0.tgz
Source39: https://registry.npmjs.org/which/-/which-2.0.2.tgz
Source40: https://registry.npmjs.org/wildcard/-/wildcard-2.0.1.tgz
Source41: nodejs-webpack-cli-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@discoveryjs/json-ext)) = 0.5.7
Provides: bundled(npm(@webpack-cli/configtest)) = 2.1.1
Provides: bundled(npm(@webpack-cli/info)) = 2.0.2
Provides: bundled(npm(@webpack-cli/serve)) = 2.0.5
Provides: bundled(npm(clone-deep)) = 4.0.1
Provides: bundled(npm(colorette)) = 2.0.20
Provides: bundled(npm(commander)) = 9.5.0
Provides: bundled(npm(cross-spawn)) = 7.0.3
Provides: bundled(npm(envinfo)) = 7.11.0
Provides: bundled(npm(fastest-levenshtein)) = 1.0.16
Provides: bundled(npm(find-up)) = 4.1.0
Provides: bundled(npm(flat)) = 5.0.2
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(hasown)) = 2.0.0
Provides: bundled(npm(import-local)) = 3.1.0
Provides: bundled(npm(interpret)) = 3.1.1
Provides: bundled(npm(is-core-module)) = 2.13.1
Provides: bundled(npm(is-plain-object)) = 2.0.4
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isobject)) = 3.0.1
Provides: bundled(npm(kind-of)) = 6.0.3
Provides: bundled(npm(locate-path)) = 5.0.0
Provides: bundled(npm(p-limit)) = 2.3.0
Provides: bundled(npm(p-locate)) = 4.1.0
Provides: bundled(npm(p-try)) = 2.2.0
Provides: bundled(npm(path-exists)) = 4.0.0
Provides: bundled(npm(path-key)) = 3.1.1
Provides: bundled(npm(path-parse)) = 1.0.7
Provides: bundled(npm(pkg-dir)) = 4.2.0
Provides: bundled(npm(rechoir)) = 0.8.0
Provides: bundled(npm(resolve)) = 1.22.8
Provides: bundled(npm(resolve-cwd)) = 3.0.0
Provides: bundled(npm(resolve-from)) = 5.0.0
Provides: bundled(npm(shallow-clone)) = 3.0.1
Provides: bundled(npm(shebang-command)) = 2.0.0
Provides: bundled(npm(shebang-regex)) = 3.0.0
Provides: bundled(npm(supports-preserve-symlinks-flag)) = 1.0.0
Provides: bundled(npm(webpack-cli)) = 5.0.1
Provides: bundled(npm(webpack-merge)) = 5.10.0
Provides: bundled(npm(which)) = 2.0.2
Provides: bundled(npm(wildcard)) = 2.0.1
AutoReq: no
AutoProv: no

%if 0%{?scl:1}
%define npm_cache_dir npm_cache
%else
%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%endif

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 41 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/cli.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/cli.js %{buildroot}%{_bindir}/webpack-cli

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/webpack-cli
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Dec 13 2023 Evgeni Golov 5.0.1-1
- Add nodejs-webpack-cli generated by npm2rpm using the bundle strategy

