%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from ruby-libvirt-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-libvirt
%global rubyabi 1.9.1

Summary: Ruby bindings for LIBVIRT
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.2
Release: 1%{?dist}
Group: Development/Languages
License: LGPLv2+
URL: http://libvirt.org/ruby/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}rubygems-devel 
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: libvirt-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ruby bindings for libvirt.


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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# remove shebangs from test files
pushd %{buildroot}%{gem_instdir}/tests
find -type f -name '*.rb' -print | xargs sed -i '/#!\/usr\/bin\/ruby/d'
popd

mkdir -p %{buildroot}%{gem_extdir}/lib
mv %{buildroot}%{gem_instdir}/lib/_libvirt.so %{buildroot}%{gem_extdir}/lib/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

%check
pushd .%{gem_instdir}
# I disabled the tests because they modify system in possibly
# dangerous way and need to be run with root privileges
%{?scl:scl enable %{scl} "}
# testrb tests
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/COPYING
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/tests

%changelog
* Fri Dec 05 2014 Dominic Cleal <dcleal@redhat.com> 0.5.2-1
- Update ruby-libvirt to 0.5.2 (dcleal@redhat.com)

* Mon Dec 16 2013 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- Update to ruby-libvirt 0.5.1 (dcleal@redhat.com)

* Fri Oct 04 2013 Sam Kottler <shk@redhat.com> 0.4.0-9
- Remove requires: libvirt (shk@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.0-4
- fix BR (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.0-3
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.0-1
- Initial package
