%global homedir %{_datadir}/%{name}
%global confdir extras/packaging/rpm/sources
%global foreman_rake %{_sbindir}/%{name}-rake
%global executor_service_name dynflowd

# explicitly define, as we build on top of an scl, not inside with scl_package
%{?scl:%global scl_prefix %{scl}-}
%global scl_ruby_bin /usr/bin/%{?scl:%{scl_prefix}}ruby
%global scl_rake /usr/bin/%{?scl:%{scl_prefix}}rake

%global release 2

Name:    foreman
Version: 1.20.1
Release: %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?dist}
Summary: Systems Management web application

Group:  Applications/System
License: GPLv3+ with exceptions
URL: https://theforeman.org
Source0: https://downloads.theforeman.org/%{name}/%{name}-%{version}%{?prerelease:-}%{?prerelease}.tar.bz2
Source1: %{name}.service
Source2: %{name}.sysconfig
Source3: %{name}.logrotate
Source4: %{name}.cron.d
Source5: %{name}.tmpfiles
Source6: %{name}.attr
Source7: %{name}.provreq
Source10: %{executor_service_name}.sysconfig
Source11: %{executor_service_name}.service
BuildArch:  noarch

Conflicts: foreman-tasks < 0.11.0-2
Conflicts: foreman-release-scl < 7-1

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygem(rake) >= 0.8.3
Requires: %{?scl_prefix_ruby}rubygem(rdoc)
Requires: %{?scl_prefix}rubygem(bundler_ext)
%if 0%{?scl:1}
Requires: %{scl}-runtime >= 5
Requires: %{scl}-runtime < 6
%endif

Requires: wget
Requires: /etc/cron.d
Requires(pre):  shadow-utils
Requires(post): chkconfig
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): chkconfig
Requires(preun): systemd-units

# Subpackages
Requires: %{name}-debug

# start specfile main Requires
Requires: %{?scl_prefix_ror}rubygem(rails) = 5.2.1
Requires: %{?scl_prefix}rubygem(rest-client) >= 2.0.0
Requires: %{?scl_prefix}rubygem(rest-client) < 3
Requires: %{?scl_prefix}rubygem(audited) >= 4.7.1
Requires: %{?scl_prefix}rubygem(audited) < 5
Requires: %{?scl_prefix}rubygem(will_paginate) >= 3.0
Requires: %{?scl_prefix}rubygem(will_paginate) < 4.0
Requires: %{?scl_prefix}rubygem(ancestry) >= 2.0
Requires: %{?scl_prefix}rubygem(ancestry) < 4
Requires: %{?scl_prefix}rubygem(scoped_search) >= 4.1.3
Requires: %{?scl_prefix}rubygem(scoped_search) < 5
Requires: %{?scl_prefix}rubygem(ldap_fluff) >= 0.4.7
Requires: %{?scl_prefix}rubygem(ldap_fluff) < 1.0
Requires: %{?scl_prefix}rubygem(apipie-rails) >= 0.5.2
Requires: %{?scl_prefix}rubygem(apipie-rails) < 0.6.0
Requires: %{?scl_prefix}rubygem(rabl) >= 0.11
Requires: %{?scl_prefix}rubygem(rabl) < 1.0
Requires: %{?scl_prefix}rubygem(oauth) >= 0.5.4
Requires: %{?scl_prefix}rubygem(oauth) < 1
Requires: %{?scl_prefix}rubygem(deep_cloneable) >= 2.3.2
Requires: %{?scl_prefix}rubygem(deep_cloneable) < 3.0
Requires: %{?scl_prefix}rubygem(validates_lengths_from_database) >= 0.5
Requires: %{?scl_prefix}rubygem(validates_lengths_from_database) < 1.0
Requires: %{?scl_prefix}rubygem(friendly_id) >= 5.2.4
Requires: %{?scl_prefix}rubygem(friendly_id) < 6
Requires: %{?scl_prefix}rubygem(secure_headers) >= 6.0
Requires: %{?scl_prefix}rubygem(secure_headers) < 7.0
Requires: %{?scl_prefix}rubygem(safemode) >= 1.3.5
Requires: %{?scl_prefix}rubygem(safemode) < 2
Requires: %{?scl_prefix}rubygem(fast_gettext) >= 1.4
Requires: %{?scl_prefix}rubygem(fast_gettext) < 2.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails) >= 1.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails) < 2.0
Requires: %{?scl_prefix}rubygem(rails-i18n) >= 5.0
Requires: %{?scl_prefix}rubygem(rails-i18n) < 6.0
Requires: %{?scl_prefix_ror}rubygem(turbolinks) >= 2.5.4
Requires: %{?scl_prefix_ror}rubygem(turbolinks) < 3
Requires: %{?scl_prefix}rubygem(logging) >= 1.8.0
Requires: %{?scl_prefix}rubygem(logging) < 3.0.0
Requires: %{?scl_prefix}rubygem(fog-core) = 1.45.0
Requires: %{?scl_prefix}rubygem(net-scp)
Requires: %{?scl_prefix}rubygem(net-ssh)
Requires: %{?scl_prefix}rubygem(net-ldap) >= 0.8.0
Requires: %{?scl_prefix}rubygem(net-ping)
Requires: %{?scl_prefix}rubygem(activerecord-session_store) >= 1.1.0
Requires: %{?scl_prefix}rubygem(activerecord-session_store) < 2
Requires: %{?scl_prefix_ror}rubygem(sprockets) >= 3
Requires: %{?scl_prefix_ror}rubygem(sprockets) < 4.0
Requires: %{?scl_prefix_ror}rubygem(sprockets-rails) >= 3.0
Requires: %{?scl_prefix_ror}rubygem(sprockets-rails) < 4.0
Requires: %{?scl_prefix}rubygem(record_tag_helper) >= 1.0
Requires: %{?scl_prefix}rubygem(record_tag_helper) < 2.0
Requires: %{?scl_prefix}rubygem(responders) >= 2.0
Requires: %{?scl_prefix}rubygem(responders) < 3.0
Requires: %{?scl_prefix}rubygem(roadie-rails) >= 1.1
Requires: %{?scl_prefix}rubygem(roadie-rails) < 2.0
Requires: %{?scl_prefix}rubygem(x-editable-rails) >= 1.5.5
Requires: %{?scl_prefix}rubygem(x-editable-rails) < 1.6.0
Requires: %{?scl_prefix}rubygem(deacon) >= 1.0
Requires: %{?scl_prefix}rubygem(deacon) < 2.0
Requires: %{?scl_prefix}rubygem(webpack-rails) >= 0.9.8
Requires: %{?scl_prefix}rubygem(webpack-rails) < 0.10.0
Requires: %{?scl_prefix_ror}rubygem(mail) >= 2.7
Requires: %{?scl_prefix_ror}rubygem(mail) < 3.0
Requires: %{?scl_prefix}rubygem(sshkey) >= 1.9
Requires: %{?scl_prefix}rubygem(sshkey) < 2.0
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.0.0
Requires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
Requires: %{?scl_prefix}rubygem(daemons)
Requires: %{?scl_prefix}rubygem(get_process_mem)
# end specfile main Requires

# start specfile facter Requires
Requires: %{?scl_prefix}rubygem(facter)
# end specfile facter Requires

# start specfile jsonp Requires
Requires: %{?scl_prefix}rubygem(rack-jsonp)
# end specfile jsonp Requires

# Build dependencies
%{?systemd_requires}
BuildRequires: gettext
BuildRequires: asciidoc
BuildRequires: %{scl_ruby_bin}
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygem(rake) >= 0.8.3
BuildRequires: %{?scl_prefix_ruby}rubygem(rdoc)
BuildRequires: %{?scl_prefix}rubygem(bundler_ext)
# start specfile sqlite BuildRequires
BuildRequires: %{?scl_prefix_ror}rubygem(sqlite3) >= 1.3.6
BuildRequires: %{?scl_prefix_ror}rubygem(sqlite3) < 1.4.0
# end specfile sqlite BuildRequires

# start specfile main BuildRequires
BuildRequires: %{?scl_prefix_ror}rubygem(rails) = 5.2.1
BuildRequires: %{?scl_prefix}rubygem(rest-client) >= 2.0.0
BuildRequires: %{?scl_prefix}rubygem(rest-client) < 3
BuildRequires: %{?scl_prefix}rubygem(audited) >= 4.7.1
BuildRequires: %{?scl_prefix}rubygem(audited) < 5
BuildRequires: %{?scl_prefix}rubygem(will_paginate) >= 3.0
BuildRequires: %{?scl_prefix}rubygem(will_paginate) < 4.0
BuildRequires: %{?scl_prefix}rubygem(ancestry) >= 2.0
BuildRequires: %{?scl_prefix}rubygem(ancestry) < 4
BuildRequires: %{?scl_prefix}rubygem(scoped_search) >= 4.1.3
BuildRequires: %{?scl_prefix}rubygem(scoped_search) < 5
BuildRequires: %{?scl_prefix}rubygem(ldap_fluff) >= 0.4.7
BuildRequires: %{?scl_prefix}rubygem(ldap_fluff) < 1.0
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) >= 0.5.2
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) < 0.6.0
BuildRequires: %{?scl_prefix}rubygem(rabl) >= 0.11
BuildRequires: %{?scl_prefix}rubygem(rabl) < 1.0
BuildRequires: %{?scl_prefix}rubygem(oauth) >= 0.5.4
BuildRequires: %{?scl_prefix}rubygem(oauth) < 1
BuildRequires: %{?scl_prefix}rubygem(deep_cloneable) >= 2.3.2
BuildRequires: %{?scl_prefix}rubygem(deep_cloneable) < 3.0
BuildRequires: %{?scl_prefix}rubygem(validates_lengths_from_database) >= 0.5
BuildRequires: %{?scl_prefix}rubygem(validates_lengths_from_database) < 1.0
BuildRequires: %{?scl_prefix}rubygem(friendly_id) >= 5.2.4
BuildRequires: %{?scl_prefix}rubygem(friendly_id) < 6
BuildRequires: %{?scl_prefix}rubygem(secure_headers) >= 6.0
BuildRequires: %{?scl_prefix}rubygem(secure_headers) < 7.0
BuildRequires: %{?scl_prefix}rubygem(safemode) >= 1.3.5
BuildRequires: %{?scl_prefix}rubygem(safemode) < 2
BuildRequires: %{?scl_prefix}rubygem(fast_gettext) >= 1.4
BuildRequires: %{?scl_prefix}rubygem(fast_gettext) < 2.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails) < 2.0
BuildRequires: %{?scl_prefix}rubygem(rails-i18n) >= 5.0
BuildRequires: %{?scl_prefix}rubygem(rails-i18n) < 6.0
BuildRequires: %{?scl_prefix_ror}rubygem(turbolinks) >= 2.5.4
BuildRequires: %{?scl_prefix_ror}rubygem(turbolinks) < 3
BuildRequires: %{?scl_prefix}rubygem(logging) >= 1.8.0
BuildRequires: %{?scl_prefix}rubygem(logging) < 3.0.0
BuildRequires: %{?scl_prefix}rubygem(fog-core) = 1.45.0
BuildRequires: %{?scl_prefix}rubygem(net-scp)
BuildRequires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix}rubygem(net-ldap) >= 0.8.0
BuildRequires: %{?scl_prefix}rubygem(net-ping)
BuildRequires: %{?scl_prefix}rubygem(activerecord-session_store) >= 1.1.0
BuildRequires: %{?scl_prefix}rubygem(activerecord-session_store) < 2
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets) >= 3
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets) < 4.0
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets-rails) >= 3.0
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets-rails) < 4.0
BuildRequires: %{?scl_prefix}rubygem(record_tag_helper) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(record_tag_helper) < 2.0
BuildRequires: %{?scl_prefix}rubygem(responders) >= 2.0
BuildRequires: %{?scl_prefix}rubygem(responders) < 3.0
BuildRequires: %{?scl_prefix}rubygem(roadie-rails) >= 1.1
BuildRequires: %{?scl_prefix}rubygem(roadie-rails) < 2.0
BuildRequires: %{?scl_prefix}rubygem(x-editable-rails) >= 1.5.5
BuildRequires: %{?scl_prefix}rubygem(x-editable-rails) < 1.6.0
BuildRequires: %{?scl_prefix}rubygem(deacon) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(deacon) < 2.0
BuildRequires: %{?scl_prefix}rubygem(webpack-rails) >= 0.9.8
BuildRequires: %{?scl_prefix}rubygem(webpack-rails) < 0.10.0
BuildRequires: %{?scl_prefix_ror}rubygem(mail) >= 2.7
BuildRequires: %{?scl_prefix_ror}rubygem(mail) < 3.0
BuildRequires: %{?scl_prefix}rubygem(sshkey) >= 1.9
BuildRequires: %{?scl_prefix}rubygem(sshkey) < 2.0
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.0.0
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(daemons)
BuildRequires: %{?scl_prefix}rubygem(get_process_mem)
# end specfile main BuildRequires

# assets
%if 0%{?scl:1}
BuildRequires: %{scl}-runtime-assets >= 5
BuildRequires: %{scl}-runtime-assets < 6
%endif
BuildRequires: nodejs >= 6.10
BuildRequires: http-parser
# Temporary dep on libuv until https://bugs.centos.org/view.php?id=10606
# is resolved
BuildRequires: libuv
BuildRequires: nodejs-packaging
BuildRequires: systemd

# start package.json devDependencies BuildRequires
#BuildRequires: npm(@storybook/addon-actions) >= 3.2.12
#BuildRequires: npm(@storybook/addon-actions) < 4.0.0
#BuildRequires: npm(@storybook/addon-knobs) >= 3.4.3
#BuildRequires: npm(@storybook/addon-knobs) < 4.0.0
#BuildRequires: npm(@storybook/react) >= 3.2.12
#BuildRequires: npm(@storybook/react) < 4.0.0
#BuildRequires: npm(@storybook/storybook-deployer) >= 2.0.0
#BuildRequires: npm(@storybook/storybook-deployer) < 3.0.0
#BuildRequires: npm(axios-mock-adapter) >= 1.10.0
#BuildRequires: npm(axios-mock-adapter) < 2.0.0
BuildRequires: npm(babel-cli) >= 6.10.1
BuildRequires: npm(babel-cli) < 7.0.0
BuildRequires: npm(babel-core) >= 6.26.3
BuildRequires: npm(babel-core) < 7.0.0
#BuildRequires: npm(babel-eslint) >= 6.1.2
#BuildRequires: npm(babel-eslint) < 7.0.0
#BuildRequires: npm(babel-jest) >= 15.0.0
#BuildRequires: npm(babel-jest) < 16.0.0
BuildRequires: npm(babel-loader) >= 7.1.1
BuildRequires: npm(babel-loader) < 8.0.0
BuildRequires: npm(babel-plugin-lodash) >= 3.3.4
BuildRequires: npm(babel-plugin-lodash) < 4.0.0
BuildRequires: npm(babel-plugin-transform-class-properties) >= 6.24.1
BuildRequires: npm(babel-plugin-transform-class-properties) < 7.0.0
BuildRequires: npm(babel-plugin-transform-object-assign) >= 6.8.0
BuildRequires: npm(babel-plugin-transform-object-assign) < 7.0.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) >= 6.8.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) < 7.0.0
BuildRequires: npm(babel-preset-env) >= 1.7.0
BuildRequires: npm(babel-preset-env) < 2.0.0
BuildRequires: npm(babel-preset-react) >= 6.5.0
BuildRequires: npm(babel-preset-react) < 7.0.0
BuildRequires: npm(babel-register) >= 6.9.0
BuildRequires: npm(babel-register) < 7.0.0
BuildRequires: npm(compression-webpack-plugin) >= 1.1.11
BuildRequires: npm(compression-webpack-plugin) < 1.2.0
#BuildRequires: npm(coveralls) >= 3.0.0
#BuildRequires: npm(coveralls) < 4.0.0
BuildRequires: npm(css-loader) >= 0.23.1
BuildRequires: npm(css-loader) < 1.0.0
BuildRequires: npm(dotenv) >= 5.0.0
BuildRequires: npm(dotenv) < 6.0.0
#BuildRequires: npm(enzyme) >= 3.4.0
#BuildRequires: npm(enzyme) < 4.0.0
#BuildRequires: npm(enzyme-adapter-react-16) >= 1.4.0
#BuildRequires: npm(enzyme-adapter-react-16) < 2.0.0
#BuildRequires: npm(enzyme-to-json) >= 3.2.1
#BuildRequires: npm(enzyme-to-json) < 4.0.0
#BuildRequires: npm(eslint) >= 4.10.0
#BuildRequires: npm(eslint) < 5.0.0
#BuildRequires: npm(eslint-config-airbnb-base) >= 12.1.0
#BuildRequires: npm(eslint-config-airbnb-base) < 13.0.0
#BuildRequires: npm(eslint-plugin-import) >= 2.8.0
#BuildRequires: npm(eslint-plugin-import) < 3.0.0
#BuildRequires: npm(eslint-plugin-react) >= 7.4.0
#BuildRequires: npm(eslint-plugin-react) < 8.0.0
BuildRequires: npm(expose-loader) >= 0.6.0
BuildRequires: npm(expose-loader) < 0.7.0
BuildRequires: npm(extract-text-webpack-plugin) >= 3.0.0
BuildRequires: npm(extract-text-webpack-plugin) < 4.0.0
BuildRequires: npm(file-loader) >= 0.9.0
BuildRequires: npm(file-loader) < 1.0.0
#BuildRequires: npm(highlight.js) >= 9.12.0
#BuildRequires: npm(highlight.js) < 10.0.0
BuildRequires: npm(identity-obj-proxy) >= 3.0.0
BuildRequires: npm(identity-obj-proxy) < 4.0.0
#BuildRequires: npm(jest-cli) >= 20.0.0
#BuildRequires: npm(jest-cli) < 21.0.0
BuildRequires: npm(jsdom) >= 9.5.0
BuildRequires: npm(jsdom) < 10.0.0
BuildRequires: npm(lodash-webpack-plugin) >= 0.11.4
BuildRequires: npm(lodash-webpack-plugin) < 1.0.0
BuildRequires: npm(node-sass) >= 4.5.0
BuildRequires: npm(node-sass) < 5.0.0
BuildRequires: npm(raf) >= 3.4.0
BuildRequires: npm(raf) < 4.0.0
#BuildRequires: npm(raw-loader) >= 0.5.1
#BuildRequires: npm(raw-loader) < 1.0.0
#BuildRequires: npm(react-remarkable) >= 1.1.3
#BuildRequires: npm(react-remarkable) < 2.0.0
#BuildRequires: npm(react-test-renderer) >= 16.2.0
#BuildRequires: npm(react-test-renderer) < 17.0.0
#BuildRequires: npm(redux-mock-store) >= 1.2.2
#BuildRequires: npm(redux-mock-store) < 2.0.0
BuildRequires: npm(sass-loader) >= 6.0.6
BuildRequires: npm(sass-loader) < 6.1.0
BuildRequires: npm(style-loader) >= 0.13.1
BuildRequires: npm(style-loader) < 1.0.0
#BuildRequires: npm(stylelint) >= 9.3.0
#BuildRequires: npm(stylelint) < 10.0.0
#BuildRequires: npm(stylelint-config-standard) >= 18.0.0
#BuildRequires: npm(stylelint-config-standard) < 19.0.0
BuildRequires: npm(uglifyjs-webpack-plugin) >= 1.2.2
BuildRequires: npm(uglifyjs-webpack-plugin) < 2.0.0
BuildRequires: npm(url-loader) >= 1.0.1
BuildRequires: npm(url-loader) < 2.0.0
BuildRequires: npm(webpack) >= 3.4.1
BuildRequires: npm(webpack) < 4.0.0
#BuildRequires: npm(webpack-bundle-analyzer) >= 2.13.1
#BuildRequires: npm(webpack-bundle-analyzer) < 3.0.0
#BuildRequires: npm(webpack-dev-server) >= 2.5.1
#BuildRequires: npm(webpack-dev-server) < 3.0.0
BuildRequires: npm(webpack-stats-plugin) >= 0.1.5
BuildRequires: npm(webpack-stats-plugin) < 1.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: npm(@novnc/novnc) >= 1.0.0
BuildRequires: npm(@novnc/novnc) < 2.0.0
BuildRequires: npm(axios) >= 0.17.1
BuildRequires: npm(axios) < 1.0.0
BuildRequires: npm(babel-polyfill) >= 6.26.0
BuildRequires: npm(babel-polyfill) < 7.0.0
BuildRequires: npm(bootstrap-sass) >= 3.3.7
BuildRequires: npm(bootstrap-sass) < 4.0.0
BuildRequires: npm(brace) >= 0.10.0
BuildRequires: npm(brace) < 1.0.0
BuildRequires: npm(classnames) >= 2.2.5
BuildRequires: npm(classnames) < 3.0.0
BuildRequires: npm(datatables.net) >= 1.10.12
BuildRequires: npm(datatables.net) < 1.11.0
BuildRequires: npm(datatables.net-bs) >= 1.10.12
BuildRequires: npm(datatables.net-bs) < 1.11.0
BuildRequires: npm(diff) >= 3.0.0
BuildRequires: npm(diff) < 3.1.0
BuildRequires: npm(ipaddr.js) >= 1.2.0
BuildRequires: npm(ipaddr.js) < 1.3.0
BuildRequires: npm(isomorphic-fetch) >= 2.2.1
BuildRequires: npm(isomorphic-fetch) < 3.0.0
BuildRequires: npm(jed) >= 1.1.1
BuildRequires: npm(jed) < 2.0.0
BuildRequires: npm(jquery) >= 2.2.4
BuildRequires: npm(jquery) < 2.3.0
BuildRequires: npm(jquery-flot) >= 0.8.3
BuildRequires: npm(jquery-flot) < 0.9.0
BuildRequires: npm(jquery-ujs) >= 1.2.0
BuildRequires: npm(jquery-ujs) < 1.3.0
BuildRequires: npm(jquery.cookie) >= 1.4.1
BuildRequires: npm(jquery.cookie) < 1.5.0
BuildRequires: npm(jstz) >= 1.0.7
BuildRequires: npm(jstz) < 1.1.0
BuildRequires: npm(lodash) >= 4.17.10
BuildRequires: npm(lodash) < 5.0.0
BuildRequires: npm(multiselect) >= 0.9.12
BuildRequires: npm(multiselect) < 0.10.0
BuildRequires: npm(patternfly) >= 3.42.0
BuildRequires: npm(patternfly) < 4.0.0
BuildRequires: npm(patternfly-react) >= 2.19.1
BuildRequires: npm(patternfly-react) < 3.0.0
BuildRequires: npm(prop-types) >= 15.6.0
BuildRequires: npm(prop-types) < 16.0.0
BuildRequires: npm(react) >= 16.4.0
BuildRequires: npm(react) < 17.0.0
BuildRequires: npm(react-bootstrap) = 0.32.1
BuildRequires: npm(react-debounce-input) >= 3.2.0
BuildRequires: npm(react-debounce-input) < 4.0.0
BuildRequires: npm(react-dom) >= 16.4.0
BuildRequires: npm(react-dom) < 17.0.0
BuildRequires: npm(react-ellipsis-with-tooltip) >= 1.0.8
BuildRequires: npm(react-ellipsis-with-tooltip) < 2.0.0
BuildRequires: npm(react-numeric-input) >= 2.0.7
BuildRequires: npm(react-numeric-input) < 3.0.0
BuildRequires: npm(react-onclickoutside) >= 6.6.2
BuildRequires: npm(react-onclickoutside) < 7.0.0
BuildRequires: npm(react-password-strength) >= 2.1.0
BuildRequires: npm(react-password-strength) < 3.0.0
BuildRequires: npm(react-redux) >= 5.0.6
BuildRequires: npm(react-redux) < 6.0.0
BuildRequires: npm(redux) >= 3.6.0
BuildRequires: npm(redux) < 4.0.0
BuildRequires: npm(redux-form) = 7.2.0
BuildRequires: npm(redux-form-validators) >= 2.1.2
BuildRequires: npm(redux-form-validators) < 3.0.0
BuildRequires: npm(redux-logger) >= 2.8.1
BuildRequires: npm(redux-logger) < 3.0.0
BuildRequires: npm(redux-thunk) >= 2.2.0
BuildRequires: npm(redux-thunk) < 3.0.0
BuildRequires: npm(reselect) >= 3.0.1
BuildRequires: npm(reselect) < 4.0.0
BuildRequires: npm(seamless-immutable) >= 7.1.2
BuildRequires: npm(seamless-immutable) < 8.0.0
BuildRequires: npm(select2) >= 3.5.2
BuildRequires: npm(select2) < 3.6.0
BuildRequires: npm(urijs) >= 1.18.10
BuildRequires: npm(urijs) < 2.0.0
BuildRequires: npm(uuid) >= 3.0.1
BuildRequires: npm(uuid) < 4.0.0
# end package.json dependencies BuildRequires

# start specfile assets BuildRequires
BuildRequires: %{?scl_prefix_ror}rubygem(jquery-turbolinks) >= 2.1
BuildRequires: %{?scl_prefix_ror}rubygem(jquery-turbolinks) < 3.0
BuildRequires: %{?scl_prefix}rubygem(jquery-ui-rails) < 5.0.0
BuildRequires: %{?scl_prefix}rubygem(patternfly-sass) >= 3.32.1
BuildRequires: %{?scl_prefix}rubygem(patternfly-sass) < 3.38.0
BuildRequires: %{?scl_prefix}rubygem(gridster-rails) >= 0.5
BuildRequires: %{?scl_prefix}rubygem(gridster-rails) < 1.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) < 2.0
BuildRequires: %{?scl_prefix_ror}rubygem(execjs) >= 1.4.0
BuildRequires: %{?scl_prefix_ror}rubygem(execjs) < 3.0
BuildRequires: %{?scl_prefix_ror}rubygem(uglifier) >= 1.0.3
BuildRequires: %{?scl_prefix_ror}rubygem(sass-rails) >= 5.0
BuildRequires: %{?scl_prefix_ror}rubygem(sass-rails) < 6.0
BuildRequires: %{?scl_prefix}rubygem(spice-html5-rails) >= 0.1.5
BuildRequires: %{?scl_prefix}rubygem(spice-html5-rails) < 0.2.0
# end specfile assets BuildRequires

# start specfile facter BuildRequires
BuildRequires: %{?scl_prefix}rubygem(facter)
# end specfile facter BuildRequires

%package cli
Summary: Foreman CLI
Group: Applications/System
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman)

%description cli
Meta Package to install hammer rubygems and its dependencies

%files cli

%package debug
Summary: Foreman debug utilities
Group: Applications/System
Requires: rsync

%description debug
Useful utilities for debug info collection

%files debug
%{_sbindir}/%{name}-debug
%{_datadir}/%{name}/script/%{name}-debug.d

%package libvirt
Summary: Foreman libvirt support
Group:  Applications/System
# start specfile libvirt Requires
Requires: %{?scl_prefix}rubygem(fog-libvirt) >= 0.4.1
Requires: %{?scl_prefix}rubygem(fog-libvirt) < 1.0
Requires: %{?scl_prefix}rubygem(ruby-libvirt) >= 0.5
Requires: %{?scl_prefix}rubygem(ruby-libvirt) < 1.0
# end specfile libvirt Requires
Requires: %{name} = %{version}-%{release}
Requires: genisoimage
Obsoletes: foreman-virt < 1.0.0
Provides: foreman-virt = 1.0.0

%description libvirt
Meta package to install requirements for libvirt compute resource support.

%files libvirt
%{_datadir}/%{name}/bundler.d/libvirt.rb

%package openstack
Summary: Foreman OpenStack support
Group:  Applications/System
# start specfile openstack Requires
Requires: %{?scl_prefix}rubygem(fog-openstack) >= 0.1.25
Requires: %{?scl_prefix}rubygem(fog-openstack) < 1.0
# end specfile openstack Requires
Requires: %{name} = %{version}-%{release}

%description openstack
Meta package to install requirements for OpenStack compute resource support.

%files openstack
%{_datadir}/%{name}/bundler.d/openstack.rb

%package ovirt
Summary: Foreman oVirt support
Group:  Applications/System
# start specfile ovirt Requires
Requires: %{?scl_prefix}rubygem(fog-ovirt) >= 1.1.2
Requires: %{?scl_prefix}rubygem(fog-ovirt) < 1.2.0
# end specfile ovirt Requires
Requires: foreman-compute = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description ovirt
Meta package to install requirements for oVirt compute resource support.

%files ovirt
%{_datadir}/%{name}/bundler.d/ovirt.rb

%package compute
Summary: Foreman compute resource Fog dependencies
Group:  Applications/System
# start specfile fog Requires
Requires: %{?scl_prefix}rubygem(fog) = 1.42.1
# end specfile fog Requires
Requires: %{name} = %{version}-%{release}
Obsoletes: foreman-compute < 1.8.0
Obsoletes: foreman-fog < 1.0.0
Provides: foreman-fog = 1.0.0
Obsoletes: foreman-ec2 < 1.3.0

%description compute
Meta package to install dependencies to support some compute resources. Most
compute resources have a more specific package which should be installed in
preference to this package.

%files compute
%{_datadir}/%{name}/bundler.d/fog.rb

%package ec2
Summary:   Foreman Amazon Web Services (AWS) EC2 support
Group:     Applications/System
# start specfile ec2 Requires
Requires: %{?scl_prefix}rubygem(fog-aws) >= 0.1
Requires: %{?scl_prefix}rubygem(fog-aws) < 2
# end specfile ec2 Requires
Requires:  %{name} = %{version}-%{release}

%description ec2
Meta package to install requirements for Amazon Web Services (AWS) EC2 support.

%files ec2
%{_datadir}/%{name}/bundler.d/ec2.rb

%package rackspace
Summary: Foreman Rackspace support
Group:  Applications/System
# start specfile rackspace Requires
Requires: %{?scl_prefix}rubygem(fog-rackspace) >= 0.1.4
Requires: %{?scl_prefix}rubygem(fog-rackspace) < 0.2.0
# end specfile rackspace Requires
Requires: %{name} = %{version}-%{release}

%description rackspace
Meta package to install requirements for Rackspace compute resource support.

%files rackspace
%{_datadir}/%{name}/bundler.d/rackspace.rb

%package vmware
Summary: Foreman VMware support
Group:  Applications/System
# start specfile vmware Requires
Requires: %{?scl_prefix}rubygem(fog-vsphere) >= 2.3.0
Requires: %{?scl_prefix}rubygem(rbvmomi) >= 1.9.0
# end specfile vmware Requires
Requires: %{name} = %{version}-%{release}

%description vmware
Meta package to install requirements for VMware compute resource support.

%files vmware
%{_datadir}/%{name}/bundler.d/vmware.rb

%package gce
Summary: Foreman Google Compute Engine (GCE) support
Group:  Applications/System
# start specfile gce Requires
Requires: %{?scl_prefix}rubygem(fog-google) <= 0.1.0
Requires: %{?scl_prefix}rubygem(google-api-client) >= 0.8.2
Requires: %{?scl_prefix}rubygem(google-api-client) < 0.9.0
# end specfile gce Requires
Requires: %{name} = %{version}-%{release}

%description gce
Meta package to install requirements for Google Compute Engine (GCE) support

%files gce
%{_datadir}/%{name}/bundler.d/gce.rb

%package assets
Summary: Foreman asset pipeline support
Group: Applications/System
Requires: %{name} = %{version}-%{release}
%if 0%{?scl:1}
Requires: %{scl}-runtime-assets >= 5
Requires: %{scl}-runtime-assets < 6
%endif
Requires: nodejs >= 6.10
# Temporary dep on libuv until https://bugs.centos.org/view.php?id=10606
# is resolved
Requires: libuv

# start package.json devDependencies Requires
#Requires: npm(@storybook/addon-actions) >= 3.2.12
#Requires: npm(@storybook/addon-actions) < 4.0.0
#Requires: npm(@storybook/addon-knobs) >= 3.4.3
#Requires: npm(@storybook/addon-knobs) < 4.0.0
#Requires: npm(@storybook/react) >= 3.2.12
#Requires: npm(@storybook/react) < 4.0.0
#Requires: npm(@storybook/storybook-deployer) >= 2.0.0
#Requires: npm(@storybook/storybook-deployer) < 3.0.0
#Requires: npm(axios-mock-adapter) >= 1.10.0
#Requires: npm(axios-mock-adapter) < 2.0.0
Requires: npm(babel-cli) >= 6.10.1
Requires: npm(babel-cli) < 7.0.0
Requires: npm(babel-core) >= 6.26.3
Requires: npm(babel-core) < 7.0.0
#Requires: npm(babel-eslint) >= 6.1.2
#Requires: npm(babel-eslint) < 7.0.0
#Requires: npm(babel-jest) >= 15.0.0
#Requires: npm(babel-jest) < 16.0.0
Requires: npm(babel-loader) >= 7.1.1
Requires: npm(babel-loader) < 8.0.0
Requires: npm(babel-plugin-lodash) >= 3.3.4
Requires: npm(babel-plugin-lodash) < 4.0.0
Requires: npm(babel-plugin-transform-class-properties) >= 6.24.1
Requires: npm(babel-plugin-transform-class-properties) < 7.0.0
Requires: npm(babel-plugin-transform-object-assign) >= 6.8.0
Requires: npm(babel-plugin-transform-object-assign) < 7.0.0
Requires: npm(babel-plugin-transform-object-rest-spread) >= 6.8.0
Requires: npm(babel-plugin-transform-object-rest-spread) < 7.0.0
Requires: npm(babel-preset-env) >= 1.7.0
Requires: npm(babel-preset-env) < 2.0.0
Requires: npm(babel-preset-react) >= 6.5.0
Requires: npm(babel-preset-react) < 7.0.0
Requires: npm(babel-register) >= 6.9.0
Requires: npm(babel-register) < 7.0.0
Requires: npm(compression-webpack-plugin) >= 1.1.11
Requires: npm(compression-webpack-plugin) < 1.2.0
#Requires: npm(coveralls) >= 3.0.0
#Requires: npm(coveralls) < 4.0.0
Requires: npm(css-loader) >= 0.23.1
Requires: npm(css-loader) < 1.0.0
Requires: npm(dotenv) >= 5.0.0
Requires: npm(dotenv) < 6.0.0
#Requires: npm(enzyme) >= 3.4.0
#Requires: npm(enzyme) < 4.0.0
#Requires: npm(enzyme-adapter-react-16) >= 1.4.0
#Requires: npm(enzyme-adapter-react-16) < 2.0.0
#Requires: npm(enzyme-to-json) >= 3.2.1
#Requires: npm(enzyme-to-json) < 4.0.0
#Requires: npm(eslint) >= 4.10.0
#Requires: npm(eslint) < 5.0.0
#Requires: npm(eslint-config-airbnb-base) >= 12.1.0
#Requires: npm(eslint-config-airbnb-base) < 13.0.0
#Requires: npm(eslint-plugin-import) >= 2.8.0
#Requires: npm(eslint-plugin-import) < 3.0.0
#Requires: npm(eslint-plugin-react) >= 7.4.0
#Requires: npm(eslint-plugin-react) < 8.0.0
Requires: npm(expose-loader) >= 0.6.0
Requires: npm(expose-loader) < 0.7.0
Requires: npm(extract-text-webpack-plugin) >= 3.0.0
Requires: npm(extract-text-webpack-plugin) < 4.0.0
Requires: npm(file-loader) >= 0.9.0
Requires: npm(file-loader) < 1.0.0
#Requires: npm(highlight.js) >= 9.12.0
#Requires: npm(highlight.js) < 10.0.0
Requires: npm(identity-obj-proxy) >= 3.0.0
Requires: npm(identity-obj-proxy) < 4.0.0
#Requires: npm(jest-cli) >= 20.0.0
#Requires: npm(jest-cli) < 21.0.0
Requires: npm(jsdom) >= 9.5.0
Requires: npm(jsdom) < 10.0.0
Requires: npm(lodash-webpack-plugin) >= 0.11.4
Requires: npm(lodash-webpack-plugin) < 1.0.0
Requires: npm(node-sass) >= 4.5.0
Requires: npm(node-sass) < 5.0.0
Requires: npm(raf) >= 3.4.0
Requires: npm(raf) < 4.0.0
#Requires: npm(raw-loader) >= 0.5.1
#Requires: npm(raw-loader) < 1.0.0
#Requires: npm(react-remarkable) >= 1.1.3
#Requires: npm(react-remarkable) < 2.0.0
#Requires: npm(react-test-renderer) >= 16.2.0
#Requires: npm(react-test-renderer) < 17.0.0
#Requires: npm(redux-mock-store) >= 1.2.2
#Requires: npm(redux-mock-store) < 2.0.0
Requires: npm(sass-loader) >= 6.0.6
Requires: npm(sass-loader) < 6.1.0
Requires: npm(style-loader) >= 0.13.1
Requires: npm(style-loader) < 1.0.0
#Requires: npm(stylelint) >= 9.3.0
#Requires: npm(stylelint) < 10.0.0
#Requires: npm(stylelint-config-standard) >= 18.0.0
#Requires: npm(stylelint-config-standard) < 19.0.0
Requires: npm(uglifyjs-webpack-plugin) >= 1.2.2
Requires: npm(uglifyjs-webpack-plugin) < 2.0.0
Requires: npm(url-loader) >= 1.0.1
Requires: npm(url-loader) < 2.0.0
Requires: npm(webpack) >= 3.4.1
Requires: npm(webpack) < 4.0.0
#Requires: npm(webpack-bundle-analyzer) >= 2.13.1
#Requires: npm(webpack-bundle-analyzer) < 3.0.0
#Requires: npm(webpack-dev-server) >= 2.5.1
#Requires: npm(webpack-dev-server) < 3.0.0
Requires: npm(webpack-stats-plugin) >= 0.1.5
Requires: npm(webpack-stats-plugin) < 1.0.0
# end package.json devDependencies Requires

# start package.json dependencies Requires
Requires: npm(@novnc/novnc) >= 1.0.0
Requires: npm(@novnc/novnc) < 2.0.0
Requires: npm(axios) >= 0.17.1
Requires: npm(axios) < 1.0.0
Requires: npm(babel-polyfill) >= 6.26.0
Requires: npm(babel-polyfill) < 7.0.0
Requires: npm(bootstrap-sass) >= 3.3.7
Requires: npm(bootstrap-sass) < 4.0.0
Requires: npm(brace) >= 0.10.0
Requires: npm(brace) < 1.0.0
Requires: npm(classnames) >= 2.2.5
Requires: npm(classnames) < 3.0.0
Requires: npm(datatables.net) >= 1.10.12
Requires: npm(datatables.net) < 1.11.0
Requires: npm(datatables.net-bs) >= 1.10.12
Requires: npm(datatables.net-bs) < 1.11.0
Requires: npm(diff) >= 3.0.0
Requires: npm(diff) < 3.1.0
Requires: npm(ipaddr.js) >= 1.2.0
Requires: npm(ipaddr.js) < 1.3.0
Requires: npm(isomorphic-fetch) >= 2.2.1
Requires: npm(isomorphic-fetch) < 3.0.0
Requires: npm(jed) >= 1.1.1
Requires: npm(jed) < 2.0.0
Requires: npm(jquery) >= 2.2.4
Requires: npm(jquery) < 2.3.0
Requires: npm(jquery-flot) >= 0.8.3
Requires: npm(jquery-flot) < 0.9.0
Requires: npm(jquery-ujs) >= 1.2.0
Requires: npm(jquery-ujs) < 1.3.0
Requires: npm(jquery.cookie) >= 1.4.1
Requires: npm(jquery.cookie) < 1.5.0
Requires: npm(jstz) >= 1.0.7
Requires: npm(jstz) < 1.1.0
Requires: npm(lodash) >= 4.17.10
Requires: npm(lodash) < 5.0.0
Requires: npm(multiselect) >= 0.9.12
Requires: npm(multiselect) < 0.10.0
Requires: npm(patternfly) >= 3.42.0
Requires: npm(patternfly) < 4.0.0
Requires: npm(patternfly-react) >= 2.19.1
Requires: npm(patternfly-react) < 3.0.0
Requires: npm(prop-types) >= 15.6.0
Requires: npm(prop-types) < 16.0.0
Requires: npm(react) >= 16.4.0
Requires: npm(react) < 17.0.0
Requires: npm(react-bootstrap) = 0.32.1
Requires: npm(react-debounce-input) >= 3.2.0
Requires: npm(react-debounce-input) < 4.0.0
Requires: npm(react-dom) >= 16.4.0
Requires: npm(react-dom) < 17.0.0
Requires: npm(react-ellipsis-with-tooltip) >= 1.0.8
Requires: npm(react-ellipsis-with-tooltip) < 2.0.0
Requires: npm(react-numeric-input) >= 2.0.7
Requires: npm(react-numeric-input) < 3.0.0
Requires: npm(react-onclickoutside) >= 6.6.2
Requires: npm(react-onclickoutside) < 7.0.0
Requires: npm(react-password-strength) >= 2.1.0
Requires: npm(react-password-strength) < 3.0.0
Requires: npm(react-redux) >= 5.0.6
Requires: npm(react-redux) < 6.0.0
Requires: npm(redux) >= 3.6.0
Requires: npm(redux) < 4.0.0
Requires: npm(redux-form) = 7.2.0
Requires: npm(redux-form-validators) >= 2.1.2
Requires: npm(redux-form-validators) < 3.0.0
Requires: npm(redux-logger) >= 2.8.1
Requires: npm(redux-logger) < 3.0.0
Requires: npm(redux-thunk) >= 2.2.0
Requires: npm(redux-thunk) < 3.0.0
Requires: npm(reselect) >= 3.0.1
Requires: npm(reselect) < 4.0.0
Requires: npm(seamless-immutable) >= 7.1.2
Requires: npm(seamless-immutable) < 8.0.0
Requires: npm(select2) >= 3.5.2
Requires: npm(select2) < 3.6.0
Requires: npm(urijs) >= 1.18.10
Requires: npm(urijs) < 2.0.0
Requires: npm(uuid) >= 3.0.1
Requires: npm(uuid) < 4.0.0
# end package.json dependencies Requires

# start specfile assets Requires
Requires: %{?scl_prefix_ror}rubygem(jquery-turbolinks) >= 2.1
Requires: %{?scl_prefix_ror}rubygem(jquery-turbolinks) < 3.0
Requires: %{?scl_prefix}rubygem(jquery-ui-rails) < 5.0.0
Requires: %{?scl_prefix}rubygem(patternfly-sass) >= 3.32.1
Requires: %{?scl_prefix}rubygem(patternfly-sass) < 3.38.0
Requires: %{?scl_prefix}rubygem(gridster-rails) >= 0.5
Requires: %{?scl_prefix}rubygem(gridster-rails) < 1.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) >= 1.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) < 2.0
Requires: %{?scl_prefix_ror}rubygem(execjs) >= 1.4.0
Requires: %{?scl_prefix_ror}rubygem(execjs) < 3.0
Requires: %{?scl_prefix_ror}rubygem(uglifier) >= 1.0.3
Requires: %{?scl_prefix_ror}rubygem(sass-rails) >= 5.0
Requires: %{?scl_prefix_ror}rubygem(sass-rails) < 6.0
Requires: %{?scl_prefix}rubygem(spice-html5-rails) >= 0.1.5
Requires: %{?scl_prefix}rubygem(spice-html5-rails) < 0.2.0
# end specfile assets Requires

%description assets
Meta package to install asset pipeline support.

%files assets
%{_datadir}/%{name}/bundler.d/assets.rb
%{_datadir}/%{name}/webpack

%package plugin
Summary: Foreman plugin support
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-build = %{version}-%{release}
Requires: %{name}-sqlite = %{version}-%{release}

%description plugin
Meta package with support for plugins.

%files plugin
%{_sysconfdir}/rpm/macros.%{name}-plugin
%{_datadir}/%{name}/schema_plugin.rb

%package build
Summary: Foreman package RPM support
Group: Development/Libraries

%description build
Meta package with support for building RPMs in the Foreman release cycle.

%files build
%{_sysconfdir}/rpm/macros.%{name}-dist
%{_fileattrsdir}/%{name}.attr
%{_rpmconfigdir}/%{name}.*

%package console
Summary: Foreman console support
Group:  Applications/System
# start specfile console Requires
Requires: %{?scl_prefix}rubygem(wirb) >= 1.0
Requires: %{?scl_prefix}rubygem(wirb) < 3.0
Requires: %{?scl_prefix}rubygem(hirb-unicode-steakknife) >= 0.0.7
Requires: %{?scl_prefix}rubygem(hirb-unicode-steakknife) < 0.1.0
Requires: %{?scl_prefix}rubygem(awesome_print) >= 1.0
Requires: %{?scl_prefix}rubygem(awesome_print) < 2.0
# end specfile console Requires
Requires: %{name} = %{version}-%{release}

%description console
Meta Package to install requirements for console support

%files console
%{_datadir}/%{name}/bundler.d/console.rb

%package mysql2
Summary: Foreman mysql2 support
Group:  Applications/System
# start specfile mysql2 Requires
Requires: %{?scl_prefix}rubygem(mysql2) >= 0.4.4
Requires: %{?scl_prefix}rubygem(mysql2) < 0.6.0
# end specfile mysql2 Requires
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-mysql < 1.4.0
Provides: %{name}-mysql = %{version}

%description mysql2
Meta Package to install requirements for mysql2 support

%files mysql2
%{_datadir}/%{name}/bundler.d/mysql2.rb

%package postgresql
Summary: Foreman Postgresql support
Group:  Applications/System
# start specfile postgresql Requires
Requires: %{?scl_prefix}rubygem(pg) >= 0.18
Requires: %{?scl_prefix}rubygem(pg) < 2.0
# end specfile postgresql Requires
Requires: %{name} = %{version}-%{release}

%description postgresql
Meta Package to install requirements for postgresql support

%files postgresql
%{_datadir}/%{name}/bundler.d/postgresql.rb

%package sqlite
Summary: Foreman sqlite support
Group:  Applications/System
# start specfile sqlite Requires
Requires: %{?scl_prefix_ror}rubygem(sqlite3) >= 1.3.6
Requires: %{?scl_prefix_ror}rubygem(sqlite3) < 1.4.0
# end specfile sqlite Requires
Requires: %{name} = %{version}-%{release}

%description sqlite
Meta Package to install requirements for sqlite support

%files sqlite
%{_datadir}/%{name}/bundler.d/sqlite.rb

%package telemetry
Summary: Foreman telemetry support
Group:  Applications/System
# start specfile telemetry Requires
Requires: %{?scl_prefix}rubygem(prometheus-client)
Requires: %{?scl_prefix}rubygem(statsd-instrument)
# end specfile telemetry Requires
Requires: %{name} = %{version}-%{release}

%description telemetry
Meta Package to install requirements for telemetry support

%files telemetry
%{_datadir}/%{name}/bundler.d/telemetry.rb

%package journald
Summary: Foreman journald logging support
Group:  Applications/System
# start specfile journald Requires
Requires: %{?scl_prefix}rubygem(logging-journald) >= 2.0
Requires: %{?scl_prefix}rubygem(logging-journald) < 3.0
# end specfile journald Requires
Requires: %{name} = %{version}-%{release}

%description journald
Meta Package to install requirements for journald logging support

%files journald
%{_datadir}/%{name}/bundler.d/journald.rb

%description
Foreman is aimed to be a Single Address For All Machines Life Cycle Management.
Foreman is based on Ruby on Rails, and this package bundles Rails and all
plugins required for Foreman to work.

%prep
%setup -q -n %{name}-%{version}%{?prerelease:-}%{?prerelease}

%build
#build man pages
%{scl_rake} -f Rakefile.dist build \
  PREFIX=%{_prefix} \
  SBINDIR=%{_sbindir} \
  SYSCONFDIR=%{_sysconfdir} \
  --trace

#replace shebangs and binaries in scripts for SCL
%if %{?scl:1}%{!?scl:0}
  # shebangs
  for f in bin/* script/performance/profiler script/performance/benchmarker script/foreman-config script/dynflowd ; do
    sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby_bin}X' $f
  done
  # script content
  sed -ri 'sX/usr/bin/rakeX%{scl_rake}X' extras/dbmigrate script/foreman-rake
%endif

#build locale files
make -C locale all-mo

#use Bundler_ext instead of Bundler
mv Gemfile Gemfile.in
cp config/database.yml.example config/database.yml
cp config/settings.yaml.example config/settings.yaml
#we need to allow taxonomies so apipie cache renders documentation with them
sed -i 's/:locations_enabled: false/:locations_enabled: true/' config/settings.yaml
sed -i 's/:organizations_enabled: false/:organizations_enabled: true/' config/settings.yaml
export BUNDLER_EXT_GROUPS="default assets"
ln -s %{nodejs_sitelib} node_modules
export NODE_ENV=production
%{?scl:scl enable %{scl} "}
webpack --bail --config config/webpack.config.js
%{?scl:"}
%{scl_rake} assets:precompile RAILS_ENV=production --trace
%{scl_rake} db:migrate db:schema:dump RAILS_ENV=production --trace
%{scl_rake} apipie:cache RAILS_ENV=production cache_part=resources --trace
rm config/database.yml config/settings.yaml

%install
rm -rf %{buildroot}

#install man pages
%{scl_rake} -f Rakefile.dist install \
  PREFIX=%{buildroot}%{_prefix} \
  SBINDIR=%{buildroot}%{_sbindir} \
  SYSCONFDIR=%{buildroot}%{_sysconfdir} \
  --trace
%{scl_rake} -f Rakefile.dist clean

install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}/plugins
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/plugins
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp/pids
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}/plugins
#Copy init scripts and sysconfigs
install -Dp -m0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/sysconfig/%{executor_service_name}
install -Dp -m0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{executor_service_name}.service
install -Dp -m0755 script/%{executor_service_name} %{buildroot}%{_sbindir}/%{executor_service_name}
install -Dp -m0755 script/%{name}-debug %{buildroot}%{_sbindir}/%{name}-debug
install -Dp -m0755 script/%{name}-rake %{buildroot}%{_sbindir}/%{name}-rake
install -Dp -m0755 script/%{name}-tail %{buildroot}%{_sbindir}/%{name}-tail
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf

cp -p Gemfile.in %{buildroot}%{_datadir}/%{name}/Gemfile.in
cp -p -r app bin bundler.d config config.ru extras lib locale Rakefile script webpack %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/%{name}/extras/{jumpstart,spec}
find %{buildroot}%{_datadir}/%{name}/script/%{name}-tail.d/* -type d |xargs rm -rf

# remove all test units from produciton release
find %{buildroot}%{_datadir}/%{name} -type d -name "test" |xargs rm -rf

# remove spring loader, depends on Bundler and only installed via development group
rm -f %{buildroot}%{_datadir}/%{name}/bin/spring

# Move config files to %{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/config/database.yml.example %{buildroot}%{_datadir}/%{name}/config/database.yml
mv %{buildroot}%{_datadir}/%{name}/config/settings.yaml.example %{buildroot}%{_datadir}/%{name}/config/settings.yaml

for i in database.yml settings.yaml foreman-debug.conf; do
mv %{buildroot}%{_datadir}/%{name}/config/$i %{buildroot}%{_sysconfdir}/%{name}
ln -sv %{_sysconfdir}/%{name}/$i %{buildroot}%{_datadir}/%{name}/config/$i
done

# Put db in %{_localstatedir}/lib/%{name}/db
cp -pr db/migrate db/seeds.rb db/seeds.d %{buildroot}%{_datadir}/%{name}
mkdir %{buildroot}%{_localstatedir}/lib/%{name}/db

ln -sv %{_localstatedir}/lib/%{name}/db %{buildroot}%{_datadir}/%{name}/db
ln -sv %{_datadir}/%{name}/migrate %{buildroot}%{_localstatedir}/lib/%{name}/db/migrate
ln -sv %{_datadir}/%{name}/seeds.rb %{buildroot}%{_localstatedir}/lib/%{name}/db/seeds.rb
ln -sv %{_datadir}/%{name}/seeds.d %{buildroot}%{_localstatedir}/lib/%{name}/db/seeds.d

# Put HTML %{_localstatedir}/lib/%{name}/public
cp -pr public %{buildroot}%{_localstatedir}/lib/%{name}/
ln -sv %{_localstatedir}/lib/%{name}/public %{buildroot}%{_datadir}/%{name}/public

# Put logs in %{_localstatedir}/log/%{name}
ln -sv %{_localstatedir}/log/%{name} %{buildroot}%{_datadir}/%{name}/log

# Put tmp files in %{_localstatedir}/run/%{name}
ln -sv %{_localstatedir}/run/%{name} %{buildroot}%{_datadir}/%{name}/tmp

# Symlink plugin settings directory to
ln -sv %{_sysconfdir}/%{name}/plugins %{buildroot}%{_datadir}/%{name}/config/settings.plugins.d

# Create VERSION file
install -pm0644 VERSION %{buildroot}%{_datadir}/%{name}/VERSION

# Create RPM macros for plugin packages to use at build time
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat > %{buildroot}%{_sysconfdir}/rpm/macros.%{name} << EOF
# Common locations
%%%{name}_dir %{_datadir}/%{name}
%%%{name}_bundlerd_dir %%{%{name}_dir}/bundler.d
%%%{name}_log_dir %{_localstatedir}/log/%{name}

# Common commands
%%%{name}_rake         %{foreman_rake}
%%%{name}_db_migrate   %%{%{name}_rake} db:migrate >> %%{%{name}_log_dir}/db_migrate.log 2>&1 || :
%%%{name}_db_seed      %%{%{name}_rake} db:seed >> %%{%{name}_log_dir}/db_seed.log 2>&1 || :
%%%{name}_restart      (/bin/systemctl try-restart %{name}.service) >/dev/null 2>&1
EOF

# Keep a copy of the schema for quick initialisation of plugin builds
cp -pr db/schema.rb %{buildroot}%{_datadir}/%{name}/schema_plugin.rb

cat > %{buildroot}%{_sysconfdir}/rpm/macros.%{name}-dist << EOF
# Version to use like a dist tag
%%%{name}dist .fm$(echo %{version} | awk -F. '{print $1 "_" $2}')
EOF

cat > %{buildroot}%{_sysconfdir}/rpm/macros.%{name}-plugin << EOF
# Generate bundler.d file for a plugin
# -n<plugin_name>   Overrides default of gem_name
%%%{name}_bundlerd_file(n:) \\
mkdir -p %%{buildroot}%%{%{name}_bundlerd_dir} \\
cat <<GEMFILE > %%{buildroot}%%{%{name}_bundlerd_dir}/%%{-n*}%%{!?-n:%%{gem_name}}.rb \\
gem '%%{-n*}%%{!?-n:%%{gem_name}}' \\
GEMFILE

# Common locations
%%%{name}_bundlerd_plugin %%{%{name}_bundlerd_dir}/%%{gem_name}.rb
%%%{name}_pluginconf_dir %{_sysconfdir}/%{name}/plugins
# Common assets locations
%%%{name}_assets_plugin %%{gem_instdir}/public/assets/%%{gem_name}
# Common webpack locations
%%%{name}_webpack_plugin %%{gem_instdir}/public/webpack/%%{gem_name}
%%%{name}_webpack_foreman %%{foreman_dir}/public/webpack/%%{gem_name}
# Common apipie locations
%%%{name}_apipie_cache_plugin %%{gem_instdir}/public/apipie-cache/plugin/%%{gem_name}
%%%{name}_apipie_cache_foreman %%{foreman_dir}/public/apipie-cache/plugin/%%{gem_name}
# build apipie cache index
%%%{name}_apipie_cache %%{%{name}_rake} apipie:cache:index >> %%{%{name}_log_dir}/apipie_cache.log 2>&1 || :

# Generate precompiled assets at gem_instdir/public/assets/gem_name/
# -r<rake_task>     Overrides rake task of plugin:assets:precompile[plugin_name]
# -n<plugin_name>   Overrides default of gem_name for precompile step
# -a                Prebuild apipie cache
# -s                Precompile assets
%%%{name}_precompile_plugin(r:n:as) \\
mkdir -p ./%{_datadir} \\
cp -r %%{%{name}_dir} ./%{_datadir} || echo 0 \\
mkdir -p ./%{_localstatedir}/lib/%{name} \\
cp -r %{_localstatedir}/lib/%{name}/db ./%{_localstatedir}/lib/%{name} || echo 0 \\
unlink ./%{_datadir}/%{name}/db \\
ln -sv \`pwd\`/%{_localstatedir}/lib/%{name}/db ./%{_datadir}/%{name}/db \\
pushd ./%%{%{name}_dir} \\
\\
ln -s %{nodejs_sitelib} node_modules \\
sed -i 's/:locations_enabled: false/:locations_enabled: true/' \`pwd\`/config/settings.yaml \\
sed -i 's/:organizations_enabled: false/:organizations_enabled: true/' \`pwd\`/config/settings.yaml \\
export GEM_PATH=%%{buildroot}%%{gem_dir}:\${GEM_PATH:+\${GEM_PATH}}\${GEM_PATH:-\`%{?scl:scl enable %%{scl_ror} -- }ruby -e "print Gem.path.join(':')"\`} \\
unlink tmp \\
\\
rm \`pwd\`/config/initializers/encryption_key.rb \\
/usr/bin/%%{?scl:%%{scl}-}rake security:generate_encryption_key \\
export BUNDLER_EXT_NOSTRICT=1 \\
export NODE_ENV=production \\
cp %%{buildroot}%%{%{name}_bundlerd_dir}/%%{gem_name}.rb ./bundler.d/%%{gem_name}.rb \\
%%{?-a:/usr/bin/%%{?scl:%%{scl}-}rake db:create RAILS_ENV=development --trace} \\
%%{?-a:/usr/bin/%%{?scl:%%{scl}-}rake db:migrate RAILS_ENV=development --trace} \\
%%{?-s:/usr/bin/%%{?scl:%%{scl}-}rake %%{-r*}%%{!?-r:plugin:assets:precompile[%%{-n*}%%{!?-n:%%{gem_name}}]} RAILS_ENV=production --trace} \\
%%{?-a:/usr/bin/%%{?scl:%%{scl}-}rake plugin:apipie:cache[%%{gem_name}] RAILS_ENV=development cache_part=resources OUT=%%{buildroot}%%{%{name}_apipie_cache_plugin} --trace} \\
\\
popd \\
rm -rf ./usr \\
%%{?-a:mkdir -p %%{buildroot}%%{foreman_dir}/public/apipie-cache/plugin} \\
%%{?-a:ln -s %%{%{name}_apipie_cache_plugin} %%{buildroot}%%{%{name}_apipie_cache_foreman}} \\
%%{?-s:[ -e %%{buildroot}%%{%{name}_webpack_plugin} ] && mkdir -p %%{buildroot}%%{foreman_dir}/public/webpack} \\
%%{?-s:[ -e %%{buildroot}%%{%{name}_webpack_plugin} ] && ln -s %%{%{name}_webpack_plugin} %%{buildroot}%%{%{name}_webpack_foreman}}
EOF

#copy rpm config
install -Dpm0644 %{SOURCE6} %{buildroot}%{_fileattrsdir}/%{name}.attr
install -pm0755 %{SOURCE7} %{buildroot}%{_rpmconfigdir}/%{name}.prov
install -pm0755 %{SOURCE7} %{buildroot}%{_rpmconfigdir}/%{name}.req

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc CHANGELOG Contributors README.md VERSION
%license LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/app
%exclude %{_datadir}/%{name}/app/assets
%exclude %{_datadir}/%{name}/script/%{name}-debug.d
%dir %{_datadir}/%{name}/bundler.d
%exclude %{_datadir}/%{name}/bundler.d/development.rb
%{_datadir}/%{name}/bundler.d/facter.rb
%{_datadir}/%{name}/bundler.d/jsonp.rb
%exclude %{_datadir}/%{name}/bundler.d/openid.rb
%exclude %{_datadir}/%{name}/bundler.d/test.rb
%{_datadir}/%{name}/bin
%{_datadir}/%{name}/config*
%{_datadir}/%{name}/db
%{_datadir}/%{name}/extras
%{_datadir}/%{name}/Gemfile.in
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/locale
%{_datadir}/%{name}/log
%{_datadir}/%{name}/migrate
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/public
%{_datadir}/%{name}/Rakefile
%{_datadir}/%{name}/script
%{_datadir}/%{name}/seeds.*
%attr(700,%{name},%{name}) %{_datadir}/%{name}/.ssh
%{_datadir}/%{name}/tmp
%{_datadir}/%{name}/VERSION
%{_sbindir}/%{name}-rake
%{_sbindir}/%{name}-tail
%{_mandir}/man8
%config(noreplace) %{_sysconfdir}/%{name}
%ghost %attr(0640,root,%{name}) %config(noreplace) %{_sysconfdir}/%{name}/encryption_key.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config %{_sysconfdir}/cron.d/%{name}
%{_sysconfdir}/rpm/macros.%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/lib/%{name}
%attr(750,%{name},%{name}) %{_localstatedir}/log/%{name}
%attr(750,%{name},%{name}) %{_localstatedir}/log/%{name}/plugins
%attr(-,%{name},%{name}) %{_localstatedir}/run/%{name}
%attr(-,%{name},root) %{_datadir}/%{name}/config.ru
%attr(-,%{name},root) %{_datadir}/%{name}/config/environment.rb
%ghost %{_datadir}/%{name}/config/initializers/encryption_key.rb
%ghost %attr(0640,root,%{name}) %config(noreplace) %{_datadir}/%{name}/config/initializers/local_secret_token.rb
%{_tmpfilesdir}/%{name}.conf

# Service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_sbindir}/%{executor_service_name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{executor_service_name}
%{_unitdir}/%{executor_service_name}.service

%pre
# Add the "foreman" user and group
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{homedir} -s /sbin/nologin -c "Foreman" %{name}
exit 0

%post
# secret token used for cookie signing etc.
if [ ! -f %{_datadir}/%{name}/config/initializers/local_secret_token.rb ]; then
  touch %{_datadir}/%{name}/config/initializers/local_secret_token.rb
  chmod 0660 %{_datadir}/%{name}/config/initializers/local_secret_token.rb
  chgrp foreman %{_datadir}/%{name}/config/initializers/local_secret_token.rb
  %{foreman_rake} security:generate_token >/dev/null 2>&1 || :
  chmod 0640 %{_datadir}/%{name}/config/initializers/local_secret_token.rb
fi

# encryption key used to encrypt DB contents
# move the generated key file to /etc/foreman/ so users back it up, symlink to it from ~foreman
if [ ! -e %{_datadir}/%{name}/config/initializers/encryption_key.rb -a \
     ! -e %{_sysconfdir}/%{name}/encryption_key.rb ]; then
  touch %{_datadir}/%{name}/config/initializers/encryption_key.rb
  chmod 0660 %{_datadir}/%{name}/config/initializers/encryption_key.rb
  chgrp foreman %{_datadir}/%{name}/config/initializers/encryption_key.rb
  %{foreman_rake} security:generate_encryption_key >/dev/null 2>&1 || :
  chmod 0640 %{_datadir}/%{name}/config/initializers/encryption_key.rb
  mv %{_datadir}/%{name}/config/initializers/encryption_key.rb %{_sysconfdir}/%{name}/
fi
if [ ! -e %{_datadir}/%{name}/config/initializers/encryption_key.rb -a \
     -e %{_sysconfdir}/%{name}/encryption_key.rb ]; then
  ln -s %{_sysconfdir}/%{name}/encryption_key.rb %{_datadir}/%{name}/config/initializers/
fi

%systemd_postun_with_restart %{name}.service
%systemd_post %{executor_service_name}.service
exit 0

%posttrans
# We need to run the db:migrate after the install transaction
# always attempt to reencrypt after update in case new fields can be encrypted
%{foreman_rake} db:migrate db:encrypt_all >> %{_localstatedir}/log/%{name}/db_migrate.log 2>&1 || :
%{foreman_rake} db:seed >> %{_localstatedir}/log/%{name}/db_seed.log 2>&1 || :
%{foreman_rake} apipie:cache:index >> %{_localstatedir}/log/%{name}/apipie_cache.log 2>&1 || :
%{foreman_rake} tmp:clear >> %{_localstatedir}/log/%{name}/tmp_clear.log 2>&1 || :
(/bin/systemctl try-restart %{name}.service) >/dev/null 2>&1
exit 0

%preun
%systemd_preun %{executor_service_name}.service
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{executor_service_name}.service
%systemd_postun_with_restart %{name}.service

%changelog
* Sun Dec 09 2018 Tomer Brisker <tbrisker@redhat.com> - 1.20.1-2
- Release 1.20.1

* Thu Dec 06 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.1-1
- Release 1.20.1

* Fri Nov 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-1
- Release 1.20.0

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.14.RC2
- Release 1.20.0-RC2

* Fri Oct 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.14.RC1
- Release 1.20.0-RC1

* Tue Oct 16 2018 Evgeni Golov - 1.20.0-0.13.develop
- ignore JS maps in webpack requires/provides

* Tue Oct 16 2018 Lukas Zapletal <lzap+rpm@redhat.com> - 1.20.0-0.12.develop
- Updated logging-journald dependency to 2.0 series

* Fri Oct 12 2018 Evgeni Golov - 1.20.0-0.11.develop
- Add automatic Provides and Requires for Foreman's webpack bundles.
  This should ensure that plugins can depend on a specific bundle version and
  get rebuilt when Foreman's bundle changes.

* Mon Oct 08 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.10.develop
- Update Gem and NPM dependencies

* Fri Sep 14 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.9.develop
- Treat logging.yaml as non-config

* Thu Sep 13 2018 Timo Goebel <mail@timogoebel.name> - 1.20.0-0.8.develop
- remove rails 4 message encryptor extensions patch

* Tue Sep 11 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.7.develop
- Update Gem and NPM dependencies

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.6.develop
- Drop schema loading for plugin builds

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> 1.20.0-0.5.develop
- Updates for Rails 5.2 and Ruby 2.5

* Mon Aug 20 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.4.develop
- Remove foreman-release as a subpackage

* Mon Aug 13 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.3.develop
- Handle GPG checking after branching

* Wed Aug 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.2.develop
- Move the foreman-rails repository definition from foreman-release-scl to foreman-release

* Wed Jul 25 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.1.develop
- Add prerelease macro

* Tue Jul 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.develop
- Bump version to 1.20-develop

* Thu May 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.19.0-0.develop
- Bump version to 1.19-develop

* Thu Jan 11 2018 Eric D Helms <ericdhelms@gmail.com> - 1.18.0-0.develop
- Bump version to 1.18-develop

* Mon Aug 28 2017 Daniel Lobato Garcia <me@daniellobato.me> - 1.17.0-0.develop
- Bump version to 1.17-develop

* Wed Mar 29 2017 Eric D Helms <ericdhelms@gmail.com> - 1.16.0-0.develop
- Bump version to 1.16-develop

* Tue Dec 06 2016 Dominic Cleal <dominic@cleal.org> - 1.15.0-0.develop
- Bump version to 1.15-develop

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> - 1.14.0-0.develop
- Bump version to 1.14-develop

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> - 1.13.0-0.develop
- Bump version to 1.13-develop

* Fri Feb 19 2016 Dominic Cleal <dominic@cleal.org> - 1.12.0-0.develop
- Bump version to 1.12-develop

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> - 1.11.0-0.develop
- Bump version to 1.11-develop

* Fri Jun 26 2015 Dominic Cleal <dcleal@redhat.com> - 1.10.0-0.develop
- Bump version to 1.10-develop

* Tue Mar 03 2015 Dominic Cleal <dcleal@redhat.com> - 1.9.0-0.develop
- Bump version to 1.9-develop

* Tue Oct 28 2014 Dominic Cleal <dcleal@redhat.com> - 1.8.0-0.develop
- Bump version to 1.8-develop

* Mon Aug 11 2014 Dominic Cleal <dcleal@redhat.com> - 1.7.0-0.develop
- Bump version to 1.7-develop

* Wed Apr 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.6.0-0.develop
- Bump version to 1.6-develop

* Thu Jan 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.5.0-0.develop
- Bump version to 1.5-develop
- Remove rails3_before_render dependency
- generate encryption key and encrypt data in postinstall (#2929)

* Thu Nov 21 2013 Dominic Cleal <dcleal@redhat.com> - 1.4.0-0.develop
- Bump and change versioning scheme, don't overwrite VERSION (#3712)
- Pin fog to 1.18.x
- Add new rails3_before_render dependency
- Removed foreman-mysql package (obsoleted by mysql2)
- Seed database after DB migration
- Change twitter-bootstrap-rails to bootstrap-sass
- Pin fog to 1.19.x
- Add BR and explicit dependency on Ruby binary, for ruby193-ruby-wrapper

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> - 1.3.9999-7
- Add rubygem-unf as a requires for the compute subpackage

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> - 1.3.9999-6
* Add foreman-gce subpackage for Google Compute Engine

* Wed Nov 6 2013 David Davis <daviddavis@redhat.com> - 1.3.9999-5
- Removing rr gem, fixes #3597

* Fri Oct 25 2013 Martin Bacovsky <mbacovsk@redhat.com> - 1.3.9999-4
- foreman-cli metapackage installs hammer

* Mon Sep 30 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-3
- Adding Foreman plugins repo

* Fri Sep 27 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-2
- Update rubygem-ancestry to 2.x

* Wed Sep 11 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-1
- Bump to version 1.3-develop

* Wed Sep 11 2013 Dominic Cleal <dcleal@redhat.com> - 1.2.9999-11
- Add new foreigner and immigrant dependencies

* Mon Sep 09 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-10
- Added dependency on fast_gettext 0.8 (multi-domain support)

* Mon Sep 02 2013 Greg Sutcliffe <gsutclif@redhat.com> 1.2.9999-9
- Remove Puppet from core requirements

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.2.9999-8
- Update fog dependency to 1.15.0 to fix rackspace VM listing issue

* Wed Jul 24 2013 Jason Montleon <jmontleo@redhat.com> 1.2.9999-7
- Update rbovirt dependency version to 0.0.21 to support sending the host ssl certificate subject as an option to the xpi plugin

* Fri Jul 19 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-6
- add foreman-rake to /usr/sbin

* Mon Jun 17 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-5
- fix asset dependency versions
- add minitest dependency for console (Lukas Zapletal)

* Thu Jun 06 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-4
- fix libvirt package dependency on ruby-libvirt

* Wed Jun 05 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-3
- foreman-debug tool now installed into /usr/sbin

* Tue May 28 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-2
- Don't force SCL
- Distribute GPG key
- Replace dist in foreman.repo
- Rename foreman-ec2 to foreman-compute
- Update dbmigrate for SCL (Lukas Zapletal)

* Mon May 20 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-1
- Updated to 1.2.9999 (1.3-pre)

* Tue Apr 30 2013 Sam Kottler <shk@redhat.com> 1.1.9999-1
- Updated to 1.1.9999 (1.2-pre)

* Fri Feb 15 2013 shk@redhat.com 1.1-3
- Bumped safemode dependency

* Thu Feb 14 2013 shk@redhat.com 1.1-2
- Fixed baseurl in the -release subpackage.
- Updated to 1.1-1

* Mon Feb 4 2013 shk@redhat.com 1.1-1
- 1.1 final.

* Mon Jan 28 2013 shk@redhat.com 1.1RC5-2
- Bumped fog version dependency

* Fri Jan 25 2013 shk@redhat.com 1.1RC5-1
- Updated Rails requirements and bumped to RC5.

* Thu Dec 27 2012 shk@redhat.com 1.1RC3-1
- Updated to 1.1RC3 and updated dependencies.

* Wed Dec 19 2012 jmontleo@redhat.com 1.0.2-1
- Fix Foreman SQL injection through search mechanism CVE-2012-5648

* Thu Aug 09 2012 jmontleo@redhat.com 1.0.1-1
- Version 1.0.1

* Sun Aug 05 2012 jmontleo@redhat.com 1.0.0-2
- Update to pull in fixes

* Mon Jul 23 2012 jmontleo@redhat.com 1.0.0-1
- Update packages for Foreman 1.0 Release and add support for using thin.

* Wed Jul 18 2012 jmontleo@redhat.com 1.0.0-0.7
- Updated pacakages for Foreman 1.0 RC5 and Proxy RC2

* Thu Jul 05 2012 jmontleo@redhat.com 1.0.0-0.6
- Fix foreman-release to account for different archs. Pull todays source.

* Wed Jul 04 2012 jmontleo@redhat.com 1.0.0-0.5
- Bump version number and rebuild for RC3

* Sun Jul 01 2012 jmontleo@redhat.com 1.0.0-0.4
- Pull todays develop branch to fix dbmigrate issue, add mistakenly deleted version string back, and replace foreman-fog with foreman-ec2 as it indicates more clearly what functionality the package provides.

* Fri Jun 29 2012 jmontleo@redhat.com 1.0.0-0.3
- More fixes for dbmigrate, foreman-cli and foreman-release added

* Fri Jun 29 2012 jmontleo@redhat.com 1.0.0-0.2
- Rebuild with develop branch from today for 1.0.0 RC2. Try to fix inconsistent db:migrate runs on upgrades.

* Tue Jun 19 2012 jmontleo@redhat.com 0-5.1-20
- Implement conf.d style Gemfile configuration for bundle to replace the ugly method used in previous rpm versions. Replace foreman-virt package with foreman-libvirt package as it was confusing to have fog virt ovirt and vmware.

* Tue Jun 19 2012 jmontleo@redhat.com 0-5.1-9
- Rebuild with todays develop branch. Add VERSION file 1688, add wget dependency 1514, update rbovirt dep to 0.0.12, and break out ovirt support to foreman-ovirt package.

* Thu Jun 14 2012 jmontleo@redhat.com 0.5.1-8
- Rebuild with todays develop branch.

* Wed Jun 13 2012 jmontleo@redhat.com 0.5.1-7
- Rebuild with todays develop branch. Add require for at least rubygem-rake 0.9.2.2. Run rake:db migrate on upgrade.

* Wed May 30 2012 jmontleo@redhat.com 0.5.1-5
- Rebuild with todays merge of compute resource RBAC patch

* Tue May 29 2012 jmontleo@redhat.com 0.5.1-4
- Fix rpm dependencies for foreman-virt and foreman-vmware to include foreman-fog

* Tue May 29 2012 jmontleo@redhat.com 0.5.1-3
- tidy up postinstall prepbundle.sh, rebuild with EC2 support, and split out foreman-fog and foreman-vmware support

* Tue May 08 2012 jmontleo@redhat.com 0.5.1-1
- adding prepbundle.sh to run post install of any foreman packages, other small fixes

* Fri May 04 2012 jmontleo@redhat.com 0.5.1-0.2
- updated foreman to develop branch from May 04 which included many fixes including no longer requiring foreman-virt

* Wed Jan 11 2012 ohadlevy@gmail.com - 0.4.2
- rebuilt

* Tue Dec 6 2011 ohadlevy@gmail.com - 0.4.1
- rebuilt

* Tue Nov 08 2011 ohadlevy@gmail.com - 0.4
- rebuilt

* Mon Nov 07 2011 ohadlevy@gmail.com - 0.4rc5
- rebuilt

* Tue Oct 25 2011 ohadlevy@gmail.com - 0.4rc4
- rebuilt

* Tue Oct 18 2011 ohadlevy@gmail.com - 0.4rc3
- rebuilt

* Wed Sep 28 2011 ohadlevy@gmail.com - 0.4rc2
- rebuilt

* Sat Sep 10 2011 ohadlevy@gmail.com - 0.4rc1
- rebuilt

* Tue Jun 07 2011 ohadlevy@gmail.com - 0.3
- rebuilt

* Tue May 24 2011 ohadlevy@gmail.com - 0.3rc1-2
- rebuilt

* Thu May 05 2011 ohadlevy@gmail.com - 0.3rc1
- rebuilt

* Tue Mar 29 2011 ohadlevy@gmail.com - 0.2
- Version bump to 0.2

* Tue Mar 22 2011 ohadlevy@gmail.com - 0.2-rc1
- rebuilt

* Thu Feb 24 2011 ohadlevy@gmail.com - 0.1.7-rc5
- rebuilt

* Sat Feb 12 2011 ohadlevy@gmail.com - 0.1.7-rc4.1
- rebuilt

* Mon Jan 31 2011 ohadlevy@gmail.com - 0.1.7-rc3.1
- rebuilt

* Tue Jan 18 2011 ohadlevy@gmail.com - 0.1.7-rc2.1
- rebuilt

* Sat Jan 15 2011 ohadlevy@gmail.com - 0.1.7-rc2
- rebuilt

* Fri Dec 17 2010 ohadlevy@gmail.com - 0.1.7rc1
- rebuilt

* Mon Nov 29 2010 ohadlevy@gmail.com - 0.1.6-3
- rebuilt

* Fri Nov 12 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6-1
- Included fix for #461, as without it newly installed instances are not usable

* Thu Nov 11 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6
- New upstream version

* Sat Oct 30 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6rc2
- New release candidate
- Updated configuration file permssion not to break passenger

* Sun Sep 19 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6rc1
- Removed the depenecy upon rack 1.0.1 as its now bundled within Foreman

* Mon May 31 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.5-1
- New upstream version
- Added migration support between old directory layout to FHS compliancy, upgrades from 0.1-4.x should now work
- Added support for logrotate
- Cleanup old activescaffold plugin leftovers files

* Fri Apr 30 2010 Todd Zullinger <tmz@pobox.com> - 0.1.4-4
- Rework %%install for better FHS compliance
- Misc. adjustments to match Fedora/EPEL packaging guidelines
- Update License field to GPLv3+ to match README
- Use foreman as the primary group for the foreman user instead of puppet
- This breaks compatibility with previous RPM, as directories can't be replaced with links easily.

* Mon Apr 19 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1-4-3
- added status to startup script
- removed puppet module from the RPM

* Mon Apr 12 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.4-2
- Added startup script for built in webrick server
- Changed foreman user default shell to /sbin/nologin and is now part of the puppet group
- defaults to sqlite database

* Tue Apr 6 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.4-1
- Initial release.
