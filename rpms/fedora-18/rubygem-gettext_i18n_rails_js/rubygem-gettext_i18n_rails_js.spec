%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name gettext_i18n_rails_js
%global rubyabi 1.9.1

Summary: Extends gettext_i18n_rails making your .po files available to client side javascript as JSON
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.8
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/nubis/gettext_i18n_rails_js
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails) >= 0.7.1
Requires: %{?scl_prefix}rubygem(rails) >= 3.2.0
Requires: %{?scl_prefix}rubygem(rails) < 3.3.0
Requires: %{?scl_prefix}rubygem(po_to_json) >= 0.0.7
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
gettext_i18n_rails will find translations inside your .js and .coffee files,
then it will create JSON versions of your .PO files and will let you serve
them with the rest of your assets, thus letting you access all your
translations offline from client side javascript.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/MIT-LICENSE
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Tue May 14 2013 Dominic Cleal <dcleal@redhat.com> 0.0.8-1
- new package built with tito

