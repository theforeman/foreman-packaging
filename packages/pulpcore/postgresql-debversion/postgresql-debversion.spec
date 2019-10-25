%if 0%{?rhel} <= 7
%global scl rh-postgresql12
%endif

%{?scl:%scl_package postgresql-debversion}
%{!?scl:%global pkg_name %{name}}

Name:     %{?scl_prefix}postgresql-debversion
Version:  1.1.1
Release:  1%{?dist}
Summary:  Debian version number type for PostgreSQL

Group:    Applications/System
License:  GPLv3
URL:      https://salsa.debian.org/postgresql/postgresql-debversion
Source0:  https://salsa.debian.org/postgresql/postgresql-debversion/-/archive/v%{version}/postgresql-debversion-v%{version}.tar.gz
Patch0:   0001-Copy-relevant-code-from-apt-pkg-to-ease-packaging.patch


Requires: %{?scl_prefix}postgresql-server
%{?scl:Requires: %{?scl_prefix}runtime}

%{?scl:BuildRequires: %{?scl_prefix}runtime}
BuildRequires: %{?scl_prefix}postgresql-devel
BuildRequires: gcc-c++

%if 0%{?rhel} > 7
BuildRequires: redhat-rpm-config
BuildRequires: postgresql-server-devel
%endif

ExclusiveArch: x86_64

%description
Debian version numbers, used to version Debian binary and source
packages, have a defined format, including specifications for how
versions should be compared in order to sort them.  This package
implements a `debversion` type to represent Debian version numbers
within the PostgreSQL database.  This also includes operators for
version comparison and index operator classes for creating indexes on
the debversion type.

Version comparison uses the algorithm used by the Debian package
manager, dpkg, using the implementation from libapt-pkg.  This means
that columns in tables using the debversion type may be sorted and
compared correctly using the same logic as `dpkg --compare-versions`.
It is also possible to create indexes on these columns.

postgresql-debversion implements the following features:

* The `debversion` type (internally derived from the `text` type)
* A full set of operators for version comparison (< <= = <> >= >)
  including commutator and negator optimisation hints
* Operator classes for btree and hash indexes
* The aggregate functions `min()` and `max()`

%prep
%autosetup -p1 -n postgresql-debversion-v%{version}

%build
%{?scl:scl enable %{scl} - <<EOF}
make %{?_smp_mflags}
%{?scl:EOF}

%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} - <<EOF}
%make_install
%{?scl:EOF}

%files
%{_libdir}/pgsql/debversion.so
%{_datadir}/pgsql/extension/debversion--1.0.5--1.0.6.sql
%{_datadir}/pgsql/extension/debversion--1.0.6--1.0.7.sql
%{_datadir}/pgsql/extension/debversion--1.0.7--1.0.8.sql
%{_datadir}/pgsql/extension/debversion--1.0.8--1.1.sql
%{_datadir}/pgsql/extension/debversion--1.1.sql
%{_datadir}/pgsql/extension/debversion--unpackaged--1.0.5.sql
%{_datadir}/pgsql/extension/debversion.control
%doc README.md
%license COPYING

%changelog
* Fri Jan 03 2020 Matthias Dellweg <dellweg@atix.de> - 1.1.1-1
- new package
