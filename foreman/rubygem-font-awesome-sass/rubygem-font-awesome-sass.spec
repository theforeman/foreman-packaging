%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name font-awesome-sass

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.6.2
Release: 1%{?dist}
Summary: Font-Awesome SASS
Group: Development/Languages
License: MIT
URL: https://github.com/FortAwesome/font-awesome-sass
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ror}rubygem(sass) >= 3.2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Font-Awesome SASS gem to be used in Ruby projects.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

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
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/assets
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/font-awesome-sass.gemspec

%changelog
* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 4.6.2-1
- Update font-awesome-sass to 4.6.2 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 4.3.2.1-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 4.3.2.1-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 31 2015 Daniel Lobato <elobatocs@gmail.com> 4.3.2.1-1
- Initial package
