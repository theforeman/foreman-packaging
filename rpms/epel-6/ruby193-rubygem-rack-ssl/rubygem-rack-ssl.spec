%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from rack-ssl-1.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rack-ssl

%global rubyabi 1.9.1

Summary: Force SSL/TLS in your app
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.2
Release: 8%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/josh/rack-ssl
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/josh/rack-ssl.git && cd rack-ssl && git checkout v1.3.2
# tar czvf rack-ssl-1.3.2-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(rack)
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(rack)
BuildRequires: %{?scl_prefix}rubygem(rack-test)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Rack middleware to force SSL/TLS.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}
%{?scl:scl enable %scl "}
testrb -Ilib test/
%{?scl:"}
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}


%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.2-8
- new package built with tito

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.2-7
- Exclude the cached gem.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.2-6
- Specfile cleanup

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.2-5
- Rebuilt for scl.

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.2-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.2-2
- Fixed license.
- Simplified test suite execution.

* Fri Jul 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.2-1
- Initial package
