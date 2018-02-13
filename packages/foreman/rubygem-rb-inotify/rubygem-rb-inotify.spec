# Generated from rb-inotify-0.9.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rb-inotify

Name: rubygem-%{gem_name}
Version: 0.9.7
Release: 2%{?dist}
Summary: A Ruby wrapper for Linux's inotify, using FFI
Group: Development/Languages
License: MIT
URL: https://github.com/nex3/rb-inotify
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
%endif
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(ffi) >= 0.5.0
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%endif
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Ruby wrapper for Linux's inotify, using FFI.


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

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%doc %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rb-inotify.gemspec

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.9.7-2
- Add missing EL6 build information (ericdhelms@gmail.com)

* Fri Jul 29 2016 Dominic Cleal <dominic@cleal.org> 0.9.7-1
- new package built with tito

