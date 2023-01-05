# template: default
%global gem_name highline

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: HighLine is a high-level command-line IO library
License: Ruby
URL: https://github.com/JEG2/highline
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A high-level IO library that provides validation, type conversion, and more
for
command-line interfaces. HighLine also includes a complete menu system that
can
crank out anything from simple list selection to complete shells with just
minutes of work.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.simplecov
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/TODO
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/site
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/examples
%exclude %{gem_instdir}/highline.gemspec

%changelog
* Wed Jan 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.1.0-1
- Update to 2.1.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-2
- Rebuild against rh-ruby27

* Fri Dec 18 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-1
- Release rubygem-highline 2.0.3

* Thu Mar 26 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.7.8-5
- Rebuild for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.7.8-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.7.8-3
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Fri Feb 10 2017 Dominic Cleal <dominic@cleal.org> 1.7.8-2
- Fix gem_name expansion for -doc dep (dominic@cleal.org)

* Thu Feb 09 2017 Dominic Cleal <dominic@cleal.org> 1.7.8-1
- Update highline to 1.7.8 (dominic@cleal.org)
- Modernise spec file (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.6.21-5
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.6.21-4
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.6.21-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.6.21-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Mon Mar 10 2014 Marek Hulan <mhulan@redhat.com> 1.6.21-1
- Update highline to 1.6.21 (mhulan@redhat.com)

* Mon Nov 18 2013 Marek Hulan <mhulan@redhat.com> 1.6.20-2
- SCLize highline (mhulan@redhat.com)

* Mon Nov 18 2013 Marek Hulan <mhulan@redhat.com> 1.6.20-1
- Bump Highline (mhulan@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 1.6.1-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 1.6.1-1
- Initial package
