%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name unf

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.3
Release: 3%{?dist}
Summary: Unicode normalization form support for Ruby/JRuby
Group: Development/Languages
License: MIT
URL: https://github.com/knu/ruby-unf
Source0: %{gem_name}-%{version}.gem
%if 0%{?fedora}
Requires: %{?scl_prefix}ruby(release)
Requires: %{?scl_prefix}ruby(rubygems)
%else
Requires: %{?scl_prefix}ruby(abi)
Requires: %{?scl_prefix}rubygems
%endif

Requires: %{?scl_prefix}rubygem(unf_ext)

BuildRequires: %{?scl_prefix}rubygems-devel
%if 0%{?fedora}
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi)
%endif
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires: %{?scl_prefix}rubygem(unf)

%description
A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby.

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
mkdir -p %{buildroot}%{gem_extdir}/lib

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/.gitignore
%doc %{gem_instdir}/.travis.yml
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Tue Nov 19 2013 Dominic Cleal <dcleal@redhat.com> 0.1.3-3
- Add dependency on unf_ext (dcleal@redhat.com)
- Fix project URL, typo (dcleal@redhat.com)

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.1.3-2
- new package built with tito

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> 0.1.3-1
- Initial creation of the package (shk@redhat.com)
