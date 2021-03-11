# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name i18n

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.2
Release: 2%{?dist}
Summary: New wave Internationalization support for Ruby
Group: Development/Languages
License: MIT
URL: http://github.com/svenfuchs/i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0.0
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.5
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 1.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.5
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 1.4.0

%description
New wave Internationalization support for Ruby.


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
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.8.2-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.2-1
- Release rubygem-i18n 1.8.2

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.0-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.0-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.4.0-2
- Bump for moving over to foreman-packaging

* Thu Jan 03 2019 Michael Moll <mmoll@mmoll.at> - 1.4.0-1
- Update to 1.4.0

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-1
- Initial package
