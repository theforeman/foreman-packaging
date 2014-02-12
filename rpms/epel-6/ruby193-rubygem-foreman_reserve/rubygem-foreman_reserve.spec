# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_reserve

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Reserve hosts via Foreman API
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.1.8.2
Release:    2%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_reserve
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.4.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-hooks

%description
Plugin engine for Foreman that allows reservation of hosts via the API.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

rm -f *gemspec

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
# the following two will be removed soon hopefully:
# https://github.com/david-caro/foreman_reserve/pull/2
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/VERSION
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb

%exclude %{gem_instdir}/test
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile*
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Feb 12 2014 Lukas Zapletal <lzap+git@redhat.com> 0.1.8.2-2
- new package built with tito

* Wed Feb 12 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.8.2-1
- Initial version
