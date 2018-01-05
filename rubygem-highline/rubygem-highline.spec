%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name highline

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   1.7.8
Release:   3%{?dist}
Summary:   HighLine is a high-level command-line IO library
Group:     Development/Languages
License:   GPLv2+ or Ruby
URL:       https://github.com/JEG2/highline
Source0:   https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:  %{?scl_prefix_ruby}ruby(release)
Requires:  %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} - <<EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} - <<EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/INSTALL
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/doc
%{gem_instdir}/*.gemspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/setup.rb
%{gem_instdir}/site
%{gem_instdir}/test
%exclude %{gem_instdir}/.*

%changelog
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
