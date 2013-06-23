%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sexp_processor
%global rubyabi 1.9.1 

Summary: sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.1.3
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/seattlerb/sexp_processor
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi} 
Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

%build
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}
%{?scl:"}

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
