# template: default
%global gem_name friendly_id

Name: rubygem-%{gem_name}
Version: 5.5.1
Release: 1%{?dist}
Summary: A comprehensive slugging and pretty-URL plugin
License: MIT
URL: https://github.com/norman/friendly_id
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.1.0
BuildRequires: ruby >= 2.1.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Active Record. It lets you create pretty URLs and work with human-friendly
strings as if they were numeric ids.


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
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/bench.rb
%exclude %{gem_instdir}/certs
%exclude %{gem_instdir}/gemfiles
%exclude %{gem_instdir}/guide.rb
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/UPGRADING.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/friendly_id.gemspec
%{gem_instdir}/test

%changelog
* Thu Nov 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.5.1-1
- Update to 5.5.1

* Sun Nov 20 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.5.0-1
- Update to 5.5.0

* Wed Aug 03 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.4.2-1
- Update to 5.4.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.3.0-2
- Rebuild against rh-ruby27

* Fri May 01 2020 Michael Moll <mmoll@mmoll.at> - 5.3.0-1
- Update friendly_id to 5.3.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.4-4
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.4-3
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.4-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jun 04 2018 Michael Moll <mmoll@mmoll.at> 5.2.4-1
- Update to 5.2.4

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.1.0-4
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 5.1.0-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 5.1.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 5.1.0-1
- Update friendly_id to 5.1.0 (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 4.0.10.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Sep 29 2014 Dominic Cleal <dcleal@redhat.com> 4.0.10.1-1
- new package built with tito
