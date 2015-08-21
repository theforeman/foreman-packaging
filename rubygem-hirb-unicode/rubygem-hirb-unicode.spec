%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hirb-unicode

Summary: Unicode support for hirb
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.0.5
Release: 5%{?dist}
Group: Development/Ruby
License: MIT
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem-hirb => 0.5
Requires: %{?scl_prefix}rubygem-hirb < 1

Requires: %{?scl_prefix}rubygem-unicode-display_width => 0.1.1
Requires: %{?scl_prefix}rubygem-unicode-display_width < 0.2
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(hirb-unicode) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%global gembuilddir %{buildroot}%{gem_dir}

%description
Unicode support for hirb

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{?scl:"}
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/.gitignore

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Gemfile

%changelog
* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.5-5
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.5-3
- new package built with tito

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.5-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.5-1
- new package built with tito
