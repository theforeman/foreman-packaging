%global gem_name radcli

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: A Ruby interface for the adcli library
Group: Development/Languages
License: Artistic-2.0
URL: https://github.com/martencassel/radcli
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: cyrus-sasl-devel
Provides: rubygem(%{gem_name}) = %{version}

%description
The radcli library provides a Ruby interface for performing actions on
a Active Directory domain using the realmd/adcli tool library.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/lib
cp -a %{buildroot}%{gem_instdir}/lib/radcli.so %{buildroot}%{gem_extdir_mri}/lib/

# rake-compiler isn't needed on the system itself
sed -i '/rake-compiler/ s/runtime/development/' %{buildroot}/%{gem_spec}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_instdir}/CHANGES
%license %{gem_instdir}/LICENSE
%{gem_instdir}/MANIFEST
%{gem_instdir}/build_adcli.sh
%exclude %{gem_instdir}/radcli.gemspec
%{gem_instdir}/scripts
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Jan 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-1
- new package built with tito

