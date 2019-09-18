# template: nonscl
%global gem_name chef-api

Name: rubygem-%{gem_name}
Version: 0.9.0
Release: 1%{?dist}
Summary: A Chef API client in Ruby
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/sethvargo/chef-api
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby(release)
Requires: ruby >= 2.2
Requires: ruby(rubygems)
Requires: rubygem(logify) >= 0.1
Requires: rubygem(logify) < 1
Requires: rubygem(mime-types)
BuildRequires: ruby(release)
BuildRequires: ruby >= 2.2
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
A tiny Chef API client with minimal dependencies.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 0.9.0-1
- Update to 0.9.0-1

* Wed Jun 22 2016 Dominic Cleal <dominic@cleal.org> 0.6.0-1
- Update chef-api to 0.6.0 (dominic@cleal.org)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- new package built with tito

