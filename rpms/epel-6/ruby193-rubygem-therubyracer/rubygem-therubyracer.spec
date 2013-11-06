%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name therubyracer
%global rubyabi 1.9.1

%global majorver 0.11.0
%global preminorver beta5
%global fullver %{majorver}%{?preminorver}

%{?preminorver:%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{fullver}}
%{?preminorver:%global gem_extdir %{_libdir}/gems/exts/%{gem_name}-%{fullver}}
%{?preminorver:%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{fullver}}
%{?preminorver:%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{fullver}.gemspec}
%{?preminorver:%global gem_cache %{gem_dir}/cache/%{gem_name}-%{fullver}.gem}

Summary: Embed the V8 Javascript interpreter into Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: %{majorver}
Release: %{?preminorver:0.}14%{?preminorver:.%{preminorver}}%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/cowboyd/therubyracer
Source0: http://rubygems.org/gems/%{gem_name}-%{version}%{?preminorver}.gem
%if 0%{?fedora}
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygem(ref)
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}v8
%if 0%{?fedora}
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygem(ref)
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}v8-devel
# some specs run "ps aux"
BuildRequires: procps
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Call javascript code and manipulate javascript objects from ruby. Call ruby
code and manipulate ruby objects from javascript.


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

mkdir -p %{buildroot}%{gem_extdir}/lib/v8
mv %{buildroot}%{gem_instdir}/lib/v8/init.so %{buildroot}%{gem_extdir}/lib/v8

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

# remove shebang in non-executable file
sed -i '1d' %{buildroot}%{gem_instdir}/Rakefile

%check
pushd .%{gem_instdir}
# this spec doesn't test anything, only requires redjs, which is not in fedora
mv spec/redjs_spec.rb spec/redjs_spec.rb.notest

# fix the v8 version we're testing against
%{?scl:scl enable %scl - << \EOF}
V8_VERSION=`d8 -e "print(version())"`
%{?scl:EOF}
sed -i "s|V8::C::V8::GetVersion().*|V8::C::V8::GetVersion().should match /^${V8_VERSION}/|" spec/c/constants_spec.rb

%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/benchmarks.rb
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/thefrontside.png
%{gem_instdir}/therubyracer.gemspec

%changelog
* Tue Nov 05 2013 Sam Kottler <shk@redhat.com> 0.11.0-0.14.beta5
- Bump the version manually again (shk@redhat.com)
- Use ruby(release) if on fedora (shk@redhat.com)

* Tue Nov 05 2013 Sam Kottler <shk@redhat.com>
- Use ruby(release) if on fedora (shk@redhat.com)

* Tue Nov 05 2013 Sam Kottler <shk@redhat.com> 0.11.0-0.13.beta5
- Remove errant changelog entries (shk@redhat.com)
- Manually bump the release to tagging will work (shk@redhat.com)
- Revert therubyracer to the last known working state (shk@redhat.com)

* Sat Feb 23 2013 Miroslav Suchý <msuchy@redhat.com> 0.11.0-0.4.beta5
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11.0-0.4.beta5
- Rebuilt for SCL.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-0.3.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11.0-0.2.beta5
- Fixed minor issues according to review comments (RHBZ #838870).

* Fri Jun 15 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11.0-0.1.beta5
- Initial package
