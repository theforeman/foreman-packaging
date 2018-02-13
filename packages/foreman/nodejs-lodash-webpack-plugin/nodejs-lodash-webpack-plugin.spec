%global npm_name lodash-webpack-plugin

Name: nodejs-%{npm_name}
Version: 0.11.4
Release: 1%{?dist}
Summary: Smaller modular Lodash builds
License: MIT
Source0: http://registry.npmjs.org/lodash-webpack-plugin/-/lodash-webpack-plugin-0.11.4.tgz
Source1: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source2: lodash-webpack-plugin-0.11.4-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(lodash-webpack-plugin) = 0.11.4
Provides: bundled-npm(lodash) = 4.17.4
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

%setup -T -q -a 2 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/lodash-webpack-plugin
cp -pfr LICENSE README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md LICENSE ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}


%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc README.md

%changelog
* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.11.4-1
- new package built with tito

