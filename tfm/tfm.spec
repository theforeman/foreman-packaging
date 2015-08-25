%{!?scl_name_base: %global scl_name_base tfm}
%global scl_vendor theforeman
%global _scl_prefix /opt/%{scl_vendor}
%{!?scl:%global scl %{scl_name_base}%{?scl_name_version}}
%{!?scl_vendor_in_name: %global scl_vendor_in_name 0}
%{?scl_package:%scl_package %scl}

# Fallback to ruby193 and v8314 when scldevel's not in the buildroot
%{!?scl_ruby:%global scl_ruby ruby193}
%{!?scl_prefix_ruby:%global scl_prefix_ruby %{scl_ruby}-}
%{!?scl_v8:%global scl_v8 v8314}
%{!?scl_prefix_v8:%global scl_prefix_v8 %{scl_v8}-}

# Do not produce empty debuginfo package.
%global debug_package %{nil}

%global install_scl 1

Summary: Package that installs %scl
Name: %scl_name
Version: 1.1
Release: 1%{?dist}
License: GPLv2+
Group: Applications/File
Source0: README
Source1: LICENSE
Source2: tfm.attr
# This should be removed as soon as scl-utils automatically generate
# dependencies on scl -runtime (rhbz#1054711).
Requires: %{scl_runtime}
%if 0%{?install_scl}
Requires: %{scl_ruby}
Requires: %{scl_v8}
%endif
BuildRequires: scl-utils-build help2man
BuildRequires: %{scl_prefix_ruby}scldevel
BuildRequires: %{scl_prefix_ruby}rubygems-devel
BuildRequires: %{scl_prefix_v8}scldevel

%description
This is the main package for %scl Software Collection.

Provides dependencies for Foreman (http://theforeman.org/).

%package runtime
Summary: Package that handles %scl Software Collection.
Group: Applications/File
Requires: scl-utils
Requires: %{scl_prefix_ruby}runtime
Requires: %{scl_prefix_v8}runtime
Requires: %{_root_bindir}/scl_source
Requires(post): policycoreutils-python
Obsoletes: ruby193-ruby-wrapper

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

Provides dependencies for Foreman (http://theforeman.org/).

%package build
Summary: Package shipping basic build configuration
Group: Applications/File
Requires: scl-utils-build
Requires: %{scl_runtime}
Requires: %{scl_prefix_ruby}scldevel
Requires: %{scl_prefix_v8}scldevel

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
. scl_source enable %{scl_ruby} %{scl_v8}

export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LIBRARY_PATH=%{_libdir}dd\${LIBRARY_PATH:+:\${LIBRARY_PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
export CPATH=%{_includedir}\${CPATH:+:\${CPATH}}
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}
export GEM_PATH=%{gem_dir}:\${GEM_PATH:+\${GEM_PATH}}\${GEM_PATH:-\`scl enable %{scl_ruby} -- ruby -e "print Gem.path.join(':')"\`}
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

scl enable %{scl_ruby} - << \EOF
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
%scl_files
%dir %{_mandir}/man*
%config(noreplace) %{?_scl_scripts}/service-environment
%{_mandir}/man7/%{scl_name}.*
%attr(755,-,-) %{_root_bindir}/%{scl_name}-rake
%attr(755,-,-) %{_root_bindir}/%{scl_name}-ruby
%{_root_bindir}/ruby193-ruby

%files build
%doc LICENSE
%{_root_sysconfdir}/rpm/macros.%{scl}-config
%{_rpmconfigdir}/fileattrs

%files scldevel
%doc LICENSE
%{_root_sysconfdir}/rpm/macros.%{scl_name}-scldevel

%changelog
* Tue Apr 28 2015 Dominic Cleal <dcleal@redhat.com> - 1.1-1
- Add tfm-ruby/rake wrappers to bindir

* Wed Feb 04 2015 Dominic Cleal <dcleal@redhat.com> - 1.0-2
- Provide changed vendor/dir prefix macros in tfm-build

* Wed Apr 02 2014 Dominic Cleal <dcleal@redhat.com> - 1.0-1
- Initial package.
