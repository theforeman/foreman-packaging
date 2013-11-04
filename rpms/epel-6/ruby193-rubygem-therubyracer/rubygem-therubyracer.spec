%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name therubyracer
%global rubyabi 1.9.1

%global majorver 0.12.0
%global fullver %{majorver}

%{?preminorver:%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{fullver}}
%{?preminorver:%global gem_extdir %{_libdir}/gems/exts/%{gem_name}-%{fullver}}
%{?preminorver:%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{fullver}}
%{?preminorver:%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{fullver}.gemspec}
%{?preminorver:%global gem_cache %{gem_dir}/cache/%{gem_name}-%{fullver}.gem}

Summary: Embed the V8 Javascript interpreter into Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.12.0
Release: 13%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/cowboyd/therubyracer
Source0: http://rubygems.org/gems/%{gem_name}-%{version}%{?preminorver}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}rubygem(ref)
Requires: %{?scl_prefix}rubygem(libv8)
Requires: %{?scl_prefix}v8
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
%if 0%{?fedora}
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygem(ref)
BuildRequires: %{?scl_prefix}rubygem(libv8)
BuildRequires: %{?scl_prefix}v8-devel
BuildRequires: %{?scl_prefix}rubygem(rspec)
%if 0%{?fedora} || "%{?scl}" == "ruby193"
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
BuildRequires: %{?scl_prefix}ruby-devel
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
            --force %{SOURCE0} \
            -- --with-system-v8 --with-v8-dir=%{_scl_root}%{_usr}
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
* Mon Nov 04 2013 Sam Kottler <shk@redhat.com> 0.12.0-13
- Only use ruby-release on Fedora (shk@redhat.com)

* Mon Nov 04 2013 Sam Kottler <shk@redhat.com> 0.12.0-12
- Fix conditional logic (shk@redhat.com)

* Mon Nov 04 2013 Sam Kottler <shk@redhat.com> 0.12.0-11
- Fix the abi and release versions (shk@redhat.com)

* Mon Nov 04 2013 Sam Kottler <shk@redhat.com> 0.12.0-10
- Disable tests for now (shk@redhat.com)

* Mon Nov 04 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.0-9
- Adding system v8 library into requires (lzap+git@redhat.com)

* Mon Nov 04 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.0-8
- Adding --with-v8-dir option (lzap+git@redhat.com)

* Fri Nov 01 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.0-7
- Removing libv8 removal patch, adding rubygem libv8 as a dep

* Fri Nov 01 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.0-6
- Removing rubygem-libv8 dependency (lzap+git@redhat.com)

* Fri Nov 01 2013 Lukas Zapletal <lzap+git@redhat.com>
- Removing rubygem-libv8 dependency (lzap+git@redhat.com)

* Fri Nov 01 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.0-4
- Bumping because of existing tag (lzap+git@redhat.com)
- Remove the libv8 gem after initial compilation so execjs - fix
  (lzap+git@redhat.com)

* Thu Oct 31 2013 Sam Kottler <shk@redhat.com> 0.12.0-2
- new package built with tito

* Thu Oct 31 2013 Sam Kottler <shk@redhat.com>
- Remove the libv8 gem after initial compilation so execjs will load it
  properly (shk@redhat.com)

* Thu Oct 24 2013 Sam Kottler <shk@redhat.com> 0.12.0-1
- Remove version check which relies on d8 (shk@redhat.com)
- Update to 0.12.0 (shk@redhat.com)
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

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
