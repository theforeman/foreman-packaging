%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from net-ssh-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh

Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.2.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/net-ssh/net-ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release) >= 2
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(release) >= 2
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# file-not-utf8 correction
pushd %{buildroot}%{gem_instdir}
iconv --from=ISO-8859-1 --to=UTF-8 THANKS.txt > THANKS.txt.new && \
touch -r THANKS.txt THANKS.txt.new && \
mv THANKS.txt.new THANKS.txt
popd

# replace shebangs to prevent SCL packages depending on non-SCL Ruby
find %{buildroot}%{gem_instdir}/support/ -name *.rb -exec \
  sed -ri '1sX/usr/bin/rubyX/usr/bin/env rubyX' {} +

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/THANKS.txt
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/Gemfile*
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/support
# Required to run tests
%{gem_instdir}/net-ssh.gemspec
%{gem_instdir}/net-ssh-public_cert.pem
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/appveyor.yml
%exclude %{gem_instdir}/ISSUE_TEMPLATE.md

%changelog
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
