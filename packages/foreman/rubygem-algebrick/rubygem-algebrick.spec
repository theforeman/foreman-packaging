# template: default
%global gem_name algebrick

Name: rubygem-%{gem_name}
Version: 0.7.5
Release: 1%{?dist}
Summary: Algebraic types and pattern matching for Ruby
License: Apache-2.0
URL: https://github.com/pitr-ch/algebrick
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Provides algebraic type definitions and pattern matching.


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
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README_FULL.md
%doc %{gem_instdir}/doc

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.7.5-1
- Update to 0.7.5

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.3-8
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.3-7
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.3-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.7.3-5
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-2
- Package algebrick for non-SCL el7 (stbenjam@redhat.com)

* Tue Jul 07 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-1
- Update algebrick to 0.7.3 (dcleal@redhat.com)

* Thu Jul 02 2015 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Update algebrick to 0.7.0 (inecas@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-2
- Fix scl build (inecas@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-1
- new package built with tito
