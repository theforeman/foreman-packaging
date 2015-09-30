%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from net-ssh-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh

%global rubyabi 1.9.1

Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.9.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/net-ssh/net-ssh
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ruby}rubygem(mocha)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix_ruby}rubygem(mocha)
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

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

# remove gem "test-unit" line
sed -i -e '/test-unit/, 1d' %{buildroot}%{gem_instdir}/test/common.rb

%check

pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %{scl} "}
# requires newer version of mocha (>= 0.13.3)
# ruby -Ilib -Itest test/test_all.rb
%{?scl:"}
popd


%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/support
%exclude %{gem_instdir}/setup.rb
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/THANKS.txt
%doc %{gem_instdir}/CHANGES.txt
%doc %{gem_instdir}/LICENSE.txt
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%{gem_docdir}
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/Rudyfile
%{gem_instdir}/test
# Required to run tests
%{gem_instdir}/net-ssh.gemspec
%{gem_instdir}/net-ssh-public_cert.pem
%exclude %{gem_instdir}/.*

%changelog
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
