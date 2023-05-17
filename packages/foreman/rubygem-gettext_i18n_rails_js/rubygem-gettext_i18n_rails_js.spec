# template: default
%global gem_name gettext_i18n_rails_js

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 1%{?dist}
Summary: Extends gettext_i18n_rails making your .po files available to client side javascript as JSON
License: MIT
URL: https://github.com/webhippie/gettext_i18n_rails_js
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.3
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
It will find translations inside your .js and .coffee files, then it will
create JSON versions of your .PO files and will let you serve them with the
rest of your assets, thus letting you access all your translations offline
from client side javascript.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
* Wed May 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.4.0-1
- Update to 1.4.0

* Tue Jan 04 2022 Evgeni Golov 1.3.1-1
- Update to 1.3.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.3-8
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.3-7
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.3-6
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.3-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Sun Jun 03 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.3-4
- Rebuilt with rails 5.1

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
