# template: default
%global gem_name request_store

Name: rubygem-%{gem_name}
Version: 1.6.0
Release: 1%{?dist}
Summary: RequestStore gives you per-request global storage
License: MIT
URL: https://github.com/steveklabnik/request_store
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
RequestStore gives you per-request global storage.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.github
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/request_store.gemspec
%{gem_instdir}/test

%changelog
* Wed Feb 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.6.0-1
- Update to 1.6.0

* Thu May 11 2023 Evgeni Golov 1.5.1-1
- Add rubygem-request_store generated by gem2rpm using the default template

