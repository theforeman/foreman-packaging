# template: default
%global gem_name mini_mime

Name: rubygem-%{gem_name}
Version: 1.1.5
Release: 1%{?dist}
Summary: A minimal mime type library
License: MIT
URL: https://github.com/discourse/mini_mime
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6.0
BuildRequires: ruby >= 2.6.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A minimal mime type library.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bench
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/mini_mime.gemspec

%changelog
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.5-1
- Update to 1.1.5

* Mon May 16 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.1.2-1
- Release rubygem-mini_mime 1.1.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.2-1
- Release rubygem-mini_mime 1.0.2

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.0.0-2
- Bump for moving over to foreman-packaging

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-1
- Initial package
