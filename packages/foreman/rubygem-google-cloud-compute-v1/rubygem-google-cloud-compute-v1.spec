# template: default
%global gem_name google-cloud-compute-v1

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 1%{?dist}
Summary: API Client library for the Google Cloud Compute V1 API
License: Apache-2.0
URL: https://github.com/googleapis/google-cloud-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
google-cloud-compute-v1 is the official client library for the Google Cloud
Compute V1 API.


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
%exclude %{gem_instdir}/.yardopts
%{gem_instdir}/AUTHENTICATION.md
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/proto_docs

%changelog
* Mon Jul 18 2022 Leos Stejskal <lstejska@redhat.com> 1.4.0-1
- Add rubygem-google-cloud-compute-v1 generated by gem2rpm using the default template

