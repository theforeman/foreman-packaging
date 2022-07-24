# template: default
%global gem_name sass

Name: rubygem-%{gem_name}
Version: 3.7.4
Release: 1%{?dist}
Summary: A powerful but elegant CSS compiler that makes CSS fun again
License: MIT
URL: https://sass-lang.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Ruby Sass is deprecated! See https://sass-lang.com/ruby-sass for
details.
Sass makes CSS fun again. Sass is an extension of CSS, adding
nested rules, variables, mixins, selector inheritance, and more.
It's translated to well-formatted, standard CSS using the
command line tool or a web-framework plugin.


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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/sass
%{_bindir}/sass-convert
%{_bindir}/scss
%exclude %{gem_instdir}/.yardopts
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/REVISION
%{gem_instdir}/VERSION
%{gem_instdir}/VERSION_DATE
%{gem_instdir}/VERSION_NAME
%{gem_instdir}/bin
%{gem_instdir}/extra
%{gem_instdir}/init.rb
%{gem_libdir}
%{gem_instdir}/rails
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
* Sun Jul 24 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.7.4-1
- Update to 3.7.4

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.4.25-5
- Rebuild against rh-ruby27

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.25-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.25-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 3.4.25-2
- Bump for moving over to foreman-packaging

* Tue Aug 14 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.4.25-1
- Initial package
