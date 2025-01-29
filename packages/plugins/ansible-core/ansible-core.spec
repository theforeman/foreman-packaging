%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Disable shebang munging for specific paths.  These files are data files.
# ansible-test munges the shebangs itself.
%global __brp_mangle_shebangs_exclude_from_file %{SOURCE2}


# NOTE(pabelanger): Don't auto add pwsh as Requires for ansible-test. We do
# not wish to package it.
%global __requires_exclude ^/usr/bin/pwsh$

%global upstream_version ${CI_ANSIBLE_UPSTREAM_VERSION_SANITIZED}

# RHEL and Fedora add -s to the shebang line.  We do *not* use -s -E -S or -I
# with ansible because it has many optional features which users need to
# install libraries on their own to use.  For instance, paramiko for the
# network connection plugins or winrm to talk to windows hosts.
# Set this to nil to remove -s
%define py_shbang_opts %{nil}
%define py2_shbang_opts %{nil}
%define py3_shbang_opts %{nil}

%define vendor_path %{buildroot}%{python3_sitelib}/ansible/_vendor/
%define vendor_pip %{__python3} -m pip install --no-deps -v --no-use-pep517 --no-binary :all: -t %{vendor_path}

Name: ansible-core
Summary: SSH-based configuration management, deployment, and task execution system
Version: 2.16.14
%global uversion %{version_no_tilde %{quote:%nil}}
Release: 3%{?dist}
Epoch:   1

Group: Development/Libraries
License: GPL-3.0-or-later
Source0: https://github.com/ansible/ansible/archive/v%{uversion}/%{name}-%{uversion}.tar.gz
Source1: https://github.com/ansible/ansible-documentation/archive/v%{uversion}/ansible-documentation-%{uversion}.tar.gz
BuildArch: noarch

URL: http://ansible.com

# We obsolete old ansible, and any version of ansible-base.
Obsoletes: ansible < 2.10.0
Obsoletes: ansible-base < 2.10.0

# Bundled provides that are sprinkled throughout the codebase.
Provides: bundled(python-backports-ssl_match_hostname) = 3.7.0.1
Provides: bundled(python-distro) = 1.6.0
Provides: bundled(python-selectors2) = 1.1.1
Provides: bundled(python-six) = 1.16.0

BuildRequires: pyproject-rpm-macros
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pip
BuildRequires: python%{python3_pkgversion}-wheel
BuildRequires: python%{python3_pkgversion}-docutils
BuildRequires: python%{python3_pkgversion}-jinja2 >= 3.0.0
BuildRequires: python%{python3_pkgversion}-pyyaml
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}-setuptools

Requires: git-core
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-jinja2 >= 3.0.0
Requires: python%{python3_pkgversion}-PyYAML >= 5.1
Requires: python%{python3_pkgversion}-cryptography
Requires: python%{python3_pkgversion}-packaging
Requires: python%{python3_pkgversion}-resolvelib >= 0.5.3
Requires: python%{python3_pkgversion}-resolvelib < 1.1.0
Requires: sshpass

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%package -n ansible-test
Summary: Tool for testing ansible plugin and module code
Requires: %{name} = %{epoch}:%{version}-%{release}

%description -n ansible-test
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package installs the ansible-test command for testing modules and plugins
developed for ansible.

%prep
%autosetup -n ansible-%{version} -a1

sed -i -s 's|/usr/bin/env python|%{python3}|' \
    bin/ansible-test \
    test/lib/ansible_test/_util/target/cli/ansible_test_cli_stub.py

%build
%pyproject_wheel

%install
%pyproject_install

# Create system directories that Ansible defines as default locations in
# ansible/config/base.yml
DATADIR_LOCATIONS='%{_datadir}/ansible/collections
%{_datadir}/ansible/plugins/doc_fragments
%{_datadir}/ansible/plugins/action
%{_datadir}/ansible/plugins/become
%{_datadir}/ansible/plugins/cache
%{_datadir}/ansible/plugins/callback
%{_datadir}/ansible/plugins/cliconf
%{_datadir}/ansible/plugins/connection
%{_datadir}/ansible/plugins/filter
%{_datadir}/ansible/plugins/httpapi
%{_datadir}/ansible/plugins/inventory
%{_datadir}/ansible/plugins/lookup
%{_datadir}/ansible/plugins/modules
%{_datadir}/ansible/plugins/module_utils
%{_datadir}/ansible/plugins/netconf
%{_datadir}/ansible/roles
%{_datadir}/ansible/plugins/strategy
%{_datadir}/ansible/plugins/terminal
%{_datadir}/ansible/plugins/test
%{_datadir}/ansible/plugins/vars'

UPSTREAM_DATADIR_LOCATIONS=$(grep -ri default lib/ansible/config/base.yml | tr ':' '\n' | grep '/usr/share/ansible')

if [ "$SYSTEM_LOCATIONS" != "$UPSTREAM_SYSTEM_LOCATIONS" ] ; then
	echo "The upstream Ansible datadir locations have changed.  Spec file needs to be updated"
	exit 1
fi

mkdir -p %{buildroot}%{_datadir}/ansible/plugins/
for location in $DATADIR_LOCATIONS ; do
	mkdir %{buildroot}"$location"
done
mkdir -p %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}%{_sysconfdir}/ansible/roles/

cp ansible-documentation-%{version}/examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp ansible-documentation-%{version}/examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
# Build man pages

mkdir -p docs/man/man1
%{__python3} packaging/cli-doc/build.py man --output-dir docs/man/man1
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/

cp -pr ansible-documentation-%{version}/docs/docsite/rst .
cp -p lib/ansible_core.egg-info/PKG-INFO .

%files
%defattr(-,root,root)
%{_bindir}/ansible*
%exclude %{_bindir}/ansible-test
%config(noreplace) %{_sysconfdir}/ansible/
%license COPYING
%doc README.md PKG-INFO
%doc changelogs/CHANGELOG*.rst
%{_mandir}/man1/ansible*
%{_datadir}/ansible/
%{python3_sitelib}/ansible*
%exclude %{python3_sitelib}/ansible_test

%files -n ansible-test
%{_bindir}/ansible-test
%{python3_sitelib}/ansible_test

%changelog
* Mon Feb 03 2025 Odilon Sousa <osousa@redhat.com> - 1:2.16.14-3
- Rebuild against python 3.12

* Mon Jan 06 2025 Satoe Imaishi <simaishi@redhat.com> - 1:2.16.14-2
- Remove Provides for ansible

* Tue Dec 03 2024 Dimitri Savineau <dsavinea@redhat.com> - 1:2.16.14-1
- ansible-core 2.16.14 release
- Fix license and manpages macros usage
- Fix CVE-2024-11079 (Unsafe Tagging Bypass via hostvars Object in
  Ansible-Core)

* Wed Nov 06 2024 Dimitri Savineau <dsavinea@redhat.com> - 1:2.16.13-1
- ansible-core 2.16.13 release
- Fix CVE-2024-8775 (Exposure of Sensitive Information in Ansible
  Vault Files Due to Improper Logging)
- Fix CVE-2024-9902 (Ansible-core user may read/write unauthorized
  content)

* Thu Sep 19 2024 Dimitri Savineau <dsavinea@redhat.com> - 1:2.16.11-1
- ansible-core 2.16.11 release
- Rebuild for python 3.11

* Thu Jun 06 2024 Dimitri Savineau <dsavinea@redhat.com> - 1:2.15.12-1
- ansible-core 2.15.12 release

* Wed May 01 2024 Dimitri Savineau <dsavinea@redhat.com> - 1:2.15.11-1
- ansible-core 2.15.11 release

* Tue Mar 26 2024 Dimitri Savineau <dsavinea@redhat.com> - 1:2.15.10-1
- ansible-core 2.15.10 release

* Thu Feb 01 2024 Satoe Imaishi <simaishi@redhat.com> - 1:2.15.9-1
- ansible-core 2.15.9 release
- Fix CVE-2024-0690 (possible information leak in tasks that ignore
  ANSIBLE_NO_LOG configuration)

* Mon Dec 11 2023 Satoe Imaishi <simaishi@redhat.com> - 1:2.15.8-1
- ansible-core 2.15.8 release
- Fix CVE-2023-5764 (Template Injection)

* Tue Nov 07 2023 Dimitri Savineau <dsavinea@redhat.com> - 1:2.15.6-2
- ansible-core 2.15.6 release
- Add Epoch configuration

* Tue Oct 10 2023 Satoe Imaishi <simaishi@redhat.com> - 2.15.5-1
- ansible-core 2.15.5 release
- Fix CVE-2023-5115 (malicious role archive can cause ansible-galaxy to
  overwrite arbitrary files)

* Tue Sep 12 2023 Dimitri Savineau <dsavinea@redhat.com> - 2.15.4-1
- ansible-core 2.15.4 release

* Mon Aug 21 2023 Dimitri Savineau <dsavinea@redhat.com> - 2.15.3-1
- ansible-core 2.15.3 release
- Use docs and examples from ansible-documentation project.
- Build the manpages.

* Mon May 15 2023 Dimitri Savineau <dsavinea@redhat.com> - 2.15.0-1
- ansible-core 2.15.0 release

* Mon Nov 07 2022 Dimitri Savineau <dsavinea@redhat.com> - 2.14.0-1
- ansible-core 2.14.0 release

* Wed May 25 2022 Dimitri Savineau <dsavinea@redhat.com> - 2.13.0-2
- revert provides configuration.

* Mon May 16 2022 David Schmidt <dschmidt@redhat.com> - 2.13.0-1
- Bump ansible-core release to v2.13.0 and updated changelog.

* Tue Dec 07 2021 James Marshall <jamarsha@redhat.com> - 2.12.1-1
- Bump release to v2.12.1 and updated changelog.

* Fri Nov 12 2021 Dimitri Savineau <dsavinea@redhat.com> - 2.12.0-2
- Bump release for changelog files and test data file.

* Mon Nov 08 2021 Dimitri Savineau <dsavinea@redhat.com> - 2.12.0-1
- ansible-core 2.12.0-1

* Wed Jul 21 2021 Paul Belanger <pabelanger@redhat.com> - 2.11.3-2
- Add git dependency for ansible-galaxy CLI command.

* Tue Jul 20 2021 Yanis Guenane <yguenane@redhat.com> - 2.11.3-1
- ansible-core 2.11.3-1

* Fri Jul 02 2021 Satoe Imaishi <simaishi@redhat.com> - 2.11.2-2
- Add man pages

* Tue Jun 29 2021 Paul Belanger <pabelanger@redhat.com> - 2.11.2-1
- ansible-core 2.11.2 released.
- Drop bundled version of resolvelib in favor of
  python38-resolvelib.

* Wed Mar 31 2021 Rick Elrod <relrod@redhat.com> - 2.11.0b4-1
- ansible-core 2.11.0 beta 4

* Thu Mar 18 2021 Rick Elrod <relrod@redhat.com> - 2.11.0b2-3
- Try adding a Provides for old ansible.

* Thu Mar 18 2021 Rick Elrod <relrod@redhat.com> - 2.11.0b2-2
- Try Obsoletes instead of Conflicts.

* Thu Mar 18 2021 Rick Elrod <relrod@redhat.com> - 2.11.0b2-1
- ansible-core 2.11.0 beta 2
- Conflict with old ansible and ansible-base.

* Thu Mar 11 2021 Rick Elrod <relrod@redhat.com> - 2.11.0b1-1
- ansible-core 2.11.0 beta 1

* Mon Nov 30 2020 Rick Elrod <relrod@redhat.com> - 2.11.0-1
- ansible-core, beta

* Wed Jun 10 2020 Rick Elrod <relrod@redhat.com> - 2.10.0-1
- ansible-base, beta
