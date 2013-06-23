%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from hike-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hike

%global rubyabi 1.9.1

Summary: Find files in a set of paths
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.1
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/sstephenson/hike
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sstephenson/hike.git && cd hike && git checkout v1.2.1
# tar czvf hike-1.2.1-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Ruby library for finding files in a set of paths.


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
tar xzf %{SOURCE1}
%{?scl:scl enable %scl "}
testrb -Ilib test
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
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.1-4
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-3
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-2
- Rebuilt for scl.

* Mon Jan 30 2012 Vít Ondruch <vondruch@redhat.com> - 1.2.1-1
- Update to Hike 1.2.1.

* Wed Jun 29 2011 Vít Ondruch <vondruch@redhat.com> - 1.1.0-1
- Initial package
