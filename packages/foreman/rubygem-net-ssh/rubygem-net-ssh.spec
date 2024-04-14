# template: default
%global gem_name net-ssh

Name: rubygem-%{gem_name}
Version: 7.2.3
Release: 1%{?dist}
Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
License: MIT
URL: https://github.com/net-ssh/net-ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows
you to write programs that invoke and interact with processes on remote
servers, via SSH2.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

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

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.dockerignore
%exclude %{gem_instdir}/Dockerfile*
%exclude %{gem_instdir}/docker-compose.yml
%doc %{gem_instdir}/CHANGES.txt
%exclude %{gem_instdir}/ISSUE_TEMPLATE.md
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/Manifest
%exclude %{gem_instdir}/appveyor.yml
%{gem_libdir}
%exclude %{gem_instdir}/net-ssh-public_cert.pem
%exclude %{gem_instdir}/support
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.noed25519
%{gem_instdir}/Gemfile.norbnacl
%doc %{gem_instdir}/DEVELOPMENT.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%doc %{gem_instdir}/THANKS.txt
%exclude %{gem_instdir}/net-ssh.gemspec

%changelog
* Sun Apr 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 7.2.3-1
- Update to 7.2.3

* Tue Jan 02 2024 Foreman Packaging Automation <packaging@theforeman.org> 7.2.1-1
- Update to 7.2.1

* Sun Aug 20 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.2.0-1
- Update to 7.2.0

* Sun Mar 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.1.0-1
- Update to 7.1.0

* Sun Oct 23 2022 Foreman Packaging Automation <packaging@theforeman.org> 7.0.1-1
- Update to 7.0.1

* Thu Aug 25 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.1.0-1
- Update to 6.1.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.2.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.2.0-2
- Bump to release for EL8

* Mon Mar 18 2019 Marek Hulan <mhulan@redhat.com> 4.2.0-1
- Update to 4.2.0

* Thu Feb 28 2019 Evgeni Golov - 4.0.1-6
- Also build rubygem-net-ssh for non-SCL

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.0.1-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Sat Jan 06 2018 Eric D. Helms <ericdhelms@gmail.com> 4.0.1-4
- Fixes needed for repoclosure (ericdhelms@gmail.com)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.0.1-3
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jul 12 2017 Eric D. Helms <ericdhelms@gmail.com> 4.0.1-2
- Fixes #20018 - Bump release version (aruzicka@redhat.com)
- Fixes #20018 - Backport ProxyCommand patch for net-ssh (aruzicka@redhat.com)

* Thu Feb 09 2017 Dominic Cleal <dominic@cleal.org> 4.0.1-1
- Update net-ssh to 4.0.1 (dominic@cleal.org)
- Modernise spec file (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 3.0.2-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Wed Jan 20 2016 Dominic Cleal <dcleal@redhat.com> 3.0.2-1
- Update net-ssh to 3.0.2 (dcleal@redhat.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.9.2-3
- Replace shebangs to remove deps on non-SCL Ruby (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.9.2-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Sep 30 2015 Dominic Cleal <dcleal@redhat.com> 2.9.2-1
- Update net-ssh to 2.9.2 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.6.7-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri May 03 2013 Ivan Necas <inecas@redhat.com> 2.6.7-1
- Update due to new fog dependency (inecas@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 2.2.1-5
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.2.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Shreyank Gupta <sgupta@redhat.com> - 2.2.1-1
- Updated to version 2.2.1-1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 2.0.23-5
- rebuild to ensure F14 has higher NVR than F13

* Fri Jun 11 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-4
- Bring back the BR: rubygem(rake) and rake test

* Thu Jun 10 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-3
- test command from test/README.txt
- Remove gem "test-unit" line
- Removed Requires rubygem(rake)
- BuildRequires/Requires: rubygem(mocha) for tests

* Thu Jun 10 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-2
- Using %%exclude for setup.rb
- Keeping net-ssh.gemspec for tests
- Moved file-not-utf8 correction to before %%check section

* Wed Jun 09 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-1
- Initial package
