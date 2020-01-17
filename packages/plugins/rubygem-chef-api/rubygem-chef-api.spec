# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name chef-api

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.0
Release: 4%{?dist}
Summary: A Chef API client in Ruby
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/sethvargo/chef-api
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(logify) >= 0.1
Requires: %{?scl_prefix}rubygem(logify) < 1
Requires: %{?scl_prefix}rubygem(mime-types)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
A tiny Chef API client with minimal dependencies.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/templates
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/chef-api.gemspec
%{gem_instdir}/spec

%changelog
* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.6.0-4
- Update spec to remove the ror scl

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.6.0-3
- Build for SCL

* Tue Oct 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.6.0-2
- Update for SCL building

* Wed Jun 22 2016 Dominic Cleal <dominic@cleal.org> 0.6.0-1
- Update chef-api to 0.6.0 (dominic@cleal.org)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- new package built with tito
