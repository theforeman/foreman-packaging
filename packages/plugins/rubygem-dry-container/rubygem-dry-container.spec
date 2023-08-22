# template: default
%global gem_name dry-container

Name: rubygem-%{gem_name}
Version: 0.9.0
Release: 1%{?dist}
Summary: A simple, configurable object container implemented in Ruby
License: MIT
URL: https://dry-rb.org/gems/dry-container
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6.0
BuildRequires: ruby >= 2.6.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A simple, configurable object container implemented in Ruby.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/dry-container.gemspec

%changelog
* Tue Aug 22 2023 Dirk Goetz <dirk.goetz@netways.de> 0.9.0-1
- Update to 0.9.0

* Tue May 31 2022 Dirk Goetz <dirk.goetz@netways.de> 0.7.2-1
- Add rubygem-dry-container generated by gem2rpm using the scl template

