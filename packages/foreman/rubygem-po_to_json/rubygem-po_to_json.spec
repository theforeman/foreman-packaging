# template: default
%global gem_name po_to_json

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: Convert gettext PO files to JSON
License: MIT
URL: https://github.com/webhippie/po_to_json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.3
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Convert gettext PO files to JSON objects so that you can use it in your
application.


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
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Fri May 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.0-1
- Update to 1.1.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-6
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.1-5
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.1-3
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.0.1-2
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update po_to_json to 1.0.1 (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-3
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.7-2
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Tue May 14 2013 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- new package built with tito
