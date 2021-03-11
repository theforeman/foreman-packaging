%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name net-scp

Summary: A pure Ruby implementation of the SCP client protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.1
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: http://net-ssh.rubyforge.org/scp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix test broken due to Net::SSH 4.0+.
# https://github.com/net-ssh/net-scp/pull/30
Patch0: net-scp-1.2.1-Fix-compatiblity-with-net-ssh-4.0.patch
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(net-ssh)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A pure Ruby implementation of the SCP client protocol


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/net-scp.gemspec
%{gem_instdir}/gem-public_cert.pem
%exclude %{gem_instdir}/setup.rb
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/test
%doc %{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.2.1-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.1-4
- Bump release to build for el8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.1-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri May 19 2017 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Update net-scp to 1.2.1 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-6
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-5
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Fix build errors and modernise specs (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.1.0-3
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri May 03 2013 Ivan Necas <inecas@redhat.com> 1.1.0-2
- Net scp requires newer mocha for running tests (inecas@redhat.com)

* Fri May 03 2013 Ivan Necas <inecas@redhat.com> 1.1.0-1
- Update due to fog dependency (inecas@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.4-6
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.4-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 17 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.4-2
- Removed obsolete cleanup.
- Removed explicit requires.

* Tue Feb 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.4-1
- Initial package
