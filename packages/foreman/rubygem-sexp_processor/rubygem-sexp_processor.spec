%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sexp_processor

Summary: sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.10.0
Release: 7%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/seattlerb/sexp_processor
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# Drop the standalone mode - won't run that way due to missing rubygems require
# anyway
find %{buildroot}%{gem_instdir}/test -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/.*\/ruby.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}%{gem_instdir} -type f | \
  xargs chmod 0644

rm -f %{buildroot}%{gem_instdir}/.gemtest

%files
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%dir %{gem_instdir}
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.10.0-7
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.10.0-6
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.10.0-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.10.0-4
- Bump rubygem-sexp_processor to 4.10.0 (dmitri@appliedlogic.ca)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.4.4-4
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.4.4-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 4.4.4-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 4.4.4-1
- Update sexp_processor to 4.4.4 (dcleal@redhat.com)
- Build for Fedora 19 (dcleal@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 4.1.3-4
- rebase to sexp_processor-4.1.3 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 4.1.3-3
- define libdir for el6 (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 4.1.3-2
- tune up spec (msuchy@redhat.com)
- rebase to sexp_processor-4.1.3.gem (msuchy@redhat.com)

* Fri Oct 26 2012 Dmitri Dolguikh <dmitri@appliedlogic.ca> 4.1.0-1
- new package built with tito

* Fri Oct 26 2012 wb - 4.1.0-1
- Initial package
