# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name thor

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.1
Release: 3%{?dist}
Summary: Thor is a toolkit for building powerful command-line interfaces
Group: Development/Languages
License: MIT
URL: http://whatisthor.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.8.7
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.5
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.8.7
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.5
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 1.0.1

%description
Thor is a toolkit for building powerful command-line interfaces.


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
%{_bindir}/thor
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/thor.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-3
- Rebuild against rh-ruby27

* Tue May 19 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.1-2
- Add missing obsoletes tfm-ror52 line

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.1-1
- Release rubygem-thor 1.0.1

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.20.0-6
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.20.0-5
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 0.20.0-4
- Bump for moving over to foreman-packaging

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.20.0-3
- Add missing gem_docdir

* Wed Aug 08 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.20.0-2
- Update for new gem_install

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.20.0-1
- Initial package
