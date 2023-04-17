# template: default
%global gem_name pulp_ostree_client

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?dist}
Summary: Pulp 3 API Ruby Gem
License: GPL-2.0+
URL: https://github.com/pulp/pulp_ostree
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9
BuildRequires: ruby >= 1.9
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Fetch, Upload, Organize, and Distribute Software Packages.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%exclude %{gem_instdir}/pulp_ostree_client.gemspec
%{gem_instdir}/spec

%changelog
* Mon Apr 17 2023 Evgeni Golov 2.0.0-1
- Update to 2.0.0

* Tue Oct 05 2021 Justin Sherrill <jsherril@redhat.com> 2.0.0-0.1.a1
- initial build

