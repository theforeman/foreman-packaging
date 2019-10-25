Name:     postgresql-debversion
Version:  v1.1.1
Release:  1%{?dist}
Summary:  Debian version number type for PostgreSQL

Group:    Applications/System
License:  GPLv3
URL:      https://salsa.debian.org/postgresql/postgresql-debversion
Source0:  https://salsa.debian.org/postgresql/postgresql-debversion/-/archive/%{version}/postgresql-debversion-%{version}.tar.gz
Patch0:   0001-Copy-relevant-code-from-apt-pkg-to-ease-packaging.patch

BuildRequires: g++
BuildRequires: postgresql-devel
BuildRequires: postgresql-server-devel

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
%autosetup -p1

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

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
* Fri Jan 03 2020 Matthias Dellweg <dellweg@atix.de> - v1.1.1-1
- new package
