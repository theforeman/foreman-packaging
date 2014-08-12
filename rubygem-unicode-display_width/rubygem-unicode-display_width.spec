%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name unicode-display_width

Summary: Support for east_asian_width string widths.
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.1.1
Release: 6%{dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/janlelis/unicode-display_width
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(unicode-display_width) = %{version}

%global gembuilddir %{buildroot}%{gem_dir}

%description
This gem adds String#display_size to get the display size of a string using
EastAsianWidth.txt.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{?scl:"}
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/data
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/.gemspec

%changelog
* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.1-4
- new package built with tito

* Mon Sep 10 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.1-3
- remove yardoc (msuchy@redhat.com)

* Mon Sep 10 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.1-2
- new package built with tito

