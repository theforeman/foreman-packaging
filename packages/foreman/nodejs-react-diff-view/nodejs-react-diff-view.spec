%global npm_name react-diff-view

Name: nodejs-%{npm_name}
Version: 1.8.1
Release: 1%{?dist}
Summary: A git diff component to consume the git unified diff output
License: MIT
Group: Development/Libraries
URL: https://github.com/otakustay/react-diff-view#readme
Source0: https://registry.npmjs.org/react-diff-view/-/react-diff-view-1.8.1.tgz
Source1: https://registry.npmjs.org/warning/-/warning-4.0.2.tgz
Source2: https://registry.npmjs.org/lodash.escape/-/lodash.escape-4.0.1.tgz
Source3: https://registry.npmjs.org/lodash.mapvalues/-/lodash.mapvalues-4.6.0.tgz
Source4: https://registry.npmjs.org/leven/-/leven-2.1.0.tgz
Source5: https://registry.npmjs.org/classnames/-/classnames-2.2.6.tgz
Source6: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source7: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source8: https://registry.npmjs.org/gitdiff-parser/-/gitdiff-parser-0.1.2.tgz
Source9: https://registry.npmjs.org/lodash.findlastindex/-/lodash.findlastindex-4.6.0.tgz
Source10: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(classnames)) = 2.2.6
Provides: bundled(npm(gitdiff-parser)) = 0.1.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(leven)) = 2.1.0
Provides: bundled(npm(lodash.escape)) = 4.0.1
Provides: bundled(npm(lodash.findlastindex)) = 4.6.0
Provides: bundled(npm(lodash.mapvalues)) = 4.6.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(react-diff-view)) = 1.8.1
Provides: bundled(npm(warning)) = 4.0.2
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
%setup -T -q -a 10 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.css.map %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js.map %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/parse.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/parse.js.map %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Oct 31 2018 Ohad Levy <ohadlevy@gmail.com> 1.8.1-1
- Add nodejs-react-diff-view generated by npm2rpm using the bundle strategy

