# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name actionview
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 6.0.3.5
Release: 2%{?dist}
Summary: Rendering framework putting the V in MVC (part of Rails)
Group: Development/Languages
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activesupport) = 6.0.3.5
Requires: %{?scl_prefix}rubygem(builder) >= 3.1
Requires: %{?scl_prefix}rubygem(builder) < 4
Requires: %{?scl_prefix}rubygem(erubi) >= 1.4
Requires: %{?scl_prefix}rubygem(erubi) < 2
Requires: %{?scl_prefix}rubygem(rails-html-sanitizer) >= 1.1
Requires: %{?scl_prefix}rubygem(rails-html-sanitizer) < 2
Requires: %{?scl_prefix}rubygem(rails-html-sanitizer) >= 1.2.0
Requires: %{?scl_prefix}rubygem(rails-dom-testing) >= 2.0
Requires: %{?scl_prefix}rubygem(rails-dom-testing) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 5.2.1

%description
Simple, battle-tested conventions and helpers for building web pages.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
* Wed Mar 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.5-2
- Rebuild against rh-ruby27

* Tue Feb 23 2021 Evgeni Golov - 6.0.3.5-1
- Release rubygem-actionview 6.0.3.5

* Mon Oct 26 2020 Evgeni Golov - 6.0.3.4-1
- Release rubygem-actionview 6.0.3.4

* Mon Jun 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.1-1
- Release rubygem-actionview 6.0.3.1

* Tue Apr 28 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.0.2.2-1
- Update to 6.0.2.2

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.0.2.1-1
- Release rubygem-actionview 6.0.2.1

* Wed Feb 05 2020  Zach Huntington-Meath <zhunting@redhat.com> 5.2.1-3
- Obsolete the ror-52 version of this package

* Wed Jan 08 2020  Zach Huntington-Meath <zhunting@redhat.com> 5.2.1-2
- Move from rails-packaging into foreman-packaging

* Wed Aug 22 2018 Eric D. Helms <ericdhelms@gmail.com> 5.2.1-1
- Release tfm-ror52-rubygem-actionview 5.2.1

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-2
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-1
- Initial package
