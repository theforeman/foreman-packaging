# template: default
%global gem_name validates_lengths_from_database

Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 1%{?dist}
Summary: Automatic maximum-length validations
License: MIT
URL: https://github.com/rubiety/validates_lengths_from_database
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4
BuildRequires: ruby >= 2.4
BuildRequires: rubygems-devel >= 1.3.4
BuildArch: noarch
# end specfile generated dependencies

%description
Introspects your database string field maximum lengths and automatically
defines length validations.


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
%exclude %{gem_instdir}/Appraisals
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/init.rb
%{gem_libdir}
%exclude %{gem_instdir}/rails
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.8.0-1
- Update to 0.8.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.0-8
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.0-7
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.0-6
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.5.0-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.0-4
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.5.0-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.5.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Feb 16 2016 Dominic Cleal <dominic@cleal.org> 0.5.0-1
- Update validates_lengths_from_database to 0.5.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-1
- Update validates_lengths_from_database to 0.4.0 (dcleal@redhat.com)

* Thu Jul 31 2014 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- new package built with tito
