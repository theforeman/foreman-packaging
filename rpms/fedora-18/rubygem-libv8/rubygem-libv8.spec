%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name libv8

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache
%global gem_spec %{gem_dir}/specifications
%endif

%global _python_bytecompile_errors_terminate_build %{nil}

Summary: Distribution of the V8 JavaScript engine
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.16.14.3
Release: 8%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/cowboyd/libv8
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} && 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby
BuildRequires: python-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Distributes the V8 JavaScript engine in binary and source forms in order to
support fast builds of The Ruby Racer

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%package testsuite
Summary:        Test suite for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{?scl_prefix}%{pkg_name} = %{version}

%description testsuite
Test::Unit or RSpec files, useful for developers.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force %{SOURCE0} \
%{?scl:"}



%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

sed -i '1d' %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/vendor/gyp/test/mac/postbuild-fail/postbuild-fail.sh

mkdir -p %{buildroot}%{gem_extdir}/lib
# TODO: move the extensions
##mv %{buildroot}%{gem_instdir}/lib/shared_object.so %{buildroot}%{gem_extdir}/lib/
# Remove the binary extension sources and build leftovers.
#rm -rf %{buildroot}%{geminstdir}/ext

rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/{.yardoc,.gitignore,.gitmodules,.travis.yml}

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/patches
%{gem_instdir}/vendor
%{gem_extdir}
%exclude %{gem_cache}
%{gem_instdir}/ext
%{gem_spec}
%doc %{gem_instdir}/README.md
%{gem_instdir}/thefrontside.png

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%files testsuite
%{gem_instdir}/spec

%changelog
* Thu Oct 24 2013 Sam Kottler <shk@redhat.com> 3.16.14.3-8
- Use the real gem directory (shk@redhat.com)

* Thu Oct 24 2013 Sam Kottler <shk@redhat.com> 3.16.14.3-7
- Remove statement again (why did it even come back?) (shk@redhat.com)
- Fix location of sed statement (shk@redhat.com)

* Thu Oct 24 2013 Sam Kottler <shk@redhat.com>
- Remove statement again (why did it even come back?) (shk@redhat.com)
- Fix location of sed statement (shk@redhat.com)

* Wed Oct 23 2013 Sam Kottler <shk@redhat.com> 3.16.14.3-5
- Ensure the patches directory gets included in the build (shk@redhat.com)

* Wed Oct 23 2013 Sam Kottler <shk@redhat.com> 3.16.14.3-4
- Bump the gem to fix compilation on F19 (shk@redhat.com)

* Wed Oct 23 2013 Sam Kottler <shk@redhat.com> 3.16.14.0-3
- Update the libv8 gem to support building with SCL (shk@redhat.com)

* Wed Oct 23 2013 Sam Kottler <shk@redhat.com> 3.16.14.0-2
- Remove the patches directory (shk@redhat.com)
- Add new libv8 gem (shk@redhat.com)
- Bumped the version of libv8 (shk@redhat.com)

* Wed Nov 21 2012 Miroslav Suchý <msuchy@redhat.com> 3.11.8.3-4
- define gem_instdir macro (msuchy@redhat.com)

* Wed Nov 21 2012 Miroslav Suchý <msuchy@redhat.com> 3.11.8.3-3
- add ruby-devel to BR (msuchy@redhat.com)

* Wed Nov 21 2012 Miroslav Suchý <msuchy@redhat.com> 3.11.8.3-2
- new package built with tito

* Wed Nov 21 2012 Miroslav Suchý <msuchy@redhat.com> - 3.11.8.3-1
- Initial package
