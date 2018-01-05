%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name patternfly-sass

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.23.0
Release: 2%{?dist}
Summary: Red Hat's Patternfly, converted to Sass and ready to drop into Rails
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/Patternfly/patternfly-sass
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygem(bootstrap-sass) >= 3.3.7
Requires: %{?scl_prefix}rubygem(bootstrap-sass) < 3.4.0
Requires: %{?scl_prefix}rubygem(font-awesome-sass) >= 4.6.2
Requires: %{?scl_prefix}rubygem(font-awesome-sass) < 4.7.0
Requires: %{?scl_prefix_ror}rubygem(sass) >= 3.4.15
Requires: %{?scl_prefix_ror}rubygem(sass) < 3.5.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Red Hat's Patternfly, converted to Sass and ready to drop into Rails.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/OPEN_SOURCE_LICENCES.txt
%{gem_instdir}/assets
%{gem_instdir}/bower.json
%{gem_instdir}/package.json
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/patternfly-sass.gemspec
%{gem_instdir}/spec

%changelog
* Thu Mar 23 2017 Dominic Cleal <dominic@cleal.org> 3.23.0-1
- Update patternfly-sass to 3.23.0 (dominic@cleal.org)

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 3.15.0-1
- Update patternfly-sass to 3.15.0 (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 3.11.0-1
- Update patternfly-sass to 3.11.0 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 2.10.1-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 2.10.1-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Wed Feb 24 2016 Dominic Cleal <dominic@cleal.org> 2.10.1-1
- Update patternfly-sass to 2.10.1 (dominic@cleal.org)

* Thu Dec 31 2015 Daniel Lobato <elobatocs@gmail.com> 2.8.0-1
- Initial package
