%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name excon

Summary: Http(s) EXtended CONnections
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.76.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/geemus/excon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: ca-certificates
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: ca-certificates
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
EXtended http(s) CONnections

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
Documentation for %{pkg_name}

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

# kill bundled cacert.pem
ln -sf /etc/pki/tls/cert.pem \
	%{buildroot}%{gem_instdir}/data/cacert.pem

%check
#pushd .%{gem_instdir}
## we need to remove the dependency on bundler and add the missing requires (workaround for not using the Rakefile)
## do not require bundler
#sed -i -e "s/'bundler'/'open4'\nrequire 'delorean'/" -e '/Bundler.require(:default, :development)/d' tests/test_helper.rb
#
## require the other needed libs
## https://github.com/geemus/excon/issues/135#issuecomment-7181061
#RUBYOPT="-r./lib/excon -rsecurerandom" shindo
#popd

%files
%dir %{gem_instdir}
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.md

%files doc
%{gem_instdir}/excon.gemspec
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/LICENSE.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.76.0-2
- Rebuild against rh-ruby27

* Mon Aug 03 2020 Bernhard Suttner <suttner@atix.de> 0.76.0-1
- Update to 0.76.0 (mainly because of https://github.com/excon/excon/issues/718)

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.58.0-5
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.58.0-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.58.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.58.0-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Aug 24 2017 Eric D. Helms <ericdhelms@gmail.com> 0.58.0-1
- Update excon to 0.58 (me@daniellobato.me)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 0.51.0-1
- Update excon to 0.51.0 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.49.0-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.49.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Mar 31 2016 Dominic Cleal <dominic@cleal.org> 0.49.0-1
- Update excon to 0.49.0 (dominic@cleal.org)

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> 0.48.0-1
- Update excon to 0.48.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.45.3-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.45.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jul 03 2015 Dominic Cleal <dcleal@redhat.com> 0.45.3-1
- Update excon to 0.45.3 (dcleal@redhat.com)

* Fri Jan 23 2015 Dominic Cleal <dcleal@redhat.com> 0.43.0-1
- Update excon to 0.43.0 (dcleal@redhat.com)

* Thu Nov 20 2014 Dominic Cleal <dcleal@redhat.com> 0.41.0-1
- Rebase to excon 0.41.0 (dcleal@redhat.com)

* Tue Jul 22 2014 Dominic Cleal <dcleal@redhat.com> 0.38.0-1
- Rebase to excon 0.38.0 (dcleal@redhat.com)

* Wed Mar 19 2014 Dominic Cleal <dcleal@redhat.com> 0.32.1-1
- Rebase to excon 0.32.1 (dcleal@redhat.com)

* Tue Jan 07 2014 Dominic Cleal <dcleal@redhat.com> 0.31.0-1
- Rebase to excon 0.31.0 (dcleal@redhat.com)

* Wed Nov 06 2013 Dominic Cleal <dcleal@redhat.com> 0.28.0-1
- Rebase to excon 0.28.0 (dcleal@redhat.com)

* Tue Aug 13 2013 Dominic Cleal <dcleal@redhat.com> 0.25.3-2
- Don't use SCL prefixes on cacert.pem path (dcleal@redhat.com)

* Mon Jul 22 2013 Dominic Cleal <dcleal@redhat.com> 0.25.3-1
- Rebase to excon 0.25.3 (dcleal@redhat.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.23.0-2
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Tue Jun 11 2013 Dominic Cleal <dcleal@redhat.com> 0.23.0-1
- Rebase to excon 0.23.0 (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri May 03 2013 Ivan Necas <inecas@redhat.com> 0.20.1-1
- Update the version due to Foreman dependency (inecas@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 0.14.3-3
- disable tests (msuchy@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 0.14.3-2
- new package built with tito

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.3-1
- Update to Excon 0.14.3.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.1-1
- Update to Excon 0.14.1
- Removed no longer needed patch for downgrading dependencies.
- Remove newly bundled certificates and link to system ones.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-2
- Fixed the changelog.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-1
- Update to version 0.9.5
- Fixed the dependencies for the new version.

* Mon Dec 05 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.12-1
- Update to version 0.7.12.

* Mon Nov 28 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.8-1
- Update to version 0.7.8.
- Replaced defines with more appropriate globals.
- Added Build dependency on rubygem-eventmachine.
- Fixed running tests for the new version.

* Wed Oct 12 2011 bkabrda <bkabrda@redhat.com> - 0.7.6-1
- Update to version 0.7.6
- Introduced doc subpackage
- Introduced check section

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.6.3-1
- Initial package
