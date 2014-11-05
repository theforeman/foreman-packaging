%global gem_name chef-api

Name: rubygem-%{gem_name}
Summary: A tiny Chef API client with minimal dependencies
Version: 0.5.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/sethvargo/chef-api
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(release)
BuildRequires: ruby(release)
Requires:      rubygem(logify) >= 0.1.0
Requires:      rubygem(logify) < 1.0.0
Requires:      rubygem(mime-types)
BuildRequires: rubygems-devel

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A tiny Chef API client with minimal dependencies

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/templates
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml

%files doc
%doc %{gem_docdir}
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile*

%changelog
* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- new package built with tito

