%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name unf_ext

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache
%global gem_spec %{gem_dir}/specifications
%endif

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.6
Release: 4%{?dist}
Summary: Unicode Normalization Form support library for CRuby
Group: Development/Languages
License: MIT
URL: https://github.com/knu/ruby-unf_ext
Source0: %{gem_name}-%{version}.gem
%if 0%{?fedora}
Requires: %{?scl_prefix}ruby(release)
Requires: %{?scl_prefix}ruby(rubygems)
%else
Requires: %{?scl_prefix}ruby(abi)
Requires: %{?scl_prefix}rubygems
%endif

%if (0%{?fedora} || "%{?scl}" == "ruby193")
BuildRequires: %{?scl_prefix}rubygems-devel
%endif

%if 0%{?fedora}
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequireS: %{?scl_prefix}ruby(abi)
%endif
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Unicode Normalization Form support library for CRuby

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}


%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}/%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir_mri}/lib

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_instdir}/ext
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/.gitignore
%doc %{gem_instdir}/.document

%changelog
* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.0.6-4
- Actually fix the rubygems-devel issue (shk@redhat.com)

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.0.6-3
- Make sure rubygems-devel is required during build for SCL (shk@redhat.com)

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.0.6-2
- Initial build with support for SCL

* Tue Nov 12 2013 Sam Kottler <skottler@redhat.com> - 0.0.6-1
- Initial package
