%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ruport

Summary: A generalized Ruby report generation and templating engine
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.7.0
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/ruport/ruport
Source0: ruport-1.7.0-66f9758a0e.zip
# can be removed as https://github.com/ruport/ruport/pull/19 is merged
Patch0: 0001_improve_prawn_support.patch
Patch1: 0002_refactoring_improve_prawn_support.patch
Patch2: 0003_fixing_prawn_depend_for_ruport.patch
Patch3: 0004_ruby_version_check_fastercsv.patch
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(fastercsv) >= 0
Requires: %{?scl_prefix}rubygem(pdf-writer) = 1.1.8
Requires: %{?scl_prefix}rubygem(prawn)
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby Reports is a software library that aims to make the task of reporting
less tedious and painful. It provides tools for data acquisition,
database interaction, formatting, and parsing/munging.

%package doc
BuildArch: noarch
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary: Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} "}
#gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -n ruport-ruport-66f9758
%patch0 -p1 -b .patch0
%patch1 -p1 -b .patch1
%patch2 -p1 -b .patch2
%patch3 -p1 -b .patch3

#gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/COPYING

%files doc
%doc %{gem_docdir}
%{gem_instdir}/util
%{gem_instdir}/test
%{gem_instdir}/examples
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/HACKING
%doc %{gem_instdir}/AUTHORS

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.7.0-5
- new package built with tito

* Mon Dec 10 2012 Eric D Helms <ehelms@redhat.com> 1.7.0-4
- Rubygem-ruport - Adds patch to include check of Ruby version in the gemspec
  to include or not dependency on fastercsv. (ehelms@redhat.com)

* Fri Dec 07 2012 Miroslav Suchý <msuchy@redhat.com> 1.7.0-3
- fastercvs is used only for RUBY_VERSION < "1.9" (msuchy@redhat.com)

* Wed Nov 14 2012 Miroslav Suchý <msuchy@redhat.com> 1.7.0-2
- require rubygem(prawn) (msuchy@redhat.com)

* Thu Oct 11 2012 Miroslav Suchý <msuchy@redhat.com> 1.7.0-1
- add 0001-Improve-Prawn-support.patch patch (msuchy@redhat.com)
- build rubygem-ruport from git HEAD to include new prawn backend
  (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.6.3-4
- add missing -a to cp in %%install (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.6.3-3
- edit spec for Fedora 17 (msuchy@redhat.com)

* Thu Oct 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.6.3-2
- bumped up the version of the rupert spec file (dmitri@redhat.com)
- fixed rupert spec file (dmitri@redhat.com)

* Thu Oct 06 2011 Dmitri Dolguikh <dmitri@redhat.com>
- fixed rupert spec file (dmitri@redhat.com)

* Thu Oct 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.6.3-1
- new package built with tito

* Thu Oct 06 2011  <wb@killing-time.appliedlogic.ca> - 1.6.3-1
- Initial package
