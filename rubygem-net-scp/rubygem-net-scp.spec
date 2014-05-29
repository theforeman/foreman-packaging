%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name net-scp
%global rubyabi 1.9.1

Summary: A pure Ruby implementation of the SCP client protocol
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://net-ssh.rubyforge.org/scp
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(net-ssh)
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix}rubygem(mocha)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A pure Ruby implementation of the SCP client protocol


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep

%build

%install
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

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
%doc %{gem_instdir}/README.rdoc
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/net-scp.gemspec
%{gem_instdir}/setup.rb
%doc %{gem_instdir}/CHANGES.txt
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/test
%{gem_instdir}/gem-public_cert.pem
%doc %{gem_docdir}

%changelog
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
