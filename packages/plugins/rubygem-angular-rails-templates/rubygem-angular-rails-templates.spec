# template: default
%global gem_name angular-rails-templates

Name:      rubygem-%{gem_name}
Version:   1.3.1
Release:   1%{?dist}
Epoch:     1
Summary:   Use your angular templates with rails' asset pipeline
License:   MIT
URL:       https://github.com/pitr/angular-rails-templates
Source0:   https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Use your angular templates with rails' asset pipeline.


%package doc
BuildArch:  noarch
Requires:   %{name} = %{epoch}:%{version}-%{release}
Summary:    Documentation for %{name}

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
%doc %{gem_instdir}/README.md

%changelog
* Thu Feb 27 2025 Eric D. Helms <ericdhelms@gmail.com> - 1:1.3.1-1
- Update to 1.3.1

* Tue Nov 19 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.2.2-1
- Update to 1.2.2

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:1.1.0-2
- Rebuild for Ruby 2.7

* Wed Apr 08 2020 Michael Moll <mmoll@mmoll.at> - 1:1.1.0-1
- Update to 1.1.0

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1:1.0.2-5
- Update spec to remove the ror scl

* Mon Oct 01 2018 Ivan Necas <inecas@gmail.com> - 1.0.2-4
- Add patch to enable running in FIPS mode

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1:1.0.2-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0.2-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Aug 18 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.2-1
- Update rubygem-angular-rails-templates to 1.0.2 (kvedulv@kvedulv.de)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-5
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-4
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace tfm-rubygem-sprockets with ror41-rubygem-sprockets
  (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)
- Fix typo in -doc requires on main package (dcleal@redhat.com)

* Thu Feb 12 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-2
- Fix dep to include epoch between -doc and main package (dcleal@redhat.com)

* Thu Feb 12 2015 Eric D. Helms <ericdhelms@gmail.com> 0.1.2-1
- Update rubygem-angular-rails-templates to 0.1.2 (ericdhelms@gmail.com)

* Mon Feb 09 2015 Eric D. Helms <ericdhelms@gmail.com> 0.1.3-1
- Update 'rubygem-angular-rails-templates' to 0.1.3 (ericdhelms@gmail.com)

* Thu Oct 02 2014 Dominic Cleal <dcleal@redhat.com> 0.0.4-7
- new package built with tito (ehelms@redhat.com)
