%{!?scl_name_base: %global scl_name_base tfm}
%global scl_vendor theforeman
%global _scl_prefix /opt/%{scl_vendor}
%{!?scl:%global scl %{scl_name_base}%{?scl_name_version}}
%{!?scl_vendor_in_name: %global scl_vendor_in_name 0}
%{?scl_package:%scl_package %scl}

# Fallback to sclo-ror42 etc. when scldevel's not in the buildroot
%{!?scl_ror:%global scl_ror sclo-ror42}
%{!?scl_prefix_ror:%global scl_prefix_ror %{scl_ror}-}
%{!?scl_ruby:%global scl_ruby rh-ruby22}
%{!?scl_prefix_ruby:%global scl_prefix_ruby %{scl_ruby}-}

# Do not produce empty debuginfo package.
%global debug_package %{nil}

%global install_scl 1

Summary: Package that installs %scl
Name: %scl_name
Version: 3.2
Release: 10%{?dist}
License: GPLv2+
Group: Applications/File
Source0: README
Source1: LICENSE
Source2: tfm.attr
# This should be removed as soon as scl-utils automatically generate
# dependencies on scl -runtime (rhbz#1054711).
Requires: %{scl_runtime}
Requires: %{scl_runtime}-assets
%if 0%{?install_scl}
Requires: %{scl_ror}
Requires: %{scl_ruby}
%endif
BuildRequires: scl-utils-build help2man
BuildRequires: %{scl_prefix_ror}scldevel
BuildRequires: %{scl_prefix_ror}runtime
BuildRequires: %{scl_prefix_ruby}scldevel
BuildRequires: %{scl_prefix_ruby}rubygems-devel

%description
This is the main package for %scl Software Collection.

Provides dependencies for Foreman (http://theforeman.org/).

%package runtime
Summary: Package that handles %scl Software Collection.
Group: Applications/File
Requires: scl-utils
Requires: %{scl_prefix_ror}runtime
Requires: %{scl_prefix_ruby}runtime
Requires: %{_root_bindir}/scl_source
Requires(post): policycoreutils-python
Obsoletes: ruby193-ruby-wrapper

# Obsolete packages no longer carried within this SCL to both clean up
# and to ensure smooth upgrades when old packages deps aren't satisified
Obsoletes: %{scl_prefix}npm(flux) < 2.1.1-2
Obsoletes: %{scl_prefix}rubygem-ace-rails-ap < 4.1.1-2
Obsoletes: %{scl_prefix}rubygem-ansi < 1.4.3-7
Obsoletes: %{scl_prefix}rubygem-archive-tar-minitar < 0.5.2-12
Obsoletes: %{scl_prefix}rubygem-audited-activerecord < 4.2.0-3
Obsoletes: %{scl_prefix}rubygem-colorize < 0.7.7-5
Obsoletes: %{scl_prefix}rubygem-concurrent-ruby < 1.0.1-2
Obsoletes: %{scl_prefix}rubygem-dalli < 2.6.4-4
Obsoletes: %{scl_prefix}rubygem-ejs < 1.1.1-4
Obsoletes: %{scl_prefix}rubygem-flot-rails < 0.0.3-8
Obsoletes: %{scl_prefix}rubygem-foreigner < 1.7.1-4
Obsoletes: %{scl_prefix}rubygem-foremancli < 1.0-10
Obsoletes: %{scl_prefix}rubygem-hirb-unicode < 0.0.5-9
Obsoletes: %{scl_prefix}rubygem-i18n < 0.7.0-3
Obsoletes: %{scl_prefix}rubygem-ipaddrjs-rails < 1.1.1-2
Obsoletes: %{scl_prefix}rubygem-jquery-rails < 3.1.0-4
Obsoletes: %{scl_prefix}rubygem-less < 2.5.1-5
Obsoletes: %{scl_prefix}rubygem-less-rails < 2.5.0-4
Obsoletes: %{scl_prefix}rubygem-macaddr < 1.7.1-2
Obsoletes: %{scl_prefix}rubygem-multi_json < 1.10.1-4
Obsoletes: %{scl_prefix}rubygem-multi-select-rails < 0.9.12-6
Obsoletes: %{scl_prefix}rubygem-nokogiri < 1.6.6.2-3
Obsoletes: %{scl_prefix}rubygem-protected_attributes < 1.1.3-4
Obsoletes: %{scl_prefix}rubygem-rails-observers < 0.1.2-8
Obsoletes: %{scl_prefix}rubygem-sass < 3.4.19-4
Obsoletes: %{scl_prefix}rubygem-sass-rails < 5.0.4-3
Obsoletes: %{scl_prefix}rubygem-select2-rails < 3.5.10-3
Obsoletes: %{scl_prefix}rubygem-sprockets < 3.5.2-2
Obsoletes: %{scl_prefix}rubygem-sprockets-rails < 2.3.3-2
Obsoletes: %{scl_prefix}rubygem-table_print < 1.5.1-7
Obsoletes: %{scl_prefix}rubygem-turbolinks < 2.5.3-4
Obsoletes: %{scl_prefix}rubygem-underscore-rails < 1.8.3-5
Obsoletes: %{scl_prefix}rubygem-uuid < 2.3.8-2
Obsoletes: %{scl_prefix}rubygem-uuidtools < 2.1.3-6

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

Provides dependencies for Foreman (http://theforeman.org/).

%package runtime-assets
Summary: Package that adds asset compilation for %scl Software Collection.
Group: Applications/File
Requires: %{scl_prefix}runtime

%description runtime-assets
Package shipping additional scripts to work with %scl Software Collection.

Provides additional asset compilation dependencies for Foreman
(http://theforeman.org/).

%package build
Summary: Package shipping basic build configuration
Group: Applications/File
Requires: scl-utils-build
Requires: %{scl_runtime}
Requires: %{scl_runtime}-assets
Requires: %{scl_prefix_ror}scldevel
Requires: %{scl_prefix_ruby}scldevel

%description build
Package shipping essential configuration macros to build %scl Software Collection.

Provides dependencies for Foreman (http://theforeman.org/).

%package scldevel
Summary: Package shipping development files for %scl
Group: Applications/File
Provides: scldevel(%{scl_name})

%description scldevel
Package shipping development files, especially usefull for development of
packages depending on %scl Software Collection.

Provides dependencies for Foreman (http://theforeman.org/).

%prep
%setup -T -c

# Expand macros used in README file.
cat > README << EOF
%{expand:%(cat %{SOURCE0})}
EOF

cp %{SOURCE1} .

%build
# Generate a helper script that will be used by help2man.
cat > h2m_helper << 'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} %{version} Software Collection" || cat README
EOF
chmod a+x h2m_helper

# Generate the man page from include.h2m and ./h2m_helper --help output.
help2man -N --section 7 ./h2m_helper -o %{scl_name}.7

%install
%scl_install

cat >> %{buildroot}%{_scl_scripts}/enable << EOF
. scl_source enable %{scl_ror}
if [ -e %{_scl_scripts}/enable_assets ]; then
  . %{_scl_scripts}/enable_assets
fi

export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LIBRARY_PATH=%{_libdir}dd\${LIBRARY_PATH:+:\${LIBRARY_PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
export CPATH=%{_includedir}\${CPATH:+:\${CPATH}}
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}
export GEM_PATH=%{gem_dir}:\${GEM_PATH:+\${GEM_PATH}}\${GEM_PATH:-\`scl enable %{scl_ror} -- ruby -e "print Gem.path.join(':')"\`}
EOF

# enable asset compilation collections optionally, only if -runtime-assets is
# installed, to reduce deps for -runtime
cat >> %{buildroot}%{_scl_scripts}/enable_assets << EOF
# noop
EOF

# additional rpm macros for builds in the collection to set the vendor correctly
cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name}-config << EOF
%%scl_vendor %{scl_vendor}
%%_scl_prefix %{_scl_prefix}
EOF

# generate rpm macros file for dependent collections
cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name}-scldevel << EOF
%%scl_%{scl_name} %{scl}
%%scl_prefix_%{scl_name} %{scl_prefix}
EOF

# generate a configuration file for daemon
cat >> %{buildroot}%{?_scl_scripts}/service-environment << EOF
# Services are started in a fresh environment without any influence of user's
# environment (like environment variable values). As a consequence,
# information of all enabled collections will be lost during service start up.
# If user needs to run a service under any software collection enabled, this
# collection has to be written into SCLNAME_SCLS_ENABLED variable in
# /opt/rh/sclname/service-environment.
$(printf '%%s' '%{scl}' | tr '[:lower:][:space:]' '[:upper:]_')_SCLS_ENABLED='%{scl}'
EOF

# Install generated man page.
mkdir -p %{buildroot}%{_mandir}/man7/
install -m 644 %{?scl_name}.7 %{buildroot}%{_mandir}/man7/%{?scl_name}.7

mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs/
cp %{SOURCE2} %{buildroot}%{_rpmconfigdir}/fileattrs/

# Install wrappers into system root to activate the SCL
%{__mkdir_p} %{buildroot}%{_root_bindir}
cat >> %{buildroot}%{_root_bindir}/%{scl_name}-ruby << EOF
#!/bin/bash
# Execute a single script with no arguments with 'scl', else it fails to
# pass spaces/quotes in arguments through correctly (RHBZ#1248418).
TMP=\$(mktemp)
trap "rm -f \$TMP" EXIT
echo -n ruby > \$TMP
for arg in "\$@"; do
  printf " %q" "\$arg" >> \$TMP
done
scl enable %{scl_name} "bash \$TMP"
EOF
# compatibility symlink
ln -s %{scl_name}-ruby %{buildroot}%{_root_bindir}/ruby193-ruby

cat >> %{buildroot}%{_root_bindir}/%{scl_name}-rake << EOF
#!/bin/bash
# Execute a single script with no arguments with 'scl', else it fails to
# pass spaces/quotes in arguments through correctly (RHBZ#1248418).
TMP=\$(mktemp)
trap "rm -f \$TMP" EXIT
echo -n rake > \$TMP
for arg in "\$@"; do
  printf " %q" "\$arg" >> \$TMP
done
scl enable %{scl_name} "bash \$TMP"
EOF

scl enable %{scl_ror} - << \EOF
# Fake tfm SCL environment.
GEM_PATH=%{gem_dir}:${GEM_PATH:+${GEM_PATH}}${GEM_PATH:-`ruby -e "print Gem.path.join(':')"`} \
X_SCLS=%{scl} \
ruby -rfileutils > rubygems_filesystem.list << \EOR
  # Create RubyGems filesystem.
  Gem.ensure_gem_subdirectories '%{buildroot}%{gem_dir}'
  FileUtils.mkdir_p File.join '%{buildroot}', Gem.default_ext_dir_for('%{gem_dir}')

  # Output the relevant directories.
  Gem.default_dirs[:%{scl}_system].each { |k, p| puts p }
EOR
EOF

%post runtime
# Simple copy of context from system root to DSC root.
# In case new version needs some additional rules or context definition,
# it needs to be solved.
# Unfortunately, semanage does not have -e option in RHEL-5, so we would
# have to have its own policy for collection (inspire in mysql%{scl_name_version} package)
semanage fcontext -a -e / %{?_scl_root} >/dev/null 2>&1 || :
restorecon -R %{?_scl_root} >/dev/null 2>&1 || :
selinuxenabled && load_policy || :

%files

%files runtime -f rubygems_filesystem.list
%doc README LICENSE
%exclude %{_scl_scripts}/enable_assets
%scl_files
%dir %{_mandir}/man*
%config(noreplace) %{?_scl_scripts}/service-environment
%{_mandir}/man7/%{scl_name}.*
%attr(755,-,-) %{_root_bindir}/%{scl_name}-rake
%attr(755,-,-) %{_root_bindir}/%{scl_name}-ruby
%{_root_bindir}/ruby193-ruby

%files runtime-assets
%{_scl_scripts}/enable_assets

%files build
%doc LICENSE
%{_root_sysconfdir}/rpm/macros.%{scl}-config
%{_rpmconfigdir}/fileattrs

%files scldevel
%doc LICENSE
%{_root_sysconfdir}/rpm/macros.%{scl_name}-scldevel

%changelog
* Fri Mar 31 2017 Dominic Cleal <dominic@cleal.org> 3.2-10
- Remove rails-observers gem (dominic@cleal.org)

* Fri Mar 24 2017 Dominic Cleal <dominic@cleal.org> 3.2-9
- Remove ace-rails-ap gem (dominic@cleal.org)

* Mon Mar 20 2017 Dominic Cleal <dominic@cleal.org> 3.2-8
- Remove colorize gem (dominic@cleal.org)

* Thu Feb 09 2017 Dominic Cleal <dominic@cleal.org> 3.2-7
- Remove table_print (dominic@cleal.org)

* Tue Jan 24 2017 Dominic Cleal <dominic@cleal.org> 3.2-6
- Remove audited-activerecord gem (dominic@cleal.org)

* Tue Nov 15 2016 Dominic Cleal <dominic@cleal.org> 3.2-5
- Remove rubygem-macaddr, uuid (dominic@cleal.org)

* Fri Sep 23 2016 Dominic Cleal <dominic@cleal.org> 3.2-4
- Remove rubygem-multi-select-rails (me@daniellobato.me)

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> 3.2-3
- Remove ipaddrjs-rails (dominic@cleal.org)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 3.2-2
- Remove select2-rails (elobatocs@gmail.com)

* Thu Aug 18 2016 Dominic Cleal <dominic@cleal.org> 3.2-1
- Remove unused v8314 dependency (dominic@cleal.org)

* Mon Aug 15 2016 Dominic Cleal <dominic@cleal.org> 3.1-5
- Remove unused flot-rails gem (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 3.1-4
- Remove dependencies replaced with webpack (elobatocs@gmail.com)

* Mon Jun 20 2016 Dominic Cleal <dominic@cleal.org> 3.1-3
- Remove foremancli, unmaintained (dominic@cleal.org)

* Thu May 12 2016 Dominic Cleal <dominic@cleal.org> 3.1-3
- Prevent enable_assets being shipped in tfm-runtime (dominic@cleal.org)

* Mon May 09 2016 Dominic Cleal <dominic@cleal.org> 3.1-2
- Replace hirb-unicode with hirb-unicode-steakknife (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 3.1-1
- Add tfm-runtime-assets subpackage (dominic@cleal.org)

* Fri Apr 29 2016 Dominic Cleal <dominic@cleal.org> 3.0-2
- Remove unused tfm-rubygem-ansi (dominic@cleal.org)

* Wed Apr 20 2016 Dominic Cleal <dominic@cleal.org> 3.0-1
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)
- Remove foreigner and packages now in sclo-ror42 (dominic@cleal.org)

* Fri Apr 15 2016 Dominic Cleal <dominic@cleal.org> 2.0-4
- Remove archive-tar-minitar package (elobatocs@gmail.com)

* Mon Apr 11 2016 Dominic Cleal <dominic@cleal.org> 2.0-3
- Add uuidtools to obsoleted packages (dominic@cleal.org)
- Fix less, less-rails package names (dominic@cleal.org)

* Fri Jan 15 2016 Dominic Cleal <dcleal@redhat.com> 2.0-2
- Remove rubygem-less and rubygem-less-rails (ericdhelms@gmail.com)

* Mon Dec 21 2015 Dominic Cleal <dcleal@redhat.com> 2.0-1
- Change to use rh-ror41, rh-ruby22 collections (dcleal@redhat.com)
- Replace tfm-rubygem-sass with ror41-rubygem-sass (dcleal@redhat.com)
- Replace tfm-rubygem-sprockets with ror41-rubygem-sprockets
  (dcleal@redhat.com)

* Tue Apr 28 2015 Dominic Cleal <dcleal@redhat.com> - 1.1-1
- Add tfm-ruby/rake wrappers to bindir

* Wed Feb 04 2015 Dominic Cleal <dcleal@redhat.com> - 1.0-2
- Provide changed vendor/dir prefix macros in tfm-build

* Wed Apr 02 2014 Dominic Cleal <dcleal@redhat.com> - 1.0-1
- Initial package.
