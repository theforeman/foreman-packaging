%global scl ruby193
%scl_package %scl

%global install_scl 1

Summary: Package that installs %scl
Name: %scl_name
Version: 1
Release: 9%{?dist}
License: GPLv2+
%if 0%{?install_scl}
Requires: %{scl_prefix}rubygem-therubyracer
Requires: %{scl_prefix}rubygem-sqlite3
Requires: %{scl_prefix}rubygem-rails
%endif
BuildRequires: scl-utils-build
BuildRequires: iso-codes

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%prep
# workaround for notdefined buildsubdir macro
%setup -c %{name}-%{version}-%{release} -T

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_scl_scripts}/root
cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH=%{_bindir}:\$PATH
export LD_LIBRARY_PATH=%{_libdir}:\$LD_LIBRARY_PATH
export MANPATH=%{_mandir}:\$MANPATH
EOF
%scl_install

%files

%files runtime
%scl_files

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1-9
- enable scl_install (msuchy@redhat.com)

* Tue Feb 19 2013 Miroslav Suchý <msuchy@redhat.com> 1-8
- add iso-codes as buildrequires (msuchy@redhat.com)
- workaround for not defined buildsubdir macro (msuchy@redhat.com)

* Tue Feb 19 2013 Miroslav Suchý <msuchy@redhat.com> 1-7
- new package built with tito

* Wed Nov 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-6
- Rebuilt for PPC.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-5
- Switched JS runtime engine to TheRubyRacer.

* Tue May 29 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-4
- Properly override MANPATH.

* Thu Apr 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-3
- Allow installing the whole scl with the ruby193 package.

* Tue Apr 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-2
- Bump release to get the build on all architectures.

* Fri Mar 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1-1
- Initial package.
