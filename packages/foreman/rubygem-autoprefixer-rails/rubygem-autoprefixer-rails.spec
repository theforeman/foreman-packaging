%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name autoprefixer-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.2.1.3
Release: 7%{?dist}
Summary: Add vendor prefixes to CSS rules using values from caniuse.com
Group: Development/Languages
License: MIT
URL: https://github.com/ai/autoprefixer-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix}rubygem(execjs)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Parse CSS and add vendor prefixes to CSS rules using values from the Can I Use
website.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %scl - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %scl - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %scl - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.rails3
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/autoprefixer-rails.gemspec
%{gem_instdir}/spec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.2.1.3-7
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1.3-6
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1.3-5
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.1.3-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.2.1.3-3
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 5.2.1.3-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Jan 05 2016 Daniel Lobato <elobatocs@gmail.com> 5.2.1.3-1
- Initial package
