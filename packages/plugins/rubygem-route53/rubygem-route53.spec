# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name route53

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 5%{?dist}
Summary: Library for Amazon's Route 53 service
Group: Development/Languages
License: GPLv3
URL: https://github.com/pcorliss/ruby_route_53
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.5
Requires: %{?scl_prefix}rubygem(ruby-hmac)
Requires: %{?scl_prefix}rubygem(nokogiri)
Requires: %{?scl_prefix}rubygem(builder)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.5
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Provides CRUD and list operations for records and zones as part of Amazon's
Route 53 service.


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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/route53
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.ruby-gemset
%exclude %{gem_instdir}/.ruby-version
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/route53.gemspec
%{gem_instdir}/spec

%changelog
* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.4.0-5
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.0-4
- Update spec to remove the ror scl

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.4.0-3
- Build for SCL

* Tue Oct 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.4.0-2
- Update for SCL building

* Thu Feb 02 2017 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- Update route53 to 0.4.0 (dominic@cleal.org)

* Wed Jun 15 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-1
- new package built with tito
