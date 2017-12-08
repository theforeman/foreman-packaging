%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog

Summary: brings clouds to you
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.42.0
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/fog/fog
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Maintained at https://github.com/theforeman/fog, branch v%{version}-simplify
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
Patch13: fog-no-local.patch
Patch14: fog-no-powerdns.patch
Patch15: fog-no-dynect.patch
Patch16: fog-no-aliyun.patch
Patch17: fog-no-dnsimple.patch
Patch18: fog-no-internet_archive.patch
Patch19: fog-no-joyent.patch

Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-aws) >= 0.6.0
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.45.0
Requires: %{?scl_prefix}rubygem(fog-core) < 2.0.0
Requires: %{?scl_prefix}rubygem(fog-digitalocean) >= 0.3.0
Requires: %{?scl_prefix}rubygem(fog-google) <= 0.1.0
Requires: %{?scl_prefix}rubygem(fog-json)
Requires: %{?scl_prefix}rubygem(fog-openstack)
Requires: %{?scl_prefix}rubygem(fog-ovirt)
Requires: %{?scl_prefix}rubygem(fog-rackspace)
Requires: %{?scl_prefix}rubygem(fog-vsphere) >= 0.4.0
Requires: %{?scl_prefix}rubygem(fog-xenserver)
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 0.2.0
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.5
Requires: %{?scl_prefix}rubygem(ipaddress) < 1.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.0
Requires: %{?scl_prefix_ruby}ruby(release)

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(fog-aws) >= 0.6.0
BuildRequires: %{?scl_prefix}rubygem(fog-core) >= 1.45.0
BuildRequires: %{?scl_prefix}rubygem(fog-core) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(fog-digitalocean) >= 0.3.0
BuildRequires: %{?scl_prefix}rubygem(fog-google) <= 0.1.0
BuildRequires: %{?scl_prefix}rubygem(fog-json)
BuildRequires: %{?scl_prefix}rubygem(fog-openstack)
BuildRequires: %{?scl_prefix}rubygem(fog-ovirt)
BuildRequires: %{?scl_prefix}rubygem(fog-rackspace)
BuildRequires: %{?scl_prefix}rubygem(fog-vsphere) >= 0.4.0
BuildRequires: %{?scl_prefix}rubygem(fog-xenserver)
BuildRequires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
BuildRequires: %{?scl_prefix}rubygem(fog-xml) < 0.2.0
BuildRequires: %{?scl_prefix}rubygem(ipaddress) >= 0.5
BuildRequires: %{?scl_prefix}rubygem(ipaddress) < 1.0
BuildRequires: %{?scl_prefix_ruby}rubygem(json) >= 2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(fog) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Obsoletes: %{?scl:ruby193-}rubygem-fog-brightbox
Obsoletes: %{?scl:ruby193-}rubygem-fog-radosgw
Obsoletes: %{?scl:ruby193-}rubygem-fog-sakuracloud
Obsoletes: %{?scl:ruby193-}rubygem-fog-softlayer

%description
The Ruby cloud services library. Supports all major cloud providers including
AWS, Rackspace, Linode, Blue Box, StormOnDemand, and many others. Full support
for most AWS services including EC2, S3, CloudWatch, SimpleDB, ELB, and RDS.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
%patch13 -p1
sed -i '/add_.*dependency.*fog-local/d' %{gem_name}.gemspec
%patch14 -p1
sed -i '/add_.*dependency.*powerdns/d' %{gem_name}.gemspec
%patch15 -p1
sed -i '/add_.*dependency.*dynect/d' %{gem_name}.gemspec
%patch16 -p1
sed -i '/add_.*dependency.*aliyun/d' %{gem_name}.gemspec
sed -i '/add_.*dependency.*cloudatcost/d' %{gem_name}.gemspec
%patch17 -p1
sed -i '/add_.*dependency.*dnsimple/d' %{gem_name}.gemspec
%patch18 -p1
sed -i '/add_.*dependency.*internet-archive/d' %{gem_name}.gemspec
%patch19 -p1
sed -i '/add_.*dependency.*joyent/d' %{gem_name}.gemspec

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{gem_name}-%{version}.gem
%{?scl:EOF}


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
%doc %{gem_docdir}
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
* Wed Aug 30 2017 Eric D. Helms <ericdhelms@gmail.com> 1.41.0-2
- Properly remove the internet-archive dependency (ewoud@kohlvanwijngaarden.nl)

* Fri Aug 25 2017 Michael Moll <kvedulv@kvedulv.de> 1.41.0-1
- Update fog to 1.41 (me@daniellobato.me)

* Mon May 22 2017 Dominic Cleal <dominic@cleal.org> 1.40.0-1
- Update fog to 1.40.0 (dominic@cleal.org)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Mar 31 2016 Dominic Cleal <dominic@cleal.org> 1.38.0-1
- Update fog to 1.38.0 (dominic@cleal.org)

* Tue Jan 19 2016 Dominic Cleal <dcleal@redhat.com> 1.37.0-1
- Update fog to 1.37.0 (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.36.0-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 20 2015 Dominic Cleal <dcleal@redhat.com> 1.36.0-1
- Update fog to 1.36.0 (dcleal@redhat.com)

* Thu Nov 19 2015 Dominic Cleal <dcleal@redhat.com> 1.34.0-2
- Obsolete old Fog packages, #12509 (dcleal@redhat.com)

* Tue Sep 08 2015 Dominic Cleal <dcleal@redhat.com> 1.34.0-1
- Update fog to 1.34.0 (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.33.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Aug 18 2015 Dominic Cleal <dcleal@redhat.com> 1.33.0-1
- Update fog to 1.33.0 (dcleal@redhat.com)

* Fri Jul 03 2015 Dominic Cleal <dcleal@redhat.com> 1.32.0-1
- Update fog to 1.32.0 (dcleal@redhat.com)

* Mon May 11 2015 Dominic Cleal <dcleal@redhat.com> 1.30.0-1
- Update fog to 1.30.0 (dcleal@redhat.com)

* Fri Apr 24 2015 Dominic Cleal <dcleal@redhat.com> 1.29.0-1
- Update fog to 1.29.0 (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

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
