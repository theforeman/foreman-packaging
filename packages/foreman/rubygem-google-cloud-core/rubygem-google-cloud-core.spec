# template: nonscl
%global gem_name google-cloud-core
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.6.0
Release: 1%{?dist}
Summary: Internal shared library for google-cloud-ruby
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/googleapis/google-cloud-ruby/tree/master/google-cloud-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby(release)
Requires: ruby >= 2.5
Requires: ruby(rubygems)
Requires: rubygem(google-cloud-env) >= 1.0
Requires: rubygem(google-cloud-env) < 2
Requires: rubygem(google-cloud-errors) >= 1.0
Requires: rubygem(google-cloud-errors) < 2
BuildRequires: ruby(release)
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
google-cloud-core is the internal shared library for google-cloud-ruby.


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
%{gem_instdir}/AUTHENTICATION.md
%{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
* Fri Apr 01 2022 Leos Stejskal <lstejska@redhat.com> 1.6.0-1
- Add rubygem-google-cloud-core generated by gem2rpm using the nonscl template

