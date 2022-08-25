%global homedir %{_datadir}/%{name}
%global confdir extras/packaging/rpm/sources
%global foreman_rake %{_sbindir}/%{name}-rake
%global dynflow_sidekiq_service_name dynflow-sidekiq@
%global rake /usr/bin/rake

%global release 7
%global prereleasesource rc2
%global prerelease %{?prereleasesource}

Name:    foreman
Version: 3.4.0
Release: %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?nightly}%{?dist}
Summary: Systems Management web application

Group:  Applications/System
License: GPLv3+ with exceptions
URL: https://theforeman.org
Source0: https://downloads.theforeman.org/%{name}/%{name}-%{version}%{?prerelease:-}%{?prerelease}.tar.bz2
Source3: %{name}.logrotate
Source4: %{name}.cron.d
Source5: %{name}.tmpfiles
BuildArch:  noarch

Requires: ruby(release)
Requires: rubygems
Requires: rubygem(rake) >= 0.8.3
Requires: rubygem(bundler_ext)

Requires: wget
Requires: /etc/cron.d
Requires: gawk
Requires(pre):  shadow-utils
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units

# Subpackages
Requires: %{name}-debug

# start specfile default Requires
Requires: rubygem(rails) >= 6.1.6.1
Requires: rubygem(rails) < 6.1.7.0
Requires: rubygem(rest-client) >= 2.0.0
Requires: rubygem(rest-client) < 3
Requires: rubygem(audited) >= 4.9.0
Requires: rubygem(audited) < 5
Requires: rubygem(will_paginate) >= 3.1.7
Requires: rubygem(will_paginate) < 4
Requires: rubygem(ancestry) >= 3.0.7
Requires: rubygem(ancestry) < 4
Requires: rubygem(scoped_search) >= 4.1.8
Requires: rubygem(scoped_search) < 5
Requires: rubygem(ldap_fluff) >= 0.5.0
Requires: rubygem(ldap_fluff) < 1.0
Requires: rubygem(apipie-rails) >= 0.5.17
Requires: rubygem(apipie-rails) < 0.6.0
Requires: rubygem(apipie-dsl) >= 2.2.6
Requires: rubygem(rdoc) < 6.4
Requires: rubygem(rabl) >= 0.15.0
Requires: rubygem(rabl) < 1
Requires: rubygem(oauth) >= 0.5.4
Requires: rubygem(oauth) < 1
Requires: rubygem(deep_cloneable) >= 3
Requires: rubygem(deep_cloneable) < 4
Requires: rubygem(validates_lengths_from_database) >= 0.5
Requires: rubygem(validates_lengths_from_database) < 1.0
Requires: rubygem(friendly_id) >= 5.4.2
Requires: rubygem(friendly_id) < 6
Requires: rubygem(secure_headers) >= 6.3
Requires: rubygem(secure_headers) < 7.0
Requires: rubygem(safemode) >= 1.3.5
Requires: rubygem(safemode) < 2
Requires: rubygem(fast_gettext) >= 1.4
Requires: rubygem(fast_gettext) < 2.0
Requires: rubygem(gettext_i18n_rails) >= 1.8
Requires: rubygem(gettext_i18n_rails) < 2.0
Requires: rubygem(rails-i18n) >= 6.0
Requires: rubygem(rails-i18n) < 7.0
Requires: rubygem(i18n) >= 1.1
Requires: rubygem(i18n) < 2.0
Requires: rubygem(logging) >= 1.8.0
Requires: rubygem(logging) < 3.0.0
Requires: rubygem(fog-core) >= 2.1
Requires: rubygem(fog-core) < 3.0
Requires: rubygem(net-scp)
Requires: rubygem(net-ssh)
Requires: rubygem(net-ldap) >= 0.16.0
Requires: rubygem(net-ping)
Requires: rubygem(activerecord-session_store) >= 2.0.0
Requires: rubygem(activerecord-session_store) < 3
Requires: rubygem(sprockets) >= 4.0
Requires: rubygem(sprockets) < 5.0
Requires: rubygem(sprockets-rails) >= 3.0
Requires: rubygem(sprockets-rails) < 4.0
Requires: rubygem(responders) >= 3.0
Requires: rubygem(responders) < 4.0
Requires: rubygem(roadie-rails) >= 2.0
Requires: rubygem(roadie-rails) < 3.0
Requires: rubygem(deacon) >= 1.0
Requires: rubygem(deacon) < 2.0
Requires: rubygem(webpack-rails) >= 0.9.8
Requires: rubygem(webpack-rails) < 0.10.0
Requires: rubygem(mail) >= 2.7
Requires: rubygem(mail) < 3.0
Requires: rubygem(sshkey) >= 1.9
Requires: rubygem(sshkey) < 2.0
Requires: rubygem(dynflow) >= 1.6.5
Requires: rubygem(dynflow) < 2.0.0
Requires: rubygem(daemons)
Requires: rubygem(bcrypt) >= 3.1
Requires: rubygem(bcrypt) < 4.0
Requires: rubygem(get_process_mem)
Requires: rubygem(rack-cors) >= 1.0.2
Requires: rubygem(rack-cors) < 1.1.0
Requires: rubygem(jwt) >= 2.2.2
Requires: rubygem(jwt) < 2.3.0
Requires: rubygem(graphql) >= 1.8.0
Requires: rubygem(graphql) < 1.9.0
Requires: rubygem(graphql-batch)
# end specfile default Requires

Requires: rubygem(bigdecimal)

# start specfile facter Requires
Requires: rubygem(facter)
# end specfile facter Requires

# start specfile jsonp Requires
Requires: rubygem(rack-jsonp)
# end specfile jsonp Requires

# Build dependencies
%{?systemd_requires}
BuildRequires: asciidoc
BuildRequires: rubygem(bigdecimal)
BuildRequires: gettext
BuildRequires: /usr/bin/ruby
BuildRequires: rubygems
BuildRequires: rubygem(rake) >= 0.8.3
BuildRequires: rubygem(bundler_ext)

# start specfile default BuildRequires
BuildRequires: rubygem(rails) >= 6.1.6.1
BuildRequires: rubygem(rails) < 6.1.7.0
BuildRequires: rubygem(rest-client) >= 2.0.0
BuildRequires: rubygem(rest-client) < 3
BuildRequires: rubygem(audited) >= 4.9.0
BuildRequires: rubygem(audited) < 5
BuildRequires: rubygem(will_paginate) >= 3.1.7
BuildRequires: rubygem(will_paginate) < 4
BuildRequires: rubygem(ancestry) >= 3.0.7
BuildRequires: rubygem(ancestry) < 4
BuildRequires: rubygem(scoped_search) >= 4.1.8
BuildRequires: rubygem(scoped_search) < 5
BuildRequires: rubygem(ldap_fluff) >= 0.5.0
BuildRequires: rubygem(ldap_fluff) < 1.0
BuildRequires: rubygem(apipie-rails) >= 0.5.17
BuildRequires: rubygem(apipie-rails) < 0.6.0
BuildRequires: rubygem(apipie-dsl) >= 2.2.6
BuildRequires: rubygem(rdoc) < 6.4
BuildRequires: rubygem(rabl) >= 0.15.0
BuildRequires: rubygem(rabl) < 1
BuildRequires: rubygem(oauth) >= 0.5.4
BuildRequires: rubygem(oauth) < 1
BuildRequires: rubygem(deep_cloneable) >= 3
BuildRequires: rubygem(deep_cloneable) < 4
BuildRequires: rubygem(validates_lengths_from_database) >= 0.5
BuildRequires: rubygem(validates_lengths_from_database) < 1.0
BuildRequires: rubygem(friendly_id) >= 5.4.2
BuildRequires: rubygem(friendly_id) < 6
BuildRequires: rubygem(secure_headers) >= 6.3
BuildRequires: rubygem(secure_headers) < 7.0
BuildRequires: rubygem(safemode) >= 1.3.5
BuildRequires: rubygem(safemode) < 2
BuildRequires: rubygem(fast_gettext) >= 1.4
BuildRequires: rubygem(fast_gettext) < 2.0
BuildRequires: rubygem(gettext_i18n_rails) >= 1.8
BuildRequires: rubygem(gettext_i18n_rails) < 2.0
BuildRequires: rubygem(rails-i18n) >= 6.0
BuildRequires: rubygem(rails-i18n) < 7.0
BuildRequires: rubygem(i18n) >= 1.1
BuildRequires: rubygem(i18n) < 2.0
BuildRequires: rubygem(logging) >= 1.8.0
BuildRequires: rubygem(logging) < 3.0.0
BuildRequires: rubygem(fog-core) >= 2.1
BuildRequires: rubygem(fog-core) < 3.0
BuildRequires: rubygem(net-scp)
BuildRequires: rubygem(net-ssh)
BuildRequires: rubygem(net-ldap) >= 0.16.0
BuildRequires: rubygem(net-ping)
BuildRequires: rubygem(activerecord-session_store) >= 2.0.0
BuildRequires: rubygem(activerecord-session_store) < 3
BuildRequires: rubygem(sprockets) >= 4.0
BuildRequires: rubygem(sprockets) < 5.0
BuildRequires: rubygem(sprockets-rails) >= 3.0
BuildRequires: rubygem(sprockets-rails) < 4.0
BuildRequires: rubygem(responders) >= 3.0
BuildRequires: rubygem(responders) < 4.0
BuildRequires: rubygem(roadie-rails) >= 2.0
BuildRequires: rubygem(roadie-rails) < 3.0
BuildRequires: rubygem(deacon) >= 1.0
BuildRequires: rubygem(deacon) < 2.0
BuildRequires: rubygem(webpack-rails) >= 0.9.8
BuildRequires: rubygem(webpack-rails) < 0.10.0
BuildRequires: rubygem(mail) >= 2.7
BuildRequires: rubygem(mail) < 3.0
BuildRequires: rubygem(sshkey) >= 1.9
BuildRequires: rubygem(sshkey) < 2.0
BuildRequires: rubygem(dynflow) >= 1.6.5
BuildRequires: rubygem(dynflow) < 2.0.0
BuildRequires: rubygem(daemons)
BuildRequires: rubygem(bcrypt) >= 3.1
BuildRequires: rubygem(bcrypt) < 4.0
BuildRequires: rubygem(get_process_mem)
BuildRequires: rubygem(rack-cors) >= 1.0.2
BuildRequires: rubygem(rack-cors) < 1.1.0
BuildRequires: rubygem(jwt) >= 2.2.2
BuildRequires: rubygem(jwt) < 2.3.0
BuildRequires: rubygem(graphql) >= 1.8.0
BuildRequires: rubygem(graphql) < 1.9.0
BuildRequires: rubygem(graphql-batch)
BuildRequires: rubygem(activerecord-nulldb-adapter)
# end specfile default BuildRequires

# assets
BuildRequires: nodejs-packaging
BuildRequires: nodejs >= 14
BuildRequires: http-parser
BuildRequires: systemd

# start package.json devDependencies BuildRequires
BuildRequires: npm(@babel/core) >= 7.7.0
BuildRequires: npm(@babel/core) < 8.0.0
BuildRequires: npm(@theforeman/builder) >= 10.1.0
BuildRequires: npm(@theforeman/builder) < 11.0.0
BuildRequires: npm(argv-parse) >= 1.0.1
BuildRequires: npm(argv-parse) < 2.0.0
BuildRequires: npm(babel-loader) >= 8.0.0
BuildRequires: npm(babel-loader) < 9.0.0
BuildRequires: npm(compression-webpack-plugin) >= 1.1.11
BuildRequires: npm(compression-webpack-plugin) < 1.2.0
BuildRequires: npm(css-loader) >= 0.23.1
BuildRequires: npm(css-loader) < 1.0.0
BuildRequires: npm(cssnano) >= 4.1.10
BuildRequires: npm(cssnano) < 5.0.0
BuildRequires: npm(dotenv) >= 5.0.0
BuildRequires: npm(dotenv) < 6.0.0
BuildRequires: npm(expose-loader) >= 0.6.0
BuildRequires: npm(expose-loader) < 0.7.0
BuildRequires: npm(extract-text-webpack-plugin) >= 3.0.0
BuildRequires: npm(extract-text-webpack-plugin) < 4.0.0
BuildRequires: npm(file-loader) >= 0.9.0
BuildRequires: npm(file-loader) < 1.0.0
BuildRequires: npm(graphql) >= 15.5.0
BuildRequires: npm(graphql) < 16.0.0
BuildRequires: npm(node-sass) >= 4.5.0
BuildRequires: npm(node-sass) < 5.0.0
BuildRequires: npm(optimize-css-assets-webpack-plugin) >= 3.2.0
BuildRequires: npm(optimize-css-assets-webpack-plugin) < 4.0.0
BuildRequires: npm(sass-loader) >= 6.0.6
BuildRequires: npm(sass-loader) < 6.1.0
BuildRequires: npm(style-loader) >= 0.13.1
BuildRequires: npm(style-loader) < 1.0.0
BuildRequires: npm(uglifyjs-webpack-plugin) >= 1.2.2
BuildRequires: npm(uglifyjs-webpack-plugin) < 2.0.0
BuildRequires: npm(url-loader) >= 1.0.1
BuildRequires: npm(url-loader) < 2.0.0
BuildRequires: npm(webpack) >= 3.4.1
BuildRequires: npm(webpack) < 4.0.0
BuildRequires: npm(webpack-stats-plugin) >= 0.1.5
BuildRequires: npm(webpack-stats-plugin) < 1.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: npm(@theforeman/vendor) >= 10.1.0
BuildRequires: npm(@theforeman/vendor) < 11.0.0
BuildRequires: npm(graphql-tag) >= 2.11.0
BuildRequires: npm(graphql-tag) < 3.0.0
BuildRequires: npm(intl) >= 1.2.5
BuildRequires: npm(intl) < 1.3.0
BuildRequires: npm(jed) >= 1.1.1
BuildRequires: npm(jed) < 2.0.0
BuildRequires: npm(react-intl) >= 2.8.0
BuildRequires: npm(react-intl) < 3.0.0
# end package.json dependencies BuildRequires

# start specfile assets BuildRequires
BuildRequires: rubygem(jquery-ui-rails) >= 6.0
BuildRequires: rubygem(jquery-ui-rails) < 7.0
BuildRequires: rubygem(patternfly-sass) >= 3.59.4
BuildRequires: rubygem(patternfly-sass) < 3.60.0
BuildRequires: rubygem(gettext_i18n_rails_js) >= 1.3.1
BuildRequires: rubygem(gettext_i18n_rails_js) < 1.4.0
BuildRequires: rubygem(execjs) >= 1.4.0
BuildRequires: rubygem(execjs) < 3.0
BuildRequires: rubygem(uglifier) >= 1.0.3
BuildRequires: rubygem(sass-rails) >= 6.0
BuildRequires: rubygem(sass-rails) < 7.0
BuildRequires: rubygem(coffee-rails) >= 5.0.0
BuildRequires: rubygem(coffee-rails) < 5.1.0
# end specfile assets BuildRequires

# start specfile facter BuildRequires
BuildRequires: rubygem(facter)
# end specfile facter BuildRequires


%package cli
Summary: Foreman CLI
Group: Applications/System
Requires: rubygem(hammer_cli_foreman)

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
Requires: rubygem(fog-libvirt) >= 0.9.0
Requires: rubygem(ruby-libvirt) >= 0.5
Requires: rubygem(ruby-libvirt) < 1.0
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
Requires: rubygem(fog-openstack) >= 1.0.8
Requires: rubygem(fog-openstack) < 2.0.0
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
Requires: rubygem(fog-ovirt) >= 2.0.1
Requires: rubygem(fog-ovirt) < 3
# end specfile ovirt Requires
Requires: %{name} = %{version}-%{release}

%description ovirt
Meta package to install requirements for oVirt compute resource support.

%files ovirt
%{_datadir}/%{name}/bundler.d/ovirt.rb

%package ec2
Summary:   Foreman Amazon Web Services (AWS) EC2 support
Group:     Applications/System
# start specfile ec2 Requires
Requires: rubygem(fog-aws) >= 3.6.2
Requires: rubygem(fog-aws) < 4
# end specfile ec2 Requires
Requires:  %{name} = %{version}-%{release}

%description ec2
Meta package to install requirements for Amazon Web Services (AWS) EC2 support.

%files ec2
%{_datadir}/%{name}/bundler.d/ec2.rb

%package vmware
Summary: Foreman VMware support
Group:  Applications/System
# start specfile vmware Requires
Requires: rubygem(fog-vsphere) >= 3.5.0
Requires: rubygem(fog-vsphere) < 4.0
Requires: rubygem(rbvmomi) >= 2.0
Requires: rubygem(rbvmomi) < 3.0
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
Requires: rubygem(fog-google) >= 1.14
Requires: rubygem(fog-google) < 2.0
Requires: rubygem(faraday) < 2
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
Requires: nodejs >= 14

# start package.json devDependencies Requires
Requires: npm(@babel/core) >= 7.7.0
Requires: npm(@babel/core) < 8.0.0
Requires: npm(@theforeman/builder) >= 10.1.0
Requires: npm(@theforeman/builder) < 11.0.0
Requires: npm(argv-parse) >= 1.0.1
Requires: npm(argv-parse) < 2.0.0
Requires: npm(babel-loader) >= 8.0.0
Requires: npm(babel-loader) < 9.0.0
Requires: npm(compression-webpack-plugin) >= 1.1.11
Requires: npm(compression-webpack-plugin) < 1.2.0
Requires: npm(css-loader) >= 0.23.1
Requires: npm(css-loader) < 1.0.0
Requires: npm(cssnano) >= 4.1.10
Requires: npm(cssnano) < 5.0.0
Requires: npm(dotenv) >= 5.0.0
Requires: npm(dotenv) < 6.0.0
Requires: npm(expose-loader) >= 0.6.0
Requires: npm(expose-loader) < 0.7.0
Requires: npm(extract-text-webpack-plugin) >= 3.0.0
Requires: npm(extract-text-webpack-plugin) < 4.0.0
Requires: npm(file-loader) >= 0.9.0
Requires: npm(file-loader) < 1.0.0
Requires: npm(graphql) >= 15.5.0
Requires: npm(graphql) < 16.0.0
Requires: npm(node-sass) >= 4.5.0
Requires: npm(node-sass) < 5.0.0
Requires: npm(optimize-css-assets-webpack-plugin) >= 3.2.0
Requires: npm(optimize-css-assets-webpack-plugin) < 4.0.0
Requires: npm(sass-loader) >= 6.0.6
Requires: npm(sass-loader) < 6.1.0
Requires: npm(style-loader) >= 0.13.1
Requires: npm(style-loader) < 1.0.0
Requires: npm(uglifyjs-webpack-plugin) >= 1.2.2
Requires: npm(uglifyjs-webpack-plugin) < 2.0.0
Requires: npm(url-loader) >= 1.0.1
Requires: npm(url-loader) < 2.0.0
Requires: npm(webpack) >= 3.4.1
Requires: npm(webpack) < 4.0.0
Requires: npm(webpack-stats-plugin) >= 0.1.5
Requires: npm(webpack-stats-plugin) < 1.0.0
# end package.json devDependencies Requires

# start package.json dependencies Requires
Requires: npm(@theforeman/vendor) >= 10.1.0
Requires: npm(@theforeman/vendor) < 11.0.0
Requires: npm(graphql-tag) >= 2.11.0
Requires: npm(graphql-tag) < 3.0.0
Requires: npm(intl) >= 1.2.5
Requires: npm(intl) < 1.3.0
Requires: npm(jed) >= 1.1.1
Requires: npm(jed) < 2.0.0
Requires: npm(react-intl) >= 2.8.0
Requires: npm(react-intl) < 3.0.0
# end package.json dependencies Requires

# start specfile assets Requires
Requires: rubygem(jquery-ui-rails) >= 6.0
Requires: rubygem(jquery-ui-rails) < 7.0
Requires: rubygem(patternfly-sass) >= 3.59.4
Requires: rubygem(patternfly-sass) < 3.60.0
Requires: rubygem(gettext_i18n_rails_js) >= 1.3.1
Requires: rubygem(gettext_i18n_rails_js) < 1.4.0
Requires: rubygem(execjs) >= 1.4.0
Requires: rubygem(execjs) < 3.0
Requires: rubygem(uglifier) >= 1.0.3
Requires: rubygem(sass-rails) >= 6.0
Requires: rubygem(sass-rails) < 7.0
Requires: rubygem(coffee-rails) >= 5.0.0
Requires: rubygem(coffee-rails) < 5.1.0
# end specfile assets Requires

%description assets
Meta package to install asset pipeline support.

%files assets
%{_datadir}/%{name}/bundler.d/assets.rb
%{_datadir}/%{name}/webpack
%{_datadir}/%{name}/.babelrc.js
%{_datadir}/%{name}/script/npm*
%{_datadir}/%{name}/script/plugin_webpack*
%{_datadir}/%{name}/script/webpack-analyze*

%package plugin
Summary: Foreman plugin support
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-build = %{version}-%{release}
Requires: rubygem(activerecord-nulldb-adapter)

%description plugin
Meta package with support for plugins.

%files plugin
%{_sysconfdir}/rpm/macros.%{name}-plugin
%{_datadir}/%{name}/schema.rb.nulldb
%{_datadir}/%{name}/bundler.d/nulldb.rb

%package build
Summary: Foreman package RPM support
Group: Development/Libraries

%description build
Meta package with support for building RPMs in the Foreman release cycle.

%files build
%{_sysconfdir}/rpm/macros.%{name}-dist

%package console
Summary: Foreman console support
Group:  Applications/System
# start specfile console Requires
Requires: rubygem(wirb) >= 1.0
Requires: rubygem(wirb) < 3.0
Requires: rubygem(amazing_print) >= 1.1
Requires: rubygem(amazing_print) < 2.0
# end specfile console Requires
Requires: %{name} = %{version}-%{release}

%description console
Meta Package to install requirements for console support

%files console
%{_datadir}/%{name}/bundler.d/console.rb

%package postgresql
Summary: Foreman Postgresql support
Group:  Applications/System
# start specfile postgresql Requires
Requires: rubygem(pg) >= 0.18
Requires: rubygem(pg) < 2.0
# end specfile postgresql Requires
Requires: %{name} = %{version}-%{release}

# On EL8 and Fedora the locales are not present by default. Since the installer
# installs with the en_US.UTF-8 locale, this is needed in most cases and
# doesn't hurt in others.
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires: glibc-langpack-en
%endif

%description postgresql
Meta Package to install requirements for postgresql support

%files postgresql
%{_datadir}/%{name}/bundler.d/postgresql.rb

%package telemetry
Summary: Foreman telemetry support
Group:  Applications/System
# start specfile telemetry Requires
Requires: rubygem(prometheus-client) >= 1.0
Requires: rubygem(prometheus-client) < 2.0
Requires: rubygem(statsd-instrument) < 3
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
Requires: rubygem(logging-journald) >= 2.0
Requires: rubygem(logging-journald) < 3.0
# end specfile journald Requires
Requires: %{name} = %{version}-%{release}

%description journald
Meta Package to install requirements for journald logging support

%files journald
%{_datadir}/%{name}/bundler.d/journald.rb

%package redis
Summary: Foreman Redis caching support
Group:  Applications/System
# start specfile redis Requires
Requires: rubygem(redis) >= 4.0
Requires: rubygem(redis) < 5.0
# end specfile redis Requires
Requires: %{name} = %{version}-%{release}

%description redis
Meta Package to install requirements for Redis caching support

%files redis
%{_datadir}/%{name}/bundler.d/redis.rb

%package dynflow-sidekiq
Summary: Foreman Dynflow's Sidekiq executor
Group:  Applications/System
# start specfile dynflow_sidekiq Requires
Requires: rubygem(sidekiq) >= 5.0
Requires: rubygem(sidekiq) < 6.0
Requires: rubygem(gitlab-sidekiq-fetcher)
Requires: rubygem(sd_notify) >= 0.1
Requires: rubygem(sd_notify) < 1.0
# end specfile dynflow_sidekiq Requires
Requires: %{name} = %{version}-%{release}

%description dynflow-sidekiq
Meta Package to install dynflow sidekiq executor support

%files dynflow-sidekiq
%{_datadir}/%{name}/bundler.d/dynflow_sidekiq.rb
%{_unitdir}/%{dynflow_sidekiq_service_name}.service
%{_datadir}/%{name}/extras/dynflow-sidekiq.rb

%post dynflow-sidekiq
%systemd_post %{dynflow_sidekiq_service_name}.service

%preun dynflow-sidekiq
%systemd_preun %{dynflow_sidekiq_service_name}.service

%postun dynflow-sidekiq
%systemd_postun_with_restart %{dynflow_sidekiq_service_name}.service

%package service
Summary: Foreman systemd service support
Group:  Applications/System
# start specfile service Requires
Requires: rubygem(puma) >= 5.1
Requires: rubygem(puma) < 6.0
# end specfile service Requires
Requires: rubygem(puma-status)
Requires: %{name} = %{version}-%{release}

%description service
Meta Package to install requirements for Foreman service

%files service
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_datadir}/%{name}/bundler.d/service.rb
%{_sbindir}/%{name}-puma-status

%description
Foreman is aimed to be a Single Address For All Machines Life Cycle Management.
Foreman is based on Ruby on Rails, and this package bundles Rails and all
plugins required for Foreman to work.

%prep
%setup -q -n %{name}-%{version}%{?prerelease:-}%{?prerelease}

%build
#build man pages
%{rake} -f Rakefile.dist build \
  PREFIX=%{_prefix} \
  SBINDIR=%{_sbindir} \
  SYSCONFDIR=%{_sysconfdir} \
  --trace

# sidekiq service SELinux helper path update
sed -i '/^ExecStart/ s|/usr/bin/sidekiq \(.\+\)$|%{_libexecdir}/%{name}/sidekiq-selinux \1|' extras/systemd/%{dynflow_sidekiq_service_name}.service

#build locale files
make -C locale all-mo

#use Bundler_ext instead of Bundler
mv Gemfile Gemfile.in
cp db/schema.rb.nulldb db/schema.rb
export BUNDLER_EXT_GROUPS="default assets"
ln -s %{nodejs_sitelib} node_modules
# Calls webpack manually since webpack:compile uses the config which uses
# node_modules/.bin/webpack and that doesn't exist in our setup
export NODE_ENV=production
webpack --bail --config config/webpack.config.js
%{rake} assets:precompile RAILS_ENV=production DATABASE_URL=nulldb://nohost --trace
rm db/schema.rb

%install
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|g' extras/noVNC/*.py
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|g' extras/noVNC/websockify/*.py
%endif

rm -rf %{buildroot}

#install man pages
%{rake} -f Rakefile.dist install \
  PREFIX=%{buildroot}%{_prefix} \
  SBINDIR=%{buildroot}%{_sbindir} \
  SYSCONFDIR=%{buildroot}%{_sysconfdir} \
  --trace
%{rake} -f Rakefile.dist clean

install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}/plugins
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/plugins
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/dynflow
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp/pids
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}/plugins
install -d -m0755 %{buildroot}%{_libexecdir}/%{name}
#Copy init scripts and sysconfigs
install -Dp -m0644 extras/systemd/%{dynflow_sidekiq_service_name}.service %{buildroot}%{_unitdir}/%{dynflow_sidekiq_service_name}.service
install -Dp -m0755 script/%{name}-debug %{buildroot}%{_sbindir}/%{name}-debug
install -Dp -m0755 script/%{name}-rake %{buildroot}%{_sbindir}/%{name}-rake
install -Dp -m0755 script/%{name}-tail %{buildroot}%{_sbindir}/%{name}-tail
install -Dp -m0755 script/%{name}-puma-status %{buildroot}%{_sbindir}/%{name}-puma-status
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dp -m0644 extras/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m0644 extras/systemd/%{name}.socket %{buildroot}%{_unitdir}/%{name}.socket

# SELinux libexec wrappers
cat > %{buildroot}%{_libexecdir}/%{name}/sidekiq-selinux <<EOF
#!/bin/bash
# Shell wrapper with SELinux transition into foreman_rails_t domain.
exec sidekiq "\$@"
EOF

cp -p Gemfile.in %{buildroot}%{_datadir}/%{name}/Gemfile.in
cp -p -r app bin bundler.d config config.ru extras lib locale Rakefile script webpack .babelrc.js %{buildroot}%{_datadir}/%{name}
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

for i in orchestrator worker; do
  mv %{buildroot}%{_datadir}/%{name}/config/dynflow/$i.yml.example %{buildroot}%{_datadir}/%{name}/config/dynflow/$i.yml
  mv %{buildroot}%{_datadir}/%{name}/config/dynflow/$i.yml %{buildroot}%{_sysconfdir}/%{name}/dynflow/
  ln -sv %{_sysconfdir}/%{name}/dynflow/$i.yml %{buildroot}%{_datadir}/%{name}/config/dynflow/$i.yml
done

# Put db in %{_localstatedir}/lib/%{name}/db
cp -pr db/schema.rb.nulldb db/migrate db/seeds.rb db/seeds.d %{buildroot}%{_datadir}/%{name}
mkdir %{buildroot}%{_localstatedir}/lib/%{name}/db

ln -sv %{_localstatedir}/lib/%{name}/db %{buildroot}%{_datadir}/%{name}/db
ln -sv %{_datadir}/%{name}/migrate %{buildroot}%{_localstatedir}/lib/%{name}/db/migrate
ln -sv %{_datadir}/%{name}/seeds.rb %{buildroot}%{_localstatedir}/lib/%{name}/db/seeds.rb
ln -sv %{_datadir}/%{name}/seeds.d %{buildroot}%{_localstatedir}/lib/%{name}/db/seeds.d
ln -sv %{_datadir}/%{name}/schema.rb.nulldb %{buildroot}%{_localstatedir}/lib/%{name}/db/schema.rb.nulldb

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
EOF

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
%%%{name}_assets_foreman %%{foreman_dir}/public/assets/%%{gem_name}
# Common webpack locations
%%%{name}_webpack_plugin %%{gem_instdir}/public/webpack/%%{gem_name}
%%%{name}_webpack_foreman %%{foreman_dir}/public/webpack/%%{gem_name}
# Common apipie locations
%%%{name}_apipie_cache_plugin %%{gem_instdir}/public/apipie-cache/plugin/%%{gem_name}
%%%{name}_apipie_cache_foreman %%{foreman_dir}/public/apipie-cache/plugin/%%{gem_name}
# build apipie cache index
%%%{name}_apipie_cache %%{%{name}_rake} apipie:cache:index >> %%{%{name}_log_dir}/apipie_cache.log 2>&1 || :
# log plugin installation
%%%{name}_plugin_log \\
echo %%{gem_name} >> %%{foreman_dir}/tmp/restart_required_changed_plugins || : \\
chown foreman:foreman %%{foreman_dir}/tmp/restart_required_changed_plugins || :

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
pushd ./%%{%{name}_dir} \\
mkdir db/ \\
cp -rf %{_datadir}/%{name}/db/* db/ \\
mv db/schema.rb.nulldb db/schema.rb \\
\\
ln -s %{nodejs_sitelib} node_modules \\
export GEM_PATH=%%{buildroot}%%{gem_dir}:\${GEM_PATH:+\${GEM_PATH}}\${GEM_PATH:-\`ruby -e "print Gem.path.join(':')"\`} \\
unlink tmp \\
\\
rm \`pwd\`/config/initializers/encryption_key.rb \\
rm \`pwd\`/config/database.yml \\
%{rake} security:generate_encryption_key \\
export BUNDLER_EXT_NOSTRICT=1 \\
export NODE_ENV=production \\
cp %%{buildroot}%%{%{name}_bundlerd_dir}/%%{gem_name}.rb ./bundler.d/%%{gem_name}.rb \\
%%{?-s:%{rake} %%{-r*}%%{!?-r:plugin:assets:precompile[%%{-n*}%%{!?-n:%%{gem_name}}]} RAILS_ENV=production DATABASE_URL=nulldb://nohost --trace} \\
%%{?-a:%{rake} plugin:apipie:cache[%%{gem_name}] FOREMAN_APIPIE_LANGS=en_US RAILS_ENV=production cache_part=resources OUT=%%{buildroot}%%{%{name}_apipie_cache_plugin} DATABASE_URL=nulldb://nohost --trace} \\
\\
popd \\
rm -rf ./usr \\
%%{?-a:mkdir -p %%{buildroot}%%{foreman_dir}/public/apipie-cache/plugin} \\
%%{?-a:ln -s %%{%{name}_apipie_cache_plugin} %%{buildroot}%%{%{name}_apipie_cache_foreman}} \\
%%{?-s:[ -e %%{buildroot}%%{%{name}_assets_plugin} ] && mkdir -p %%{buildroot}%%{foreman_dir}/public/assets} \\
%%{?-s:[ -e %%{buildroot}%%{%{name}_assets_plugin} ] && ln -s %%{%{name}_assets_plugin} %%{buildroot}%%{%{name}_assets_foreman}} \\
%%{?-s:[ -e %%{buildroot}%%{%{name}_webpack_plugin} ] && mkdir -p %%{buildroot}%%{foreman_dir}/public/webpack} \\
%%{?-s:[ -e %%{buildroot}%%{%{name}_webpack_plugin} ] && ln -s %%{%{name}_webpack_plugin} %%{buildroot}%%{%{name}_webpack_foreman}} \\
%%{?-s:rm -f %%{buildroot}%%{%{name}_webpack_plugin}/*.js.map} \\
%%{?-s:rm -f %%{buildroot}%%{gem_instdir}/public/webpack/foreman-vendor.*} \\
%%{?-s:rm -rf %%{buildroot}%%{gem_instdir}/public/webpack/fonts} \\
%%{?-s:rm -rf %%{buildroot}%%{gem_instdir}/public/webpack/images}
EOF


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc CHANGELOG Contributors README.md VERSION
%license LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/app
%{_datadir}/%{name}/app/assets/config/manifest.js
%exclude %{_datadir}/%{name}/app/assets/images
%exclude %{_datadir}/%{name}/app/assets/stylesheets
%exclude %{_datadir}/%{name}/app/assets/javascripts
%exclude %{_datadir}/%{name}/script/%{name}-debug.d
%exclude %{_datadir}/%{name}/script/%{name}-puma-status
%exclude %{_datadir}/%{name}/script/%{name}-rake
%exclude %{_datadir}/%{name}/script/%{name}-tail
%exclude %{_datadir}/%{name}/script/npm*
%exclude %{_datadir}/%{name}/script/plugin_webpack*
%exclude %{_datadir}/%{name}/script/webpack-analyze*
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
%exclude %{_datadir}/%{name}/extras/systemd
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
%attr(755,root,root) %{_libexecdir}/%{name}/*
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

%pre
# Add the "foreman" user and group
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{homedir} -s /sbin/nologin -c "Foreman" %{name}

if [ $1 == 2 ]; then
  systemctl --no-reload disable dynflowd.service > /dev/null 2>&1 || :
  systemctl stop dynflowd.service > /dev/null 2>&1 || :
fi
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

# Enforce tmpfiles run
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
exit 0

%post service
%systemd_post %{name}.socket %{name}.service

%preun service
%systemd_preun %{name}.socket %{name}.service

%postun service
%systemd_postun_with_restart %{name}.service
%systemd_postun %{name}.socket

%changelog
* Thu Aug 25 2022 Patrick Creech <pcreech@redhat.com> - 3.4.0-0.7.rc2
- Release foreman 3.4.0rc2

* Tue Aug 23 2022 Evgeni Golov - 3.4.0-0.7.rc1
- Refs #35409 - Include sprockets-based assets in plugin macros

* Thu Aug 11 2022 Patrick Creech <pcreech@redhat.com> - 3.4.0-0.6.rc1
- Release foreman 3.4.0rc1

* Wed Aug 03 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.4.0-0.6.develop
- Update Gem and NPM dependencies

* Fri Jul 15 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.4.0-0.5.develop
- Remove SCL compatibility macros
- Update Rails dependency

* Wed Jul 13 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.4.0-0.4.develop
- Update Gem and NPM dependencies

* Tue May 24 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.4.0-0.3.develop
- Update to Rails 6.1

* Mon May 23 2022 Evgeni Golov - 3.4.0-0.2.develop
- Update Foreman GEM requirements

* Tue May 10 2022 Odilon Sousa <osousa@redhat.com> - 3.4.0-0.1.develop
- Bump version to 3.4-develop

* Mon May 02 2022 Evgeni Golov - 3.3.0-0.5.develop
- Refs #34602 - log plugin installations

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.3.0-0.4.develop
- Stop generating apipie cache for Foreman

* Wed Mar 23 2022 Evgeni Golov - 3.3.0-0.3.develop
- Update foreman GEM dependencies

* Wed Feb 23 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.3.0-0.2.develop
- Drop accidental nodejs dependency by moving files
- Exclude redundant systemd files

* Thu Feb 10 2022 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.0-0.1.develop
- Bump version to 3.3-develop

* Tue Jan 25 2022 Evgeni Golov - 3.2.0-0.3.develop
- Update Gem and NPM dependencies

* Thu Dec 16 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.2.0-0.2.develop
- Build plugin apipie:cache with production Rails environment

* Fri Nov 12 2021 Odilon Sousa <osousa@redhat.com> - 3.2.0-0.1.develop
- Bump version to 3.2-develop

* Thu Aug 05 2021 Patrick Creech <pcreech@redhat.com> - 3.1.0-0.1.develop
- Bump version to 3.1-develop

* Thu Jul 22 2021 Tomer Brisker <tbrisker@gmail.com> - 3.0.0-0.1.develop
- Bump version to 3.0-develop

* Wed Jun 02 2021 Amir Feferkuchen <afeferku@redhat.com> - 2.6.0-0.2.develop
- Update NPM dependencies

* Tue May 04 2021 Zach Huntington-Meath <zhunting@redhat.com> - 2.6.0-0.1.develop
- Bump version to 2.6-develop

* Fri Apr 30 2021 Evgeni Golov - 2.5.0-0.8.develop
- Update depdendencies

* Wed Apr 28 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.5.0-0.7.develop
- Use rubygem-activerecord-session_store 2+

* Wed Apr 21 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.5.0-0.6.develop
- Add foreman-puma-status support

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.5.0-0.5.develop
- Rebuild for Ruby 2.7

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.5.0-0.4.develop
- Add timestamps to cron jobs

* Wed Mar 10 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.5.0-0.3.develop
- Update Gem and NPM dependencies

* Mon Feb 08 2021 Ondrej Prazak <oprazak@redhat.com> - 2.5.0-0.2.develop
- Bump @theforeman/vendor

* Tue Feb 02 2021 Evgeni Golov - 2.5.0-0.1.develop
- Bump version to 2.5-develop

* Thu Jan 07 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.4.0-0.4.develop
- Update puma dependency (#31431)

* Mon Dec 28 2020 Tomer Brisker <tbrisker@gmail.com> - 2.4.0-0.3.develop
- Update Gem dependencies

* Wed Nov 18 2020 Tomer Brisker <tbrisker@gmail.com> - 2.4.0-0.2.develop
- Update NPM dependencies

* Mon Nov 02 2020 Patrick Creech <pcreech@redhat.com> - 2.4.0-0.1.develop
- Bump version to 2.4-develop

* Sun Oct 25 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-0.7.develop
- Update Gem and NPM dependencies

* Tue Sep 29 2020 Ondrej Ezr <ezrik12@gmail.com> - 2.3.0-0.6.develop
- Clean up cron file

* Thu Sep 24 2020 Evgeni Golov - 2.3.0-0.5.develop
- Update GEM dependencies

* Fri Sep 04 2020 Lukas Zapletal <lzap+rpm@redhat.com> - 2.3.0-0.4.develop
- Enforce tmpfiles

* Mon Aug 31 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-0.3.develop
- Update Gem and NPM dependencies

* Sat Aug 29 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-0.2.develop
- Add puma-plugin-systemd to service subpackage requires

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-0.1.develop
- Bump version to 2.3-develop

* Wed Aug 05 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.30.develop
- Only generate en_US apipie docs for Foreman and Plugins

* Wed Jul 29 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.29.develop
- Ensure foreman.socket is removed on package removal

* Mon Jul 20 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.0-0.28.develop
- Update Gem and NPM dependencies

* Mon Jun 22 2020 Avi Sharvit <sharvita@gmail.com> - 2.2.0-0.27.develop
- Update foreman-js dependencies

* Fri Jun 19 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.26.develop
- Include manifest.js in Foreman RPM

* Fri Jun 19 2020 Michael Moll <mmoll@mmoll.at> - 2.2.0-0.25.develop
- Update sprockets dependency

* Mon Jun 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.24.develop
- Update Rails to 6.0.3.1

* Wed Jun 10 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.23.develop
- Ensure socket gets handled with service

* Thu May 21 2020 Lukas Zapletal <lzap+rpm@redhat.com> - 2.2.0-0.22.develop
- Added SELinux wrapper for sidekiq

* Thu May 21 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.0-0.21.develop
- Update Gem and NPM dependencies

* Wed May 13 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.20.develop
- Bump version to 2.2-develop

* Wed May 06 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.0-0.20.develop
- Require glibc-langpack-en in foreman-postgresql

* Sun May 3 2020 Tomer Brisker <tbrisker@gmail.com> - 2.1.0-0.19.develop
- Drop rackspace

* Fri May 1 2020 Justin Sherrill <jsherril@redhat.com> 2.1.0-0.18.develop
- stop dynflowd before service file is removed

* Fri May 1 2020 Tomer Brisker <tbrisker@gmail.com> - 2.1.0-0.17.develop
- Drop sqlite

* Thu Apr 30 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.0-0.16.develop
- Update Gem and NPM dependencies

* Fri Apr 24 2020 Evgeni Golov - 2.1.0-0.15.develop
- Regenerate GEM dependencies using new code

* Thu Apr 23 2020 Evgeni Golov - 2.1.0-0.14.develop
- Update Gem dependencies

* Thu Apr 23 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.13.develop
- Fix schema.rb.nulldb location

* Wed Apr 22 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.12.develop
- Use nulldb for rake tasks

* Wed Apr 22 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.11.develop
- Only use scl for dynflow if available

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-0.10.develop
- Bump to release for EL8

* Wed Apr 08 2020 Evgeni Golov - 2.1.0-0.9.develop
- Fix ignoring fonts and images for plugins once more

* Tue Apr 07 2020 ehelms - 2.1.0-0.8.develop
- Fix ignoring fonts and images for plugins

* Tue Apr 07 2020 Evgeni Golov - 2.1.0-0.7.develop
- Add images/ and fonts/ to exclude of plugin webpack builds

* Thu Mar 26 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.6.develop
- Stop dynflow service before removal

* Fri Mar 20 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.0-0.5.develop
- Use systemd socket activation (#29144)

* Tue Mar 10 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.0-0.4.develop
- Update Gem and NPM dependencies

* Thu Mar 05 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.0-0.3.develop
- Update Gem and NPM dependencies

* Thu Feb 20 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.2.develop
- Drop setting organization and location to enabled

* Thu Feb 13 2020 Tomer Brisker <tbrisker@gmail.com> - 2.1.0-0.1.develop
- Bump version to 2.1-develop

* Tue Feb 04 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-0.9.develop
- Update the rest of the tfm-runtime requirements

* Tue Feb 04 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-0.8.develop
- Update tfm-runtime requirement

* Wed Jan 22 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-0.7.develop
- Include .babelrc.js in foreman-assets

* Tue Jan 21 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-0.6.develop
- Update spec to remove the ror scl

* Tue Jan 21 2020 Ondrej Ezr <ezrik12@gmail.com> - 2.0.0-0.5.develop
- drop dynflowd service and leave only dynflow-sidekiq

* Thu Jan 16 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-0.4.develop
- Remove database action macros and restart

* Wed Jan 15 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.0.0-0.3.develop
- Update Gem and NPM dependencies

* Wed Jan 08 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.0.0-0.2.develop
- Update Gem dependencies

* Mon Jan 06 2020 Tomer Brisker <tbrisker@gmail.com> - 2.0.0-0.1.develop
- Bump version to 2.0-develop

* Sun Dec 08 2019 Michael Moll <mmoll@mmoll.at> - 1.25.0-0.6.develop
- Update NPM dependencies

* Mon Dec 02 2019 Evgeni Golov - 1.25.0-0.5.develop
- Update Gem and NPM dependencies

* Thu Nov 21 2019 Tomer Brisker <tbrisker@gmail.com> - 1.25.0-0.4.develop
- drop mysql package

* Mon Nov 18 2019 Evgeni Golov - 1.25.0-0.3.develop
- Unify prerelease macro handling

* Wed Oct 30 2019 Michael Moll <mmoll@mmoll.at> - 1.25.0-0.2.develop
- Update fog-libvirt gem dependency

* Wed Oct 30 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.25.0-0.1.develop
- Bump version to 1.25-develop

* Tue Oct 22 2019 Ondrej Ezr <ezrik12@gmail.com> - 1.24.0-0.11.develop
- Add dynflow-sidekiq package providing services for running dynflow on sidekiq

* Fri Oct 11 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.24.0-0.10.develop
- Updates to support NodeJS packages built into SCL

* Thu Oct 10 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.24.0-0.9.develop
- Update MALLOC_ARENA_MAX in dynflowd sysconfig

* Thu Oct 10 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.24.0-0.8.develop
- Update JWT dependencies (#25809)

* Mon Oct 07 2019 Tomer Brisker <tbrisker@gmail.com> 1.24.0-0.7.develop
- remove foreman-config

* Sun Oct 06 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.24.0-0.6.develop
- Update Gem and NPM dependencies

* Thu Oct 03 2019 Michael Moll <mmoll@mmoll.at> - 1.24.0-0.5.develop
- Update responders gem dependency

* Tue Oct 01 2019 Michael Moll <mmoll@mmoll.at> - 1.24.0-0.4.develop
- Update deep_cloneable gem dependency

* Wed Aug 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.24.0-0.3.develop
- Update Gem and NPM dependencies

* Thu Aug 22 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.24.0-0.2.develop
- Update Gem and NPM dependencies

* Tue Jul 30 2019 Evgeni Golov - 1.24.0-0.1.develop
- Bump version to 1.24-develop

* Wed Jul 17 2019 Evgeni Golov - 1.23.0-0.15.develop
- Remove foreman-vendor artifacts from plugin builds

* Tue Jul 16 2019 Evgeni Golov - 1.23.0-0.14.develop
- use @theforeman/vendor

* Thu Jul 11 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.13.develop
- Update Gem and NPM dependencies

* Wed Jul 03 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.12.develop
- Define foreman_restart macro

* Mon Jun 10 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.11.develop
- Update Gem and NPM dependencies
- Add a redis subpackage

* Thu May 23 2019 Shira Maximov <shiramaximov@gmail.com> 1.23.0-0.10.develop
- Update for-ovirt deps

* Fri May 17 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.9.develop
- Update Gem and NPM dependencies

* Thu May 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.8.develop
- Update Gem and NPM dependencies

* Tue May 14 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.7.develop
- Remove webpack provides/requires

* Mon May 13 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.6.develop
- Update Gem and NPM dependencies

* Wed May 08 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.5.develop
- Update Gem and NPM dependencies

* Tue May 7 2019 Timo Goebel <mail@timogoebel.name> - 1.23.0-0.4.develop
- Obsolete foreman_userdata

* Fri May 03 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.3.develop
- Update Gem and NPM dependencies

* Tue Apr 30 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.2.develop
- Update Gem and NPM dependencies

* Tue Apr 23 2019 Evgeni Golov <evgeni@golov.de> - 1.23.0-0.1.develop
- Bump version to 1.23-develop

* Mon Apr 15 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.22.0-0.11.develop
- Replace foreman-ruby with tfm-ruby

* Mon Apr 1 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.22.0-0.10.develop
- Add foreman-puma service

* Fri Mar 29 2019 Tomer Brisker <tbrisker@redhat.com> - 1.22.0-0.9.develop
- Obsolete foreman-compute

* Thu Mar 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.8.develop
- Drop foreman-compute requirement

* Wed Mar 27 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.7.develop
- Update Gem and NPM dependencies

* Thu Feb 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.6.develop
- Update Gem and NPM dependencies

* Tue Feb 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.5.develop
- #26084 Restart the passenger service

* Mon Feb 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.4.develop
- Update roadie-rails dependency

* Mon Feb 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.3.develop
- Update Gem and NPM dependencies

* Wed Jan 23 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.2.develop
- Update Gem and NPM dependencies

* Wed Jan 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.1.develop
- Bump to 1.22

* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.21.0-0.7.develop
- Update Gem and NPM dependencies

* Wed Dec 05 2018 Evgeni Golov - 1.21.0-0.6.develop
- Make the Requires script more robust if the manifest.json cannot be found

* Thu Nov 29 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.21.0-0.5.develop
- Update Gem and NPM dependencies

* Mon Nov 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.21.0-0.4.develop
- Update Gem and NPM dependencies

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.21.0-0.3.develop
- Remove *.js.map file after asset precompile

* Wed Oct 24 2018 Adam Price <komidore64@gmail.com> - 1.21.0-0.2.develop
- add nightly macro

* Wed Oct 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.21.0-0.1.develop
- Bump version to 1.21 and reset release

* Wed Oct 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.14.develop
- Remove incorrect systemd service alias

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
