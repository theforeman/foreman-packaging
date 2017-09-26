%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_snapshot_management
%global plugin_name snapshot_management

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?foremandist}%{?dist}
Summary: Snapshot Management for VMware vSphere
Group: Applications/Systems
License: GPL-3.0
URL: http://www.orcharhino.com
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: foreman >= 1.14.0
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: foreman-plugin >= 1.14
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}

%description
Foreman-plugin to manage snapshots in a vSphere environment.


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

%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_restart}
exit 0

%changelog
* Tue Aug 15 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-1
- new package built with tito

