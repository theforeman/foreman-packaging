%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name uglifyjs-webpack-plugin

Name: %{?scl_prefix}nodejs-uglifyjs-webpack-plugin
Version: 1.3.0
Release: 1%{?dist}
Summary: UglifyJS plugin for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack-contrib/uglifyjs-webpack-plugin
Source0: https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz
Source1: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-3.5.2.tgz
Source2: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source3: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz
Source4: https://registry.npmjs.org/bluebird/-/bluebird-3.7.2.tgz
Source5: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source6: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz
Source7: https://registry.npmjs.org/cacache/-/cacache-10.0.4.tgz
Source8: https://registry.npmjs.org/chownr/-/chownr-1.1.4.tgz
Source9: https://registry.npmjs.org/commander/-/commander-2.14.1.tgz
Source10: https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz
Source11: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source12: https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz
Source13: https://registry.npmjs.org/copy-concurrently/-/copy-concurrently-1.0.5.tgz
Source14: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz
Source15: https://registry.npmjs.org/cyclist/-/cyclist-1.0.2.tgz
Source16: https://registry.npmjs.org/duplexify/-/duplexify-3.7.1.tgz
Source17: https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.4.tgz
Source18: https://registry.npmjs.org/errno/-/errno-0.1.8.tgz
Source19: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source20: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source21: https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-1.0.0.tgz
Source22: https://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz
Source23: https://registry.npmjs.org/flush-write-stream/-/flush-write-stream-1.1.1.tgz
Source24: https://registry.npmjs.org/from2/-/from2-2.3.0.tgz
Source25: https://registry.npmjs.org/fs-write-stream-atomic/-/fs-write-stream-atomic-1.0.10.tgz
Source26: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source27: https://registry.npmjs.org/glob/-/glob-7.2.3.tgz
Source28: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source29: https://registry.npmjs.org/iferr/-/iferr-0.1.5.tgz
Source30: https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
Source31: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source32: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source33: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source34: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source35: https://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz
Source36: https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.5.tgz
Source37: https://registry.npmjs.org/make-dir/-/make-dir-1.3.0.tgz
Source38: https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz
Source39: https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz
Source40: https://registry.npmjs.org/mississippi/-/mississippi-2.0.0.tgz
Source41: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.6.tgz
Source42: https://registry.npmjs.org/move-concurrently/-/move-concurrently-1.0.1.tgz
Source43: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source44: https://registry.npmjs.org/p-limit/-/p-limit-1.3.0.tgz
Source45: https://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz
Source46: https://registry.npmjs.org/p-try/-/p-try-1.0.0.tgz
Source47: https://registry.npmjs.org/parallel-transform/-/parallel-transform-1.2.0.tgz
Source48: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source49: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source50: https://registry.npmjs.org/pify/-/pify-3.0.0.tgz
Source51: https://registry.npmjs.org/pkg-dir/-/pkg-dir-2.0.0.tgz
Source52: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source53: https://registry.npmjs.org/promise-inflight/-/promise-inflight-1.0.1.tgz
Source54: https://registry.npmjs.org/prr/-/prr-1.0.1.tgz
Source55: https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz
Source56: https://registry.npmjs.org/pump/-/pump-2.0.1.tgz
Source57: https://registry.npmjs.org/pumpify/-/pumpify-1.5.1.tgz
Source58: https://registry.npmjs.org/punycode/-/punycode-2.3.0.tgz
Source59: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz
Source60: https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz
Source61: https://registry.npmjs.org/run-queue/-/run-queue-1.0.3.tgz
Source62: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source63: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source64: https://registry.npmjs.org/schema-utils/-/schema-utils-0.4.7.tgz
Source65: https://registry.npmjs.org/serialize-javascript/-/serialize-javascript-1.9.1.tgz
Source66: https://registry.npmjs.org/source-list-map/-/source-list-map-2.0.1.tgz
Source67: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source68: https://registry.npmjs.org/ssri/-/ssri-5.3.0.tgz
Source69: https://registry.npmjs.org/stream-each/-/stream-each-1.2.3.tgz
Source70: https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.1.tgz
Source71: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source72: https://registry.npmjs.org/through2/-/through2-2.0.5.tgz
Source73: https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz
Source74: https://registry.npmjs.org/uglify-es/-/uglify-es-3.3.10.tgz
Source75: https://registry.npmjs.org/uglifyjs-webpack-plugin/-/uglifyjs-webpack-plugin-1.3.0.tgz
Source76: https://registry.npmjs.org/unique-filename/-/unique-filename-1.1.1.tgz
Source77: https://registry.npmjs.org/unique-slug/-/unique-slug-2.0.2.tgz
Source78: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source79: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source80: https://registry.npmjs.org/webpack-sources/-/webpack-sources-1.4.3.tgz
Source81: https://registry.npmjs.org/worker-farm/-/worker-farm-1.7.0.tgz
Source82: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source83: https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz
Source84: https://registry.npmjs.org/y18n/-/y18n-4.0.3.tgz
Source85: https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz
Source86: nodejs-uglifyjs-webpack-plugin-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(ajv)) = 6.12.6
Provides: bundled(npm(ajv-keywords)) = 3.5.2
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(balanced-match)) = 1.0.2
Provides: bundled(npm(bluebird)) = 3.7.2
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(buffer-from)) = 1.1.2
Provides: bundled(npm(cacache)) = 10.0.4
Provides: bundled(npm(chownr)) = 1.1.4
Provides: bundled(npm(commander)) = 2.14.1
Provides: bundled(npm(commondir)) = 1.0.1
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(concat-stream)) = 1.6.2
Provides: bundled(npm(copy-concurrently)) = 1.0.5
Provides: bundled(npm(core-util-is)) = 1.0.3
Provides: bundled(npm(cyclist)) = 1.0.2
Provides: bundled(npm(duplexify)) = 3.7.1
Provides: bundled(npm(end-of-stream)) = 1.4.4
Provides: bundled(npm(errno)) = 0.1.8
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(find-cache-dir)) = 1.0.0
Provides: bundled(npm(find-up)) = 2.1.0
Provides: bundled(npm(flush-write-stream)) = 1.1.1
Provides: bundled(npm(from2)) = 2.3.0
Provides: bundled(npm(fs-write-stream-atomic)) = 1.0.10
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(glob)) = 7.2.3
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(iferr)) = 0.1.5
Provides: bundled(npm(imurmurhash)) = 0.1.4
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(locate-path)) = 2.0.0
Provides: bundled(npm(lru-cache)) = 4.1.5
Provides: bundled(npm(make-dir)) = 1.3.0
Provides: bundled(npm(minimatch)) = 3.1.2
Provides: bundled(npm(minimist)) = 1.2.8
Provides: bundled(npm(mississippi)) = 2.0.0
Provides: bundled(npm(mkdirp)) = 0.5.6
Provides: bundled(npm(move-concurrently)) = 1.0.1
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(p-limit)) = 1.3.0
Provides: bundled(npm(p-locate)) = 2.0.0
Provides: bundled(npm(p-try)) = 1.0.0
Provides: bundled(npm(parallel-transform)) = 1.2.0
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(pify)) = 3.0.0
Provides: bundled(npm(pkg-dir)) = 2.0.0
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(promise-inflight)) = 1.0.1
Provides: bundled(npm(prr)) = 1.0.1
Provides: bundled(npm(pseudomap)) = 1.0.2
Provides: bundled(npm(pump)) = 2.0.1
Provides: bundled(npm(pumpify)) = 1.5.1
Provides: bundled(npm(punycode)) = 2.3.0
Provides: bundled(npm(readable-stream)) = 2.3.8
Provides: bundled(npm(rimraf)) = 2.7.1
Provides: bundled(npm(run-queue)) = 1.0.3
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(schema-utils)) = 0.4.7
Provides: bundled(npm(serialize-javascript)) = 1.9.1
Provides: bundled(npm(source-list-map)) = 2.0.1
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(ssri)) = 5.3.0
Provides: bundled(npm(stream-each)) = 1.2.3
Provides: bundled(npm(stream-shift)) = 1.0.1
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(through2)) = 2.0.5
Provides: bundled(npm(typedarray)) = 0.0.6
Provides: bundled(npm(uglify-es)) = 3.3.10
Provides: bundled(npm(uglifyjs-webpack-plugin)) = 1.3.0
Provides: bundled(npm(unique-filename)) = 1.1.1
Provides: bundled(npm(unique-slug)) = 2.0.2
Provides: bundled(npm(uri-js)) = 4.4.1
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(webpack-sources)) = 1.4.3
Provides: bundled(npm(worker-farm)) = 1.7.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(xtend)) = 4.0.2
Provides: bundled(npm(y18n)) = 4.0.3
Provides: bundled(npm(yallist)) = 2.1.2
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

%setup -T -q -a 86 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.3.0-1
- Update to 1.3.0

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.5-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.2.5-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.2.5-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.5-1
- Update to 1.2.5

* Thu Mar 08 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.2-1
- new bundled package created with add_npm_package.sh
