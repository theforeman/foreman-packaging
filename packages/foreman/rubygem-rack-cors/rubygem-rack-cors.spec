# template: default
%global gem_name rack-cors

Name: rubygem-%{gem_name}
Version: 1.0.6
Release: 1%{?dist}
Summary: Middleware for enabling Cross-Origin Resource Sharing in Rack apps
License: MIT
URL: https://github.com/cyu/rack-cors
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Middleware that will make Rack-based apps CORS compatible. Fork the project
here: https://github.com/cyu/rack-cors.


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
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rack-cors.gemspec
%{gem_instdir}/test

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.0.6-1
- Update to 1.0.6

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.2-2
- Bump to release for EL8

* Mon Feb 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.2-1
- Add rubygem-rack-cors generated by gem2rpm using the scl template

