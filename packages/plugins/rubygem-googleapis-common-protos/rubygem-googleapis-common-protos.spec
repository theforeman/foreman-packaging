# template: default
%global gem_name googleapis-common-protos

Name: rubygem-%{gem_name}
Version: 1.3.12
Release: 1%{?dist}
Summary: Common gRPC and protocol buffer classes used in Google APIs
License: Apache-2.0
URL: https://github.com/googleapis/common-protos-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Common gRPC and protocol buffer classes used in Google APIs.


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
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Fri Sep 30 2022 Eric D. Helms <ericdhelms@gmail.com> 1.3.12-1
- Add rubygem-googleapis-common-protos generated by gem2rpm using the default template

