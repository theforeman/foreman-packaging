%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from uuidtools-2.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name uuidtools

%global rubyabi 1.9.1

Summary: A simple universally unique ID generation library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.3
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://uuidtools.rubyforge.org/
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}rubygem(rspec-core)
BuildRequires: %{?scl_prefix_ruby}rubygem(rspec-mocks)
BuildRequires: %{?scl_prefix_ruby}rubygem(rspec-expectations)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
UUIDTools was designed to be a simple library for generating any of the various
types of UUIDs.  It conforms to RFC 4122 whenever possible.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%clean
rm -rf %{buildroot}

%check
pushd .%{gem_instdir}
# Can't run during check as it calls ifconfig
echo 'UUIDTools::UUID.mac_address = "00:1f:c6:62:3d:15"' >> spec/spec_helper.rb
%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
popd

%files
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/tasks
%{gem_instdir}/website
%{gem_instdir}/spec
%{gem_docdir}

%changelog
* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 2.1.3-3
- new package built with tito

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 2.1.3-1
- Updated to uuidtools 2.1.3.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.2-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.2-1
- Updated to uuidtools 2.1.2.

* Thu Dec 15 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.1-4
- Use RSpec 2.x instead of RSpec 1.x.

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 2.1.1-3
- Initial package

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 16 2010 Matthew Kent <mkent@magoazul.com> - 2.1.1-1
- Initial package
