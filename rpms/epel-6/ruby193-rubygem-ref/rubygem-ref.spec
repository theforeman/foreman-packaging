%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from ref-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ref
%global rubyabi 1.9.1

Summary: Library that implements weak, soft, and strong references in Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/bdurand/ref
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Library that implements weak, soft, and strong references in Ruby that work
across multiple runtimes (MRI, REE, YARV, Jruby, Rubinius, and IronRuby). Also
includes implementation of maps/hashes that use references and a reference
queue.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
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

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
testrb test/*_test.rb
%{?scl:"}
popd


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/ext
%{gem_libdir}
%exclude %{gem_libdir}/org
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/VERSION
%{gem_instdir}/test
%exclude %{gem_instdir}/test/*.rbc

%changelog
* Fri Feb 22 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-4
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.0-3
- Rebuilt for SCL.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.0-1
- Initial package
