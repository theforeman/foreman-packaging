# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name bastion

%define rubyabi 1.9.1

Summary:    UI plugin for Foreman providing AngularJS structure
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.3.1
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv2+
URL:        http://github.com/katello/bastion
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires: foreman >= 1.8.0
Requires: %{?scl_prefix}rubygem(angular-rails-templates) = 0.1.2

BuildRequires: foreman-assets >= 1.8.0
BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygem(less-rails) >= 2.5.0
BuildRequires: %{?scl_prefix}rubygem(less-rails) < 2.6
BuildRequires: %{?scl_prefix}rubygem(angular-rails-templates) = 0.1.2


%description
Bastion serves as a plugin to Foreman that provides common
elements for an AngularJS based UI component for a feature.
The structure, common elements, and development tasks serve as
a basis for any plugin to quickly scaffold and create a UI that
takes advantage of the Foreman (or Foreman plugin) API to create
a modern UI.

%package doc
Summary:    Documentation for rubygem-%{gem_name}
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%package devel
Summary:   Provides asset compilation dependencies for %{scl_prefix}rubygem-%{gem_name}
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires:  %{?scl_prefix}rubygem(less-rails) >= 2.5.0
Requires:  %{?scl_prefix}rubygem(less-rails) < 2.6
Requires:  %{?scl_prefix}rubygem(uglifier)

%description devel
This package contains assets compilation dependencies for %{scl_prefix}rubygem-%{gem_name}.

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

cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/bastion.rb
gem 'bastion'
gem 'less-rails'
GEMFILE

%foreman_precompile_plugin -r bastion:assets:precompile -s
%foreman_bundlerd_file

mkdir -p %{buildroot}%{foreman_dir}/public/assets
ln -s %{foreman_assets_plugin} %{buildroot}%{foreman_dir}/public/assets/bastion

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/vendor
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_dir}/public/assets/bastion
%{foreman_assets_plugin}
%{gem_instdir}/LICENSE
%{gem_instdir}/Rakefile

%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/.jshintrc
%exclude %{gem_instdir}/grunt
%exclude %{gem_instdir}/bastion.js
%exclude %{gem_instdir}/Gruntfile.js
%exclude %{gem_instdir}/bower.json
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/eslint.yaml
%exclude %{gem_dir}/cache

%files doc
%doc %{gem_instdir}/README.md

%files devel

%changelog
* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.3.0-1
- Update rubygem-bastion to 0.3.0 (ericdhelms@gmail.com)

* Wed Mar 04 2015 Dominic Cleal <dcleal@redhat.com> 0.2.9-1
- Update package rubygem-bastion to 0.2.9 (ericdhelms@gmail.com)

* Fri Feb 27 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.8-1
- Update rubygem-bastion to 0.2.8 (ericdhelms@gmail.com)

* Tue Feb 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.7-1
- Update package rubygem-bastion to 0.2.7 (ericdhelms@gmail.com)

* Mon Feb 23 2015 Dominic Cleal <dcleal@redhat.com> 0.2.6-2
- Default options in foreman_precompile_plugin changed (rubygem-bastion)
  (martin.bacovsky@gmail.com)

* Wed Feb 18 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.6-1
- Update rubygem-bastion to 0.2.6 (ericdhelms@gmail.com)

* Thu Feb 12 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.5-1
- Update rubygem-bastion to 0.2.5 (ericdhelms@gmail.com)

* Mon Feb 09 2015 Eric D. Helms <ericdhelms@gmail.com> 0.2.2-1
- Remove angular-rails-templates version dependency on rubygem-bastion
  (ericdhelms@gmail.com)

* Tue Feb 03 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update bastion to 0.2.0 (ericdhelms@gmail.com)

* Tue Jan 13 2015 Dominic Cleal <dcleal@redhat.com> 0.1.13-1
- Update rubygem-bastion to 0.1.13 (ericdhelms@gmail.com)

* Tue Dec 09 2014 Eric D. Helms <ericdhelms@gmail.com> 0.1.12-1
- Update rubygem-bastion to 0.1.12 (ericdhelms@gmail.com)

* Mon Dec 01 2014 Eric D. Helms <ericdhelms@gmail.com> 0.1.10-1
- Update rubygem-bastion to 0.1.10 (ericdhelms@gmail.com)

* Tue Nov 18 2014 Dominic Cleal <dcleal@redhat.com> 0.1.9-1
- Update 'rubygem-bastion' to 0.1.9 (ericdhelms@gmail.com)

* Wed Nov 12 2014 Dominic Cleal <dcleal@redhat.com> 0.1.8-1
- Update 'rubygem-bastion' to 0.1.8 (ericdhelms@gmail.com)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.1.7-2
- Convert bastion to use asset precompilation RPM macros (dcleal@redhat.com)

* Tue Oct 28 2014 Dominic Cleal <dcleal@redhat.com> 0.1.7-1
- Update rubygem-bastion to 0.1.7 (ericdhelms@gmail.com)

* Wed Oct 22 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update bastion to 0.1.5 (dcleal@redhat.com)

* Tue Oct 21 2014 Dominic Cleal <dcleal@redhat.com> 0.1.4-1
- Update 'rubygem-bastion' 0.1.4 (ericdhelms@gmail.com)

* Fri Oct 17 2014 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- new package built with tito (ericdhelms@gmail.com)


