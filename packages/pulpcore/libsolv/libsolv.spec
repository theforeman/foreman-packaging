%global libname solv

%bcond_without python2_bindings
%bcond_without python3_bindings
%bcond_with    perl_bindings
%bcond_without ruby_bindings
# Creates special prefixed pseudo-packages from appdata metadata
%bcond_without appdata
# Creates special prefixed "group:", "category:" pseudo-packages
%bcond_without comps
# For rich dependencies
%bcond_without complex_deps
%bcond_without helix_repo
%bcond_without suse_repo
%bcond_without debian_repo
%bcond_without arch_repo
# For handling deb + rpm at the same time
%bcond_without multi_semantics
%bcond_with    zchunk
%bcond_with    zstd

Name:           lib%{libname}
Version:        0.7.12
Release:        1%{?dist}
Summary:        Package dependency solver

License:        BSD
URL:            https://github.com/openSUSE/libsolv
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(rpm)
BuildRequires:  zlib-devel
# -DWITH_LIBXML2=ON
BuildRequires:  libxml2-devel
# -DENABLE_LZMA_COMPRESSION=ON
BuildRequires:  xz-devel
# -DENABLE_BZIP2_COMPRESSION=ON
BuildRequires:  bzip2-devel
%if %{with zstd}
# -DENABLE_ZSTD_COMPRESSION=ON
BuildRequires:  libzstd-devel
%endif
%if %{with zchunk}
# -DENABLE_ZCHUNK_COMPRESSION=ON
BuildRequires:  pkgconfig(zck)
%endif

%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package
  and dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rpm-devel%{?_isa}

%description devel
Development files for %{name}.

%package tools
Summary:        Package dependency solver tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
# repo2solv dependencies. Used as execl()
Requires:       %{_bindir}/find

%description tools
Package dependency solver tools.

%package demo
Summary:        Applications demoing the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}
# solv dependencies. Used as execlp() and system()
Requires:       %{_bindir}/curl
Requires:       %{_bindir}/gpg2

%description demo
Applications demoing the %{name} library.

%if %{with perl_bindings}
%package -n perl-%{libname}
Summary:        Perl bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  perl-devel
BuildRequires:  perl-generators
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-%{libname}
Perl bindings for the %{name} library.
%endif

%if %{with ruby_bindings}
%package -n ruby-%{libname}
Summary:        Ruby bindings for the %{name} library
BuildRequires:  swig
BuildRequires:  ruby-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ruby-%{libname}
Ruby bindings for the %{name} library.
%endif

%if %{with python2_bindings}
%package -n python2-%{libname}
Summary:        Python bindings for the %{name} library
%{?python_provide:%python_provide python2-%{libname}}
BuildRequires:  swig
BuildRequires:  python2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python2-%{libname}
Python bindings for the %{name} library.

Python 2 version.
%endif

%if %{with python3_bindings}
%package -n python3-%{libname}
Summary:        Python bindings for the %{name} library
%{?python_provide:%python_provide python3-%{libname}}
BuildRequires:  swig
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{libname}
Python bindings for the %{name} library.

Python 3 version.
%endif

%prep
%autosetup -p1

%build
%cmake . -B"%{_vpath_builddir}" -GNinja          \
  -DFEDORA=1                                     \
  -DENABLE_RPMDB=ON                              \
  -DENABLE_RPMDB_BYRPMHEADER=ON                  \
  -DENABLE_RPMDB_LIBRPM=ON                       \
  -DENABLE_RPMPKG_LIBRPM=ON                      \
  -DENABLE_RPMMD=ON                              \
  %{?with_comps:-DENABLE_COMPS=ON}               \
  %{?with_appdata:-DENABLE_APPDATA=ON}           \
  -DUSE_VENDORDIRS=ON                            \
  -DWITH_LIBXML2=ON                              \
  -DENABLE_LZMA_COMPRESSION=ON                   \
  -DENABLE_BZIP2_COMPRESSION=ON                  \
  %{?with_zstd:-DENABLE_ZSTD_COMPRESSION=ON}     \
%if %{with zchunk}
  -DENABLE_ZCHUNK_COMPRESSION=ON                 \
  -DWITH_SYSTEM_ZCHUNK=ON                        \
%endif
  %{?with_helix_repo:-DENABLE_HELIXREPO=ON}      \
  %{?with_suse_repo:-DENABLE_SUSEREPO=ON}        \
  %{?with_debian_repo:-DENABLE_DEBIAN=ON}        \
  %{?with_arch_repo:-DENABLE_ARCHREPO=ON}        \
  %{?with_multi_semantics:-DMULTI_SEMANTICS=ON}  \
  %{?with_complex_deps:-DENABLE_COMPLEX_DEPS=1}  \
  %{?with_perl_bindings:-DENABLE_PERL=ON}        \
  %{?with_ruby_bindings:-DENABLE_RUBY=ON}        \
%if %{with python2_bindings} || %{with python3_bindings}
  -DENABLE_PYTHON=ON                             \
%if %{with python2_bindings}
  -DPYTHON_EXECUTABLE=%{__python2}               \
%if %{with python3_bindings}
  -DENABLE_PYTHON3=ON                            \
  -DPYTHON3_EXECUTABLE=%{__python3}              \
%endif
%else
  -DPYTHON_EXECUTABLE=%{__python3}               \
%endif
%endif
  %{nil}
%ninja_build -C "%{_vpath_builddir}"

%install
%ninja_install -C "%{_vpath_builddir}"

%check
%ninja_test -C "%{_vpath_builddir}"

%files
%license LICENSE*
%doc README
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}ext.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}ext.so
%{_includedir}/%{libname}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}ext.pc
# Own directory because we don't want to depend on cmake
%dir %{_datadir}/cmake/Modules/
%{_datadir}/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man3/%{name}*.3*

# Some small macro to list tools with mans
%global solv_tool() \
%{_bindir}/%{1}\
%{_mandir}/man1/%{1}.1*

%files tools
%solv_tool deltainfoxml2solv
%solv_tool dumpsolv
%solv_tool installcheck
%solv_tool mergesolv
%solv_tool repomdxml2solv
%solv_tool rpmdb2solv
%solv_tool rpmmd2solv
%solv_tool rpms2solv
%solv_tool testsolv
%solv_tool updateinfoxml2solv
%solv_tool repo2solv
%if %{with comps}
  %solv_tool comps2solv
%endif
%if %{with appdata}
  %solv_tool appdata2solv
%endif
%if %{with debian_repo}
  %solv_tool deb2solv
%endif
%if %{with arch_repo}
  %solv_tool archpkgs2solv
  %solv_tool archrepo2solv
%endif
%if %{with helix_repo}
  %solv_tool helix2solv
%endif
%if %{with suse_repo}
  %solv_tool susetags2solv
%endif

%files demo
%solv_tool solv

%if %{with perl_bindings}
%files -n perl-%{libname}
%{perl_vendorarch}/%{libname}.pm
%{perl_vendorarch}/%{libname}.so
%endif

%if %{with ruby_bindings}
%files -n ruby-%{libname}
%{ruby_vendorarchdir}/%{libname}.so
%endif

%if %{with python2_bindings}
%files -n python2-%{libname}
%{python2_sitearch}/_%{libname}.so
%{python2_sitearch}/%{libname}.py*
%endif

%if %{with python3_bindings}
%files -n python3-%{libname}
%{python3_sitearch}/_%{libname}.so
%{python3_sitearch}/%{libname}.py
%{python3_sitearch}/__pycache__/%{libname}.*
%endif

%changelog
* Tue Apr 21 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.12-1
- Update to 0.7.12
