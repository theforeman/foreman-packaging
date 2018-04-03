%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ovirt-engine-sdk

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.2.3
Release: 1%{?dist}
Summary: Ruby SDK for the oVirt Engine API.
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/oVirt/ovirt-engine-sdk-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9.2
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(json) >= 1.0
Requires: %{?scl_prefix_ruby}rubygem(json) < 3.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 1.9.2
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby SDK for the oVirt Engine API.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/ext
%{gem_extdir_mri}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.adoc
%doc %{gem_instdir}/CHANGES.adoc

%changelog
* Wed Apr 04 2018 Ivan Necas <inecas@redhat.com> 4.2.3-1
- new package
