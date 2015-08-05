%if 0%{?rhel} == 6
%{!?gem_extdir_mri:%global gem_extdir_mri %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}
%global gem_extdir_mri_lib %{gem_extdir_mri}
%else
%{!?gem_extdir_mri:%global gem_extdir_mri %{gem_extdir}}
%global gem_extdir_mri_lib %{gem_extdir_mri}/lib
%endif
%global gem_name newt

Summary: Ruby bindings for newt
Name: rubygem-%{gem_name}

Version: 0.9.5
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/theforeman/ruby-newt
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby
Requires: rubygems
Requires: newt

BuildRequires: ruby
BuildRequires: rubygems
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: newt-devel

Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby bindings for the newt TUI library allows creation of rich
user text-based experience in Ruby language.

%package doc
BuildArch:  noarch
Requires:   rubygem-%{gem_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
find .%{gem_dir}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri_lib}/ruby_newt
mv %{buildroot}%{gem_instdir}/lib/ruby_newt/ruby_newt.so %{buildroot}%{gem_extdir_mri_lib}/ruby_newt/ruby_newt.so
rm -rf %{buildroot}%{gem_instdir}/{ext,tmp,.require_paths}

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc

%changelog
* Tue Aug 04 2015 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.5-1
- bumped version

* Tue Jun 30 2015 Dominic Cleal <dcleal@redhat.com> 0.9.4-1
- new package built with tito

