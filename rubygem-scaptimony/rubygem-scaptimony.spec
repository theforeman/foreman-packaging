# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name scaptimony

%define rubyabi 1.9.1

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.2
Release: 2%{?dist}
Summary: SCAPtimony is SCAP database and storage server
Group: Applications/System
License: GPLv3
URL: https://github.com/OpenSCAP/scaptimony
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(openscap) >= 0.4.1
Requires: %{?scl_prefix_ruby}rubygem(rails) >= 3.2.8
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem-openscap >= 0.4.1
Requires: %{?scl_prefix_ruby}rubygem-rails >= 3.2.8
Requires: %{?scl_prefix_ruby}rubygem-rails < 1:3.3.0
BuildRequires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
SCAPtimony is SCAP storage and database server build on top
of OpenSCAP library. SCAPtimony can be deployed as a part of
your Rails application (i.e. Foreman) or as a stand-alone
sealed server.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/COPYING

%exclude %{gem_instdir}/test

%files doc
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile


%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.3.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 21 2015 Dominic Cleal <dcleal@redhat.com> 0.3.2-1
- Update scaptimony to 0.3.2 (dcleal@redhat.com)

* Mon Mar 02 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.1-1
- new upstream release

* Mon Jan 26 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-1
- Update scaptimony to 0.3.0 (dcleal@redhat.com)

* Fri Jan 23 2015 Marek Hulan <mhulan@redhat.com> 0.2.0-2
- new package built based on upstream spec

* Thu Dec 04 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-1
- new upstream release

* Thu Oct 23 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- rebuilt

* Sun Oct 05 2014 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-1
- Initial package
- rebuilt
