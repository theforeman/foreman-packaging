%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from jquery-ui-rails-4.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-ui-rails

Summary: jQuery UI packaged for the Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.1.2
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/joliss/jquery-ui-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.6
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.6
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
jQuery UI's JavaScript, CSS, and image files packaged for the Rails 3.1+ asset
pipeline


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

rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.gitmodules,.travis.yml,Gemfile,Rakefile}



%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/License.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/VERSIONS.md
%doc %{gem_instdir}/History.md

%changelog
* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 4.1.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.1.2-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 4.1.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Nov 18 2014 Dominic Cleal <dcleal@redhat.com> 4.1.2-1
- Update jquery-ui-rails to 4.1.2 (dcleal@redhat.com)

* Thu Jun 27 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-7
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-5
- fix files section (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-4
- fix files section (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-3
- new package built with tito

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-2
- new package built with tito

* Thu Mar 28 2013 msuchy@redhat.com - 4.0.2-1
- Initial package
