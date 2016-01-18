%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name patternfly-sass

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.8.0
Release: 1%{?dist}
Summary: Red Hat's Patternfly, converted to Sass and ready to drop into Rails
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/Patternfly/patternfly-sass
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygem(bootstrap-sass) >= 3.3.5
Requires: %{?scl_prefix}rubygem(bootstrap-sass) < 3.4.0
Requires: %{?scl_prefix}rubygem(font-awesome-sass) >= 4.3.0
Requires: %{?scl_prefix}rubygem(font-awesome-sass) < 4.4.0
Requires: %{?scl_prefix}rubygem(sass) >= 3.4.15
Requires: %{?scl_prefix}rubygem(sass) < 3.5.0
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
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/assets
%{gem_instdir}/bower.json
%{gem_libdir}
%{gem_instdir}/package.json
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
* Thu Dec 31 2015 Daniel Lobato <elobatocs@gmail.com> 2.8.0-1
- Initial package
