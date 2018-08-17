%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name jquery_pwstrength_bootstrap_4

Summary: A small wrapper over jquery.pwstrength.bootstrap library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.2
Release: 5%{?dist}
Group: Development/Languages
License: MIT or GPLv3+
URL: https://github.com/unorthodoxgeek/jquery_pwstrength_bootstrap-gem
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.1

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
Obsoletes: %{?scl_prefix}rubygem-jquery_pwstrength_bootstrap < 1.2.2-3

%description
The jQuery Password Strength Meter is a plugin for Twitter Bootstrap that
provides rulesets for visualy displaying the quality of a users typed in
password.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_instdir}/jquery_pwstrength_bootstrap.gemspec
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE.txt
%doc %{gem_instdir}/GPL-LICENSE.txt
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%changelog
* Thu Aug 16 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.2-5
- Rebuild for Rails 5.2

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.2.2-4
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.2.2-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-2
- Fix obsoletion of old package name (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.2.2-1
- new package built with tito

