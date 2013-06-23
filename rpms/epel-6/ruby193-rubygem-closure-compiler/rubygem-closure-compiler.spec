%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name closure-compiler
#%define __jar_repack 0

Summary: Ruby Wrapper for the Google Closure Compiler
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.6
Release: 10%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/documentcloud/closure-compiler/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Ruby Wrapper for the Google Closure Compiler for
JavaScript compression.

%prep
%setup -q -c -T -n  %{gem_name}-%{version}

%build
mkdir -p .%{gem_dir}

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

%{?scl:scl enable %{scl} "}
# gem install compiles any C extensions and installs into a directory
%{?scl:"}
# We set that to be a local directory so that we can move it into the
# buildroot in %%install
%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{SOURCE0}
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 1.1.6-10
- fixing ruby193 scl package (lzap+git@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.6-9
- create directory in %%setup macro (msuchy@redhat.com)

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.6-8
- tune up spec for ruby193 SC (msuchy@redhat.com)

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.6-7
- new package built with tito

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.6-6
- edit spec for Fedora 17 (msuchy@redhat.com)
- rename closure-compiler to rubygem-closure-compiler (msuchy@redhat.com)

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.6-5
- correctly set gem_dir on rhel6 (msuchy@redhat.com)

* Thu Jun 28 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.6-4
- in rhel6 there is no package rubygems-devel (msuchy@redhat.com)

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.6-3
- macros ruby_sitelib and geminstdir are not used (msuchy@redhat.com)
- gem_dir and gem_instdir macros are defined in ruby-devel (msuchy@redhat.com)

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.6-2
- rebase to rubygem-closure-compiler 1.1.6 and polish spec file

* Wed Jun 27 2012 Miroslav Suchý <msuchy@redhat.com>
- rebase to rubygem-closure-compiler 1.1.6 and polish spec file

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 0.3.3-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 0.3.3-1
- Initial package
