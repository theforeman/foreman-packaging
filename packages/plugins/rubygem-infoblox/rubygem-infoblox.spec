# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name infoblox

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.0
Release: 2%{?dist}
Group: Development/Languages
Summary: A Ruby wrapper to the Infoblox WAPI.
License: MIT
URL: https://github.com/govdelivery/infoblox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(faraday)
Requires: %{?scl_prefix}rubygem(faraday_middleware)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
This gem is a Ruby interface to the Infoblox WAPI. Using the gem, you can query, create, update, and delete DNS records in your Infoblox instance


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
%exclude %{gem_instdir}/.ruby-version
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/RELEASES.md
%{gem_instdir}/Rakefile
%{gem_instdir}/infoblox.gemspec
%{gem_instdir}/spec

%changelog
* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-2
- Update to 3.0.0-2 for SCL

* Thu Jul 25 2019 Lukas Zapletal <lzap+rpm@redhat.com> 3.0.0-1
- Update infoblox to 3.0.0

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 2.0.4-1
- Update infoblox to 2.0.4 (ericdhelms@gmail.com)

* Tue Sep 06 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- new package built with tito

