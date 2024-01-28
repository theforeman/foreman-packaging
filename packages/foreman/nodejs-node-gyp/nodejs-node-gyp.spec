%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name node-gyp

Name: %{?scl_prefix}nodejs-node-gyp
Version: 8.4.1
Release: 1%{?dist}
Summary: Node
License: MIT
Group: Development/Libraries
URL: https://github.com/nodejs/node-gyp#readme
Source0: https://registry.npmjs.org/@gar/promisify/-/promisify-1.1.3.tgz
Source1: https://registry.npmjs.org/@npmcli/fs/-/fs-1.1.1.tgz
Source2: https://registry.npmjs.org/@npmcli/move-file/-/move-file-1.1.2.tgz
Source3: https://registry.npmjs.org/@tootallnate/once/-/once-1.1.2.tgz
Source4: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source5: https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz
Source6: https://registry.npmjs.org/agentkeepalive/-/agentkeepalive-4.5.0.tgz
Source7: https://registry.npmjs.org/aggregate-error/-/aggregate-error-3.1.0.tgz
Source8: https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz
Source9: https://registry.npmjs.org/aproba/-/aproba-2.0.0.tgz
Source10: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-3.0.1.tgz
Source11: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz
Source12: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source13: https://registry.npmjs.org/cacache/-/cacache-15.3.0.tgz
Source14: https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz
Source15: https://registry.npmjs.org/clean-stack/-/clean-stack-2.2.0.tgz
Source16: https://registry.npmjs.org/color-support/-/color-support-1.1.3.tgz
Source17: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source18: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source19: https://registry.npmjs.org/debug/-/debug-4.3.4.tgz
Source20: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source21: https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz
Source22: https://registry.npmjs.org/encoding/-/encoding-0.1.13.tgz
Source23: https://registry.npmjs.org/env-paths/-/env-paths-2.2.1.tgz
Source24: https://registry.npmjs.org/err-code/-/err-code-2.0.3.tgz
Source25: https://registry.npmjs.org/fs-minipass/-/fs-minipass-2.1.0.tgz
Source26: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source27: https://registry.npmjs.org/gauge/-/gauge-4.0.4.tgz
Source28: https://registry.npmjs.org/glob/-/glob-7.2.3.tgz
Source29: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source30: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source31: https://registry.npmjs.org/http-cache-semantics/-/http-cache-semantics-4.1.1.tgz
Source32: https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-4.0.1.tgz
Source33: https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.1.tgz
Source34: https://registry.npmjs.org/humanize-ms/-/humanize-ms-1.2.1.tgz
Source35: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.6.3.tgz
Source36: https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
Source37: https://registry.npmjs.org/indent-string/-/indent-string-4.0.0.tgz
Source38: https://registry.npmjs.org/infer-owner/-/infer-owner-1.0.4.tgz
Source39: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source40: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source41: https://registry.npmjs.org/ip/-/ip-2.0.0.tgz
Source42: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz
Source43: https://registry.npmjs.org/is-lambda/-/is-lambda-1.0.1.tgz
Source44: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source45: https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz
Source46: https://registry.npmjs.org/make-fetch-happen/-/make-fetch-happen-9.1.0.tgz
Source47: https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz
Source48: https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz
Source49: https://registry.npmjs.org/minipass/-/minipass-5.0.0.tgz
Source50: https://registry.npmjs.org/minipass-collect/-/minipass-collect-1.0.2.tgz
Source51: https://registry.npmjs.org/minipass-fetch/-/minipass-fetch-1.4.1.tgz
Source52: https://registry.npmjs.org/minipass-flush/-/minipass-flush-1.0.5.tgz
Source53: https://registry.npmjs.org/minipass-pipeline/-/minipass-pipeline-1.2.4.tgz
Source54: https://registry.npmjs.org/minipass-sized/-/minipass-sized-1.0.3.tgz
Source55: https://registry.npmjs.org/minizlib/-/minizlib-2.1.2.tgz
Source56: https://registry.npmjs.org/mkdirp/-/mkdirp-1.0.4.tgz
Source57: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
Source58: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source59: https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz
Source60: https://registry.npmjs.org/node-gyp/-/node-gyp-8.4.1.tgz
Source61: https://registry.npmjs.org/nopt/-/nopt-5.0.0.tgz
Source62: https://registry.npmjs.org/npmlog/-/npmlog-6.0.2.tgz
Source63: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source64: https://registry.npmjs.org/p-map/-/p-map-4.0.0.tgz
Source65: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source66: https://registry.npmjs.org/promise-inflight/-/promise-inflight-1.0.1.tgz
Source67: https://registry.npmjs.org/promise-retry/-/promise-retry-2.0.1.tgz
Source68: https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz
Source69: https://registry.npmjs.org/retry/-/retry-0.12.0.tgz
Source70: https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz
Source71: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source72: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source73: https://registry.npmjs.org/semver/-/semver-7.5.4.tgz
Source74: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source75: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz
Source76: https://registry.npmjs.org/smart-buffer/-/smart-buffer-4.2.0.tgz
Source77: https://registry.npmjs.org/socks/-/socks-2.7.1.tgz
Source78: https://registry.npmjs.org/socks-proxy-agent/-/socks-proxy-agent-6.2.1.tgz
Source79: https://registry.npmjs.org/ssri/-/ssri-8.0.1.tgz
Source80: https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz
Source81: https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz
Source82: https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz
Source83: https://registry.npmjs.org/tar/-/tar-6.2.0.tgz
Source84: https://registry.npmjs.org/unique-filename/-/unique-filename-1.1.1.tgz
Source85: https://registry.npmjs.org/unique-slug/-/unique-slug-2.0.2.tgz
Source86: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source87: https://registry.npmjs.org/which/-/which-2.0.2.tgz
Source88: https://registry.npmjs.org/wide-align/-/wide-align-1.1.5.tgz
Source89: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source90: https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz
Source91: nodejs-node-gyp-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@gar/promisify)) = 1.1.3
Provides: bundled(npm(@npmcli/fs)) = 1.1.1
Provides: bundled(npm(@npmcli/move-file)) = 1.1.2
Provides: bundled(npm(@tootallnate/once)) = 1.1.2
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(agent-base)) = 6.0.2
Provides: bundled(npm(agentkeepalive)) = 4.5.0
Provides: bundled(npm(aggregate-error)) = 3.1.0
Provides: bundled(npm(ansi-regex)) = 5.0.1
Provides: bundled(npm(aproba)) = 2.0.0
Provides: bundled(npm(are-we-there-yet)) = 3.0.1
Provides: bundled(npm(balanced-match)) = 1.0.2
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(cacache)) = 15.3.0
Provides: bundled(npm(chownr)) = 2.0.0
Provides: bundled(npm(clean-stack)) = 2.2.0
Provides: bundled(npm(color-support)) = 1.1.3
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(debug)) = 4.3.4
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(emoji-regex)) = 8.0.0
Provides: bundled(npm(encoding)) = 0.1.13
Provides: bundled(npm(env-paths)) = 2.2.1
Provides: bundled(npm(err-code)) = 2.0.3
Provides: bundled(npm(fs-minipass)) = 2.1.0
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(gauge)) = 4.0.4
Provides: bundled(npm(glob)) = 7.2.3
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(http-cache-semantics)) = 4.1.1
Provides: bundled(npm(http-proxy-agent)) = 4.0.1
Provides: bundled(npm(https-proxy-agent)) = 5.0.1
Provides: bundled(npm(humanize-ms)) = 1.2.1
Provides: bundled(npm(iconv-lite)) = 0.6.3
Provides: bundled(npm(imurmurhash)) = 0.1.4
Provides: bundled(npm(indent-string)) = 4.0.0
Provides: bundled(npm(infer-owner)) = 1.0.4
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(ip)) = 2.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 3.0.0
Provides: bundled(npm(is-lambda)) = 1.0.1
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(lru-cache)) = 6.0.0
Provides: bundled(npm(make-fetch-happen)) = 9.1.0
Provides: bundled(npm(minimatch)) = 3.1.2
Provides: bundled(npm(minipass)) = 3.3.6
Provides: bundled(npm(minipass)) = 5.0.0
Provides: bundled(npm(minipass-collect)) = 1.0.2
Provides: bundled(npm(minipass-fetch)) = 1.4.1
Provides: bundled(npm(minipass-flush)) = 1.0.5
Provides: bundled(npm(minipass-pipeline)) = 1.2.4
Provides: bundled(npm(minipass-sized)) = 1.0.3
Provides: bundled(npm(minizlib)) = 2.1.2
Provides: bundled(npm(mkdirp)) = 1.0.4
Provides: bundled(npm(ms)) = 2.1.2
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(negotiator)) = 0.6.3
Provides: bundled(npm(node-gyp)) = 8.4.1
Provides: bundled(npm(nopt)) = 5.0.0
Provides: bundled(npm(npmlog)) = 6.0.2
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(p-map)) = 4.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(promise-inflight)) = 1.0.1
Provides: bundled(npm(promise-retry)) = 2.0.1
Provides: bundled(npm(readable-stream)) = 3.6.2
Provides: bundled(npm(retry)) = 0.12.0
Provides: bundled(npm(rimraf)) = 3.0.2
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(semver)) = 7.5.4
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(signal-exit)) = 3.0.7
Provides: bundled(npm(smart-buffer)) = 4.2.0
Provides: bundled(npm(socks)) = 2.7.1
Provides: bundled(npm(socks-proxy-agent)) = 6.2.1
Provides: bundled(npm(ssri)) = 8.0.1
Provides: bundled(npm(string_decoder)) = 1.3.0
Provides: bundled(npm(string-width)) = 4.2.3
Provides: bundled(npm(strip-ansi)) = 6.0.1
Provides: bundled(npm(tar)) = 6.2.0
Provides: bundled(npm(unique-filename)) = 1.1.1
Provides: bundled(npm(unique-slug)) = 2.0.2
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(which)) = 2.0.2
Provides: bundled(npm(wide-align)) = 1.1.5
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(yallist)) = 4.0.0
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

%setup -T -q -a 91 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/addon.gypi %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/gyp %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/macOS_Catalina_acid_test.sh %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/test %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/update-gyp.py %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/node-gyp.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/node-gyp.js %{buildroot}%{_bindir}/node-gyp

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/node-gyp
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/CONTRIBUTING.md
%doc node_modules/%{npm_name}/README.md
%doc node_modules/%{npm_name}/docs
%doc node_modules/%{npm_name}/macOS_Catalina.md

%changelog
* Sun Jan 28 2024 Foreman Packaging Automation <packaging@theforeman.org> 8.4.1-1
- Update to 8.4.1

* Wed Aug 02 2023 Eric D. Helms <ericdhelms@gmail.com> 6.1.0-10
- Drop SCL from nodejs-node-gyp spec

* Wed Apr 1 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-9
- Update patch more

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-8
- Update patch more

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-7
- Update patch

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-6
- Update patching logic

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-5
- fix addon.gypi

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-4
- fix patch usage

* Fri Mar 27 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-3
- update patch usage

* Wed Mar 25 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-2
- update to use more recent spec changes

* Wed Mar 25 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-1
- Add nodejs-node-gyp generated by npm2rpm using the bundle strategy
