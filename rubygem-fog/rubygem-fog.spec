%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog

Summary: brings clouds to you
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.28.0
Release: 1%{dist}
Group: Development/Ruby
License: MIT
URL: http://github.com/fog/fog
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch1:  fog-no-brightbox.patch
Patch2:  fog-no-sakuracloud.patch
Patch3:  fog-no-softlayer.patch
Patch4:  fog-no-profitbricks.patch
Patch5:  fog-no-voxel.patch
Patch6:  fog-no-vmfusion.patch
Patch7:  fog-no-terremark.patch
Patch8:  fog-no-ecloud.patch
Patch9:  fog-no-storm_on_demand.patch
Patch10: fog-no-atmos.patch
Patch11: fog-no-serverlove.patch
Patch12: fog-no-riakcs.patch

Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(fog-aws) >= 0
Requires: %{?scl_prefix}rubygem(fog-aws) < 1
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.27.3
Requires: %{?scl_prefix}rubygem(fog-core) < 2.0.0
Requires: %{?scl_prefix}rubygem(fog-json)
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 0.2.0
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.4
Requires: %{?scl_prefix}rubygem(ipaddress) < 1.0
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.5.11
Requires: %{?scl_prefix}rubygem(nokogiri) < 2.0
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif

BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygem(fog-aws) >= 0
BuildRequires: %{?scl_prefix}rubygem(fog-aws) < 1
BuildRequires: %{?scl_prefix}rubygem(fog-core) >= 1.27.3
BuildRequires: %{?scl_prefix}rubygem(fog-core) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(fog-json)
BuildRequires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
BuildRequires: %{?scl_prefix}rubygem(fog-xml) < 0.2.0
BuildRequires: %{?scl_prefix}rubygem(ipaddress) >= 0.4
BuildRequires: %{?scl_prefix}rubygem(ipaddress) < 1.0
BuildRequires: %{?scl_prefix}rubygem(nokogiri) >= 1.5.11
BuildRequires: %{?scl_prefix}rubygem(nokogiri) < 2.0
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(fog) = %{version}

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
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

# Patch out providers we don't need
%patch1 -p1
sed -i '/add_.*dependency.*brightbox/d' %{gem_name}.gemspec
sed -i '/add_.*dependency.*radosgw/d' %{gem_name}.gemspec
%patch2 -p1
sed -i '/add_.*dependency.*sakuracloud/d' %{gem_name}.gemspec
%patch3 -p1
sed -i '/add_.*dependency.*softlayer/d' %{gem_name}.gemspec
%patch4 -p1
sed -i '/add_.*dependency.*profitbricks/d' %{gem_name}.gemspec
%patch5 -p1
sed -i '/add_.*dependency.*voxel/d' %{gem_name}.gemspec
%patch6 -p1
sed -i '/add_.*dependency.*vmfusion/d' %{gem_name}.gemspec
%patch7 -p1
sed -i '/add_.*dependency.*terremark/d' %{gem_name}.gemspec
%patch8 -p1
sed -i '/add_.*dependency.*ecloud/d' %{gem_name}.gemspec
%patch9 -p1
sed -i '/add_.*dependency.*storm_on_demand/d' %{gem_name}.gemspec
%patch10 -p1
sed -i '/add_.*dependency.*atmos/d' %{gem_name}.gemspec
%patch11 -p1
sed -i '/add_.*dependency.*serverlove/d' %{gem_name}.gemspec
%patch12 -p1
sed -i '/add_.*dependency.*riakcs/d' %{gem_name}.gemspec

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --no-rdoc --no-ri \
            --force %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* %{buildroot}%{_bindir}/

%check
# Verify that patching resulted in a valid gemspec and the library still loads
%{?scl:scl enable %{scl} - << \EOF}
export RUBYLIB=$RUBYLIB:$(pwd)/lib
ruby -rfog -rfog/version -e 'puts Fog::VERSION; puts Fog.providers.keys.join(",")'
bin/fog -v
%{?scl:EOF}

%files
%dir %{gem_instdir}
%{gem_instdir}/benchs
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.md
%{gem_spec}
%{_bindir}/fog
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/RELEASE.md
%{gem_instdir}/gemfiles
%{gem_instdir}/spec
%{gem_instdir}/tests
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%{gem_instdir}/fog.gemspec

%changelog
* Sun Feb 22 2015 Daniel Lobato <dlobatog@redhat.com> 1.28.0-1
- Update fog to 1.28.0 (dlobatog@redhat.com)

* Tue Feb 17 2015 Dominic Cleal <dcleal@redhat.com> 1.27.0-1
- Update fog to 1.27.0 (dcleal@redhat.com)

* Wed Nov 26 2014 Dominic Cleal <dcleal@redhat.com> 1.25.0-1
- Update fog to 1.25.0 (dcleal@redhat.com)

* Thu Nov 20 2014 Dominic Cleal <dcleal@redhat.com> 1.24.0-3
- Fix removal of add_runtime_dependency lines in gemspec (dcleal@redhat.com)

* Wed Nov 19 2014 Dominic Cleal <dcleal@redhat.com> 1.24.0-2
- Remove fog-brightbox, radosgw, sakuracloud, softlayer dependencies
  (dcleal@redhat.com)

* Mon Oct 13 2014 Dominic Cleal <dcleal@redhat.com> 1.24.0-1
- refs #7879 - update fog to v1.24.0 (dcleal@redhat.com)

* Tue Jul 22 2014 Dominic Cleal <dcleal@redhat.com> 1.23.0-1
- Rebase to fog 1.23.0 (dcleal@redhat.com)

* Tue Mar 25 2014 Dominic Cleal <dcleal@redhat.com> 1.21.0-2
- Add dependency on fog-brightbox (dcleal@redhat.com)

* Wed Mar 19 2014 Dominic Cleal <dcleal@redhat.com> 1.21.0-1
- Rebase to fog 1.21.0 (dcleal@redhat.com)

* Tue Mar 11 2014 Dominic Cleal <dcleal@redhat.com> 1.20.0-1
- Rebase to fog 1.20.0 (dcleal@redhat.com)

* Tue Jan 07 2014 Dominic Cleal <dcleal@redhat.com> 1.19.0-1
- Rebase to fog 1.19.0 (dcleal@redhat.com)

* Wed Nov 06 2013 Dominic Cleal <dcleal@redhat.com> 1.18.0-1
- Rebase to fog 1.18.0 (dcleal@redhat.com)

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

