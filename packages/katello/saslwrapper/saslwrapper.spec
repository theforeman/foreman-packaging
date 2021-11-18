%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitearchdir"]')}

Name:           saslwrapper
Version:        0.22
Release:        6%{?dist}
Summary:        Ruby and Python wrappers for the cyrus sasl library.
Group:          System Environment/Libraries
License:        ASL 2.0
URL:            http://qpid.apache.org
Source0:	      %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: doxygen
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: python2
BuildRequires: python2-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: cyrus-sasl-lib
BuildRequires: cyrus-sasl
BuildRequires: swig

%description
A simple wrapper for cyrus-sasl that permits easy binding into
scripting languages.

%package devel
Summary: Header files for developing with saslwrapper.
Group: System Environment/Libraries
Requires: %name = %version-%release

%description devel
The header files for developing with saslwrapper.

%package -n python2-saslwrapper
Summary: Python bindings for saslwrapper.
Group: System Environment/Libraries
Requires: %name = %version-%release
Requires: python2

%description -n python2-saslwrapper
Python bindings for the saslwrapper library.


%prep
%setup -q

%build
export LDFLAGS="-Wl,-z,relro"
./bootstrap
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name "*.la" | xargs rm

%clean
rm -rf %{buildroot}

%check
make check

%files
%defattr(-,root,root,-)
%doc LICENSE
%_libdir/libsaslwrapper.so.*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%_libdir/libsaslwrapper.so
%_includedir/saslwrapper.h

%files -n python2-saslwrapper
%defattr(-,root,root,-)
%python2_sitearch/saslwrapper.py*
%python2_sitearch/_saslwrapper.so


%changelog
* Wed Nov 21 2018 Irina Boverman <iboverma@redhat.com> - 0.22-6
- Initial build for RHEL 8
- Removed ruby-saslwrapper

* Wed Nov  6 2013 Irina Boverman <iboverma@redhat.com> - 0.22-5
- Added relro support

* Thu Jun 13 2013 Irina Boverman <iboverma@redhat.com> - 0.22-3
- Updated sources to 0.22-RC6

* Tue May  7 2013 Irina Boverman <iboverma@redhat.com> - 0.22-2
- Updated sources

* Tue Apr 30 2013 Irina Boverman <iboverma@redhat.com> - 0.22-1
- Rebase to 0.22

* Thu Oct  4 2012 Irina Boverman <iboverma@redhat.com> - 0.18-1
- Resolved: rhbz861962, Rebased to 0.18

* Mon Apr  2 2012 Nuno Santos <nsantos@redhat.com> - 0.14-1
- Rebased to official upstream 0.14 release
- Resolves: rhbz#808783

* Mon Aug  8 2011 Justin Ross <jross@redhat.com> - 0.12-1
- Rebased to 0.12, svn revision 1154981
- Resolves: bz706996

* Tue Apr 12 2011 Ted Ross <tross@redhat.com> - 0.10-2
- Related: rhbz#693862
- Added ExclusiveArch: i686 x86_64

* Wed Apr  6 2011 Justin Ross <jross@redhat.com> - 0.10-1
- Rebased to 0.10, svn revision 1083082

* Fri May 28 2010 Justin Ross <jross@redhat.com> - 0.1.934605-2
- Resolves: rhbz#597290

* Mon Apr 19 2010 Rafael Schloming <rafaels@redhat.com> - 0.1.934605-1
- Rebased to 934605.

* Tue Jan 12 2010 Rafael Schloming <rafaels@redhat.com> - 0.1.897961-3
- Moved libsaslwrapper.so symlink into devel package.

* Tue Jan 12 2010 Rafael Schloming <rafaels@redhat.com> - 0.1.897961-2
- Bump release.
- Fixed manifest for python-saslwrapper.

* Tue Jan 12 2010 Rafael Schloming <rafaels@redhat.com> - 0.1.897961-1
- Added groups to subpackages.
- Replaced python_sitelib with python_sitearch, use %%global instead of %%define, and killed unused ruby_sitelib.

* Fri Jan  8 2010 Rafael H. Schloming <rafaels@redhat.com> - 0.1.897204-1
- Initial version.
