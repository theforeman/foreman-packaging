%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rr

%global rubyabi 1.9.1
  
%if 0%{?fedora} >= 17
  %global rubyabi 1.9.1
%endif

%if 0%{?fedora} >= 19
  %global rubyabi 2.0.0
%endif

Summary: RR (Double Ruby) is a test double framework 
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.5
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://pivotallabs.com
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: http://s3.amazonaws.com/rubygem-rr/tests/v%{version}.tar.gz

%if 0%{?fedora} >= 19
Requires:       %{?scl_prefix_ruby}ruby(release)
%endif

%if 0%{?fedora} >= 17 && 0%{?fedora} < 19
Requires:      %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif

%if 0%{?fedora} <= 17
Requires: %{?scl_prefix_ruby}ruby(rubygems) 
%endif

BuildRequires: %{?scl_prefix_ruby}ruby-irb
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

# The following are for running test suite
#BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
#BuildRequires: %{?scl_prefix}rubygem(session)
#BuildRequires: %{?scl_prefix_ruby}rubygem(diff-lcs)
#BuildRequires: %{?scl_prefix_ruby}rubygem(rspec)

%description
RR (Double Ruby) is a test double framework that features a rich selection of
double techniques and a terse syntax.

A Test Double is a generalization of something that replaces a real object to
make it easier to test another object. Its like a stunt double for tests.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n %{gem_name}-%{version}

# Modify the gemspec if necessary with a patch or sed
# Also apply patches to code if necessary
# %%patch0 -p1

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
# gem install compiles any C extensions and installs into a directory
# We set that to be a local directory so that we can move it into the
# buildroot in %%install

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --bindir ./%{_bindir} \
        --force \
        --rdoc \
        --ri \
        %{gem_name}-%{version}.gem
%{?scl:"}

%if 0%{?fedora} >= 19
%gem_install
%endif

tar -xvzf %{SOURCE1}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# Remove leftovers.
rm  %{buildroot}%{gem_instdir}/Rakefile

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/VERSION
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/VERSION
%{gem_spec}
%{gem_libdir}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec
#%%{gem_instdir}/benchmarks

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.0.5-3
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jun 14 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.5-2
- rubygem-rr scl changes

* Sun Apr 21 2013 Guillermo Gómez <guillermo.gomez@gmail.com> - 1.0.5-1
- Updated version 1.0.5
- Automated tests included 
- rubygem(rspec) included as a build require

* Sun Mar 24 2013 Guillermo Gómez <guillermo.gomez@gmail.com> - 1.0.4-7
- Removed unnecesary dependencies
- Fixes for Ruby 2.0.0 packaging

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-8
- F-19: Rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 1.0.4-6
- Removed unnecesary dependencies
- Spec adjusted according new guidelines

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 12 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 1.0.4-4
- Changelog entries fixed

* Tue Feb 07 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 1.0.4-3
- Updated spec file for Ruby 1.9 guidelines
- RSPec 1x tests disabled

* Tue Jan 24 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 1.0.4-2
- Removed unused macro from spec file
- Removed doc tag for benchmarks and spec file
- Removed cached version of the gem
- Fixed test suite files and test suite enabled at check section

* Sat Jan 21 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 1.0.4-1
- Initial package
