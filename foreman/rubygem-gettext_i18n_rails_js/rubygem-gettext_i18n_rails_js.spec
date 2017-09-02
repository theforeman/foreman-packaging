%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name gettext_i18n_rails_js

Summary: Extends gettext_i18n_rails making your .po files available to client side javascript as JSON
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.3
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/nubis/gettext_i18n_rails_js
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(gettext) >= 3.0.2
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails) >= 0.7.1
Requires: %{?scl_prefix_ror}rubygem(rails) >= 3.2.0
Requires: %{?scl_prefix}rubygem(po_to_json) >= 1.0.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
gettext_i18n_rails will find translations inside your .js and .coffee files,
then it will create JSON versions of your .PO files and will let you serve
them with the rest of your assets, thus letting you access all your
translations offline from client side javascript.

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
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/LICENSE
%{gem_instdir}/README.md
%exclude %{gem_instdir}/spec

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.0.3-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.0.3-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0.3-1
- Update gettext_i18n_rails_js to 1.0.3 (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-3
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.8-2
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Tue May 14 2013 Dominic Cleal <dcleal@redhat.com> 0.0.8-1
- new package built with tito
