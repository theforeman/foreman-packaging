# template: default
%global gem_name unicode-display_width

Name: rubygem-%{gem_name}
Version: 2.4.2
Release: 1%{?dist}
Summary: Determines the monospace display width of a string in Ruby
License: MIT
URL: https://github.com/janlelis/unicode-display_width
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4.0
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
[Unicode 15.0.0] Determines the monospace display width of a string using
EastAsianWidth.txt, Unicode general category, and other data.


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
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Tue Aug 01 2023 Eric D. Helms <ericdhelms@gmail.com> 2.4.2-1
- Update to 2.4.2-1

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.8.0-1
- Update to 1.8.0

* Mon Apr 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-2
- Rebuild against rh-ruby27

* Mon Mar 22 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-1
- Release rubygem-unicode-display_width 1.7.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.5-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.5-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.5-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon May 09 2016 Dominic Cleal <dominic@cleal.org> 1.0.5-1
- Update unicode-display_width to 1.0.5 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.1.1-8
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.1.1-7
- Converted to tfm SCL (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.1-4
- new package built with tito

* Mon Sep 10 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.1-3
- remove yardoc (msuchy@redhat.com)

* Mon Sep 10 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.1-2
- new package built with tito
