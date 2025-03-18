# template: default
%global gem_name excon

Name: rubygem-%{gem_name}
Version: 1.2.5
Release: 1%{?dist}
Summary: speed, persistence, http(s)
License: MIT
URL: https://github.com/excon/excon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7.0
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

Requires: (rubygem(logger) or ruby-default-gems < 3.5)

Requires: ca-certificates

%description
EXtended http(s) CONnections.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g logger

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# kill bundled cacert.pem
ln -sf /etc/pki/tls/cert.pem \
	%{buildroot}%{gem_instdir}/data/cacert.pem

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/excon.gemspec

%changelog
* Tue Mar 18 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.5-1
- Update to 1.2.5

* Wed Oct 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.112.0-1
- Update to 0.112.0

* Thu Jul 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.111.0-1
- Update to 0.111.0

* Tue Apr 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.110.0-1
- Update to 0.110.0

* Fri Jan 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.109.0-1
- Update to 0.109.0

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.105.0-1
- Update to 0.105.0

* Sun Nov 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.104.0-1
- Update to 0.104.0

* Sun Oct 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.103.0-1
- Update to 0.103.0

* Sun Aug 27 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.102.0-1
- Update to 0.102.0

* Thu Jun 29 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.100.0-1
- Update to 0.100.0

* Tue Feb 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.99.0-1
- Update to 0.99.0

* Mon Jan 23 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.97.2-1
- Update to 0.97.2

* Sun Jan 15 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.97.0-1
- Update to 0.97.0

* Wed Jan 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.95.0-1
- Update to 0.95.0

* Thu Nov 10 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.94.0-1
- Update to 0.94.0

* Tue Oct 25 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.93.1-1
- Update to 0.93.1

* Sun Jul 31 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.92.4-1
- Update to 0.92.4

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.92.3-1
- Update to 0.92.3

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
