%global npm_name babel-plugin-lodash

Name: nodejs-%{npm_name}
Version: 3.3.4
Release: 1%{?dist}
Summary: Modular Lodash builds without the hassle
License: MIT
Group: Development/Libraries
URL: https://github.com/lodash/babel-plugin-lodash#readme
Source0: https://registry.npmjs.org/babel-plugin-lodash/-/babel-plugin-lodash-3.3.4.tgz
Source1: https://registry.npmjs.org/require-package-name/-/require-package-name-2.0.1.tgz
Source2: https://registry.npmjs.org/@babel/types/-/@babel/types-7.0.0-beta.51.tgz
Source3: https://registry.npmjs.org/@babel/helper-module-imports/-/@babel/helper-module-imports-7.0.0-beta.51.tgz
Source4: https://registry.npmjs.org/glob/-/glob-7.1.2.tgz
Source5: https://registry.npmjs.org/lodash/-/lodash-4.17.10.tgz
Source6: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz
Source7: https://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source8: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source9: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source10: https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source11: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source12: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source13: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source14: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source15: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source16: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source17: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source18: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/helper-module-imports)) = 7.0.0-beta.51
Provides: bundled(npm(@babel/types)) = 7.0.0-beta.51
Provides: bundled(npm(babel-plugin-lodash)) = 3.3.4
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(esutils)) = 2.0.2
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(glob)) = 7.1.2
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.3
Provides: bundled(npm(lodash)) = 4.17.10
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(require-package-name)) = 2.0.1
Provides: bundled(npm(to-fast-properties)) = 2.0.0
Provides: bundled(npm(wrappy)) = 1.0.2
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
%setup -T -q -a 18 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Jun 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.3.4-1
- Update to 3.3.4

* Wed Jan 03 2018 Daniel Lobato Garcia <me@daniellobato.me> 3.3.2-1
- new package built with tito

