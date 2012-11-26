%define rbname ffi
%define version 1.0.11
%define release 1

Summary: Ruby-FFI is a ruby extension for programmatically loading dynamic libraries, binding functions within them, and calling those functions from Ruby code
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://wiki.github.com/ffi/ffi
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildRequires: libffi-devel
BuildRequires: ruby-devel
BuildRequires: gcc
Provides: rubygem(ffi) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here[http://wiki.github.com/ffi/ffi/why-use-ffi].


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gemdir}/gems/ffi-1.0.11/History.txt
%{gemdir}/gems/ffi-1.0.11/LICENSE
%doc %{gemdir}/gems/ffi-1.0.11/README.rdoc
%{gemdir}/gems/ffi-1.0.11/Rakefile
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/AbstractMemory.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/AbstractMemory.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ArrayType.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ArrayType.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Buffer.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Call.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Call.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ClosurePool.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ClosurePool.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/DataConverter.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/DynamicLibrary.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/DynamicLibrary.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Function.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Function.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/FunctionInfo.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/LastError.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/LastError.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MappedType.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MappedType.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MemoryPointer.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MemoryPointer.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MethodHandle.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MethodHandle.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Platform.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Platform.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Pointer.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Pointer.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Struct.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Struct.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructByReference.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructByReference.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructByValue.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructByValue.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructLayout.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Thread.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Thread.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Type.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Type.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Types.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Types.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Variadic.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/compat.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/endian.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/extconf.rb
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi.bsd.mk
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi.darwin.mk
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi.gnu.mk
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi.mk
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/ChangeLog
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/ChangeLog.libffi
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/ChangeLog.libgcj
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/ChangeLog.v1
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/LICENSE
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/Makefile.am
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/Makefile.in
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/README
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/acinclude.m4
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/aclocal.m4
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/compile
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/config.guess
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/config.sub
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/configure
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/configure.ac
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/configure.host
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/depcomp
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/doc/libffi.info
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/doc/libffi.texi
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/doc/stamp-vti
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/doc/version.texi
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/fficonfig.h.in
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/include/Makefile.am
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/include/Makefile.in
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/include/ffi.h.in
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/include/ffi_common.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/install-sh
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/libffi.pc.in
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/libtool-version
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/ltmain.sh
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/m4/libtool.m4
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/m4/ltoptions.m4
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/m4/ltsugar.m4
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/m4/ltversion.m4
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/m4/lt~obsolete.m4
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/man/Makefile.am
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/man/Makefile.in
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/man/ffi.3
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/man/ffi_call.3
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/man/ffi_prep_cif.3
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/mdate-sh
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/missing
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/alpha/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/alpha/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/alpha/osf.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/arm/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/arm/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/arm/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/avr32/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/avr32/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/avr32/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/closures.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/cris/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/cris/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/cris/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/debug.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/dlmalloc.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/frv/eabi.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/frv/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/frv/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/ia64/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/ia64/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/ia64/ia64_flags.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/ia64/unix.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/java_raw_api.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/m32r/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/m32r/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/m32r/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/m68k/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/m68k/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/m68k/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/mips/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/mips/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/mips/n32.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/mips/o32.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/pa/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/pa/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/pa/hpux32.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/pa/linux.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/aix.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/aix_closure.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/asm.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/darwin.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/darwin_closure.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/ffi_darwin.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/linux64.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/linux64_closure.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/ppc_closure.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/powerpc/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/prep_cif.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/raw_api.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/s390/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/s390/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/s390/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sh/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sh/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sh/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sh64/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sh64/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sh64/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sparc/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sparc/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sparc/v8.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/sparc/v9.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/types.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/darwin.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/darwin64.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/ffi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/ffi64.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/ffitarget.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/freebsd.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/sysv.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/unix64.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/win32.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/src/x86/win64.S
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/Makefile.am
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/Makefile.in
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/config/default.exp
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/lib/libffi-dg.exp
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/lib/target-libpath.exp
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/lib/wrapper.exp
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/call.exp
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_fn0.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_fn1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_fn2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_fn3.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_fn4.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_fn5.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_fn6.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_loc_fn0.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/closure_stdcall.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_12byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_16byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_18byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_19byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_1_1byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_20byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_20byte1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_24byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_2byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_3_1byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_3byte1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_3byte2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_4_1byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_4byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_5_1_byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_5byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_64byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_6_1_byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_6byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_7_1_byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_7byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_8byte.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_9byte1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_9byte2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_double.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_float.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_longdouble.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_longdouble_split.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_longdouble_split2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_pointer.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_sint16.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_sint32.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_sint64.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_uint16.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_uint32.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_align_uint64.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_dbls_struct.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_double.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_double_va.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_float.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_longdouble.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_longdouble_va.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_multi_schar.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_multi_sshort.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_multi_sshortchar.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_multi_uchar.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_multi_ushort.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_multi_ushortchar.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_pointer.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_pointer_stack.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_schar.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_sint.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_sshort.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_uchar.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_uint.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_ulonglong.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/cls_ushort.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/err_bad_abi.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/err_bad_typedef.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/ffitest.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/float.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/float1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/float2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/float3.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/float4.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/huge_struct.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/many.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/many_win32.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/negint.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct10.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct3.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct4.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct5.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct6.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct7.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct8.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/nested_struct9.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/problem1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/promotion.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/pyobjc-tc.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_dbl.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_dbl1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_dbl2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_fl.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_fl1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_fl2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_fl3.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_ldl.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_ll.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_ll1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_sc.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_sl.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_uc.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/return_ul.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/stret_large.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/stret_large2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/stret_medium.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/stret_medium2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/strlen.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/strlen_win32.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct1.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct2.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct3.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct4.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct5.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct6.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct7.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct8.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/struct9.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.call/testclosure.c
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.special/ffitestcxx.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.special/special.exp
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.special/unwindtest.cc
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/testsuite/libffi.special/unwindtest_ffi_call.cc
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/libffi/texinfo.tex
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/rbffi.h
%{gemdir}/gems/ffi-1.0.11/gen/Rakefile
%{gemdir}/gems/ffi-1.0.11/lib/ffi.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/autopointer.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/buffer.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/callback.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/enum.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/errno.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/ffi.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/io.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/library.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/managedstruct.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/memorypointer.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/platform.rb
%doc /usr/lib/ruby/gems/1.8/doc/ffi-1.0.11/ri
%doc /usr/lib/ruby/gems/1.8/doc/ffi-1.0.11/rdoc
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/i386-darwin/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/i386-freebsd/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/i386-linux/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/i386-netbsd/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/i386-openbsd/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/i386-solaris/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/i386-windows/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/powerpc-aix/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/powerpc-darwin/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/sparc-solaris/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/sparcv9-solaris/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/x86_64-darwin/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/x86_64-freebsd/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/x86_64-linux/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/x86_64-netbsd/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/x86_64-openbsd/types.conf
%doc %{gemdir}/gems/ffi-1.0.11/lib/ffi/platform/x86_64-solaris/types.conf
%{gemdir}/gems/ffi-1.0.11/lib/ffi/pointer.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/struct.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/struct_layout_builder.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/tools/const_generator.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/tools/generator.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/tools/generator_task.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/tools/struct_generator.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/tools/types_generator.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/types.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/union.rb
%{gemdir}/gems/ffi-1.0.11/lib/ffi/variadic.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/async_callback_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/bool_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/buffer_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/callback_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/custom_param_type.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/custom_type_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/dup_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/enum_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/errno_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/ffi_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/function_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/library_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/managed_struct_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/number_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/pointer_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/rbx/attach_function_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/rbx/memory_pointer_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/rbx/spec_helper.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/rbx/struct_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/spec_helper.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/string_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/strptr_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/struct_callback_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/struct_initialize_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/struct_packed_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/struct_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/typedef_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/union_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/ffi/variadic_spec.rb
%{gemdir}/gems/ffi-1.0.11/spec/spec.opts
%{gemdir}/gems/ffi-1.0.11/tasks/ann.rake
%{gemdir}/gems/ffi-1.0.11/tasks/extension.rake
%{gemdir}/gems/ffi-1.0.11/tasks/gem.rake
%{gemdir}/gems/ffi-1.0.11/tasks/git.rake
%{gemdir}/gems/ffi-1.0.11/tasks/notes.rake
%{gemdir}/gems/ffi-1.0.11/tasks/post_load.rake
%{gemdir}/gems/ffi-1.0.11/tasks/rdoc.rake
%{gemdir}/gems/ffi-1.0.11/tasks/rubyforge.rake
%{gemdir}/gems/ffi-1.0.11/tasks/setup.rb
%{gemdir}/gems/ffi-1.0.11/tasks/spec.rake
%{gemdir}/gems/ffi-1.0.11/tasks/svn.rake
%{gemdir}/gems/ffi-1.0.11/tasks/test.rake
%{gemdir}/gems/ffi-1.0.11/tasks/yard.rake
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/AbstractMemory.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ArrayType.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Buffer.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Call.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ClosurePool.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/DataConverter.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/DynamicLibrary.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Function.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/FunctionInfo.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/LastError.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Makefile
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MappedType.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MemoryPointer.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/MethodHandle.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Platform.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Pointer.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Struct.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructByReference.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructByValue.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/StructLayout.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Thread.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Type.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Types.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/Variadic.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/extconf.h
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ffi.o
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/ffi_c.so
%{gemdir}/gems/ffi-1.0.11/ext/ffi_c/mkmf.log
%{gemdir}/gems/ffi-1.0.11/lib/ffi_c.so
%{gemdir}/specifications/ffi-1.0.11.gemspec
/usr/lib/ruby/gems/1.8/cache/ffi-1.0.11.gem
%changelog
