%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog

Summary: brings clouds to you
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.15.0
Release: 2%{dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem-builder 
Requires: %{?scl_prefix}rubygem-excon >= 0.25.0
Requires: %{?scl_prefix}rubygem-excon < 0.26.0
Requires: %{?scl_prefix}rubygem-formatador => 0.2.0
Requires: %{?scl_prefix}rubygem-formatador < 0.3
Requires: %{?scl_prefix}rubygem-multi_json => 1.0
Requires: %{?scl_prefix}rubygem-multi_json < 2
Requires: %{?scl_prefix}rubygem-mime-types 
Requires: %{?scl_prefix}rubygem-net-scp => 1.1.0
Requires: %{?scl_prefix}rubygem-net-scp < 2
Requires: %{?scl_prefix}rubygem-net-ssh >= 2.1.3
Requires: %{?scl_prefix}rubygem-nokogiri => 1.5.0
Requires: %{?scl_prefix}rubygem-nokogiri < 2
Requires: %{?scl_prefix}rubygem-ruby-hmac 
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(fog) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
The Ruby cloud services library. Supports all major cloud providers including
AWS, Rackspace, Linode, Blue Box, StormOnDemand, and many others. Full support
for most AWS services including EC2, S3, CloudWatch, SimpleDB, ELB, and RDS.

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
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0} --no-rdoc --no-ri 
%{?scl:"}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/{.document,.gitignore,.irbrc,.travis.yml}

%files
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/benchs
%exclude %{gem_cache}
%{gem_spec}
%{_bindir}/fog

%files doc
%{gem_instdir}/README.md
%{gem_instdir}/RELEASE.md
%{gem_instdir}/tests
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/changelog.txt
%{gem_instdir}/fog.gemspec

%changelog
* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.15.0-2
- Bump fog version to 1.15.0 (shk@redhat.com)

* Mon Jul 22 2013 Dominic Cleal <dcleal@redhat.com> 1.14.0-1
- Rebase to fog 1.14.0 (dcleal@redhat.com)
- Fix excon dependency version (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.12.1-2
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Tue Jun 11 2013 Dominic Cleal <dcleal@redhat.com> 1.12.1-1
- Rebase to fog 1.12.1 (dcleal@redhat.com)

* Sun May 26 2013 Dominic Cleal <dcleal@redhat.com> 1.11.1-3
- Fix patch path for non-SCL installs (dcleal@redhat.com)

* Sun May 26 2013 Dominic Cleal <dcleal@redhat.com> 1.11.1-2
- Patch gemspec to enable multi_json as an optional json replacement
  (dcleal@redhat.com)

* Sun May 26 2013 Dominic Cleal <dcleal@redhat.com> 1.11.1-1
- Update to fog 1.11.1 (dcleal@redhat.com)

* Fri May 03 2013 Ivan Necas <inecas@redhat.com> 1.10.1-9
- update dep specs (inecas@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri Apr 26 2013 Sam Kottler <shk@redhat.com> 1.10.1-8
- Added RELEASE.md to spec (shk@redhat.com)

* Fri Apr 26 2013 Sam Kottler <shk@redhat.com> 1.10.1-7
- Moved readme to %%files (shk@redhat.com)

* Fri Apr 26 2013 Sam Kottler <shk@redhat.com> 1.10.1-6
- Fixed README (shk@redhat.com)

* Fri Apr 26 2013 Sam Kottler <shk@redhat.com> 1.10.1-5
- Updated the spec to no longer include docs/ for rubygem-fog (shk@redhat.com)

* Fri Apr 26 2013 Sam Kottler <shk@redhat.com> 1.10.1-4
- Added fog 1.10.1 binary (shk@redhat.com)

* Fri Apr 26 2013 Sam Kottler <shk@redhat.com> 1.10.1-3
- Automatic commit of package [rubygem-fog] minor release [1.10.1-2].
  (shk@redhat.com)

* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.8.0-3
- put correct license in spec (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 1.8.0-2
- rebase to fog-1.8.0 (msuchy@redhat.com)

* Fri Dec 07 2012 Ivan Necas <inecas@redhat.com> 1.8.0-1
- Update to version 1.8 (inecas@redhat.com)

* Thu Nov 08 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-4
- rebuild with rubygems 1.8

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-3
- polish the spec (msuchy@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-2
- remove version requirements on rubygem (msuchy@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com>
- remove version requirements on rubygem (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.0-1
- new package built with tito

