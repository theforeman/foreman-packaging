%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name clamp

Summary: a minimal framework for command-line utilities
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.2
Release: 3%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: https://github.com/mdub/clamp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Clamp provides an object-model for command-line utilities.
It handles parsing of command-line options, and generation of usage help.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/spec
%{gem_instdir}/examples
%{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/LICENSE


%exclude %{gem_cache}
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.autotest
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/Guardfile

%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/README.md
%{gem_instdir}/CHANGES.md

%changelog
* Thu Aug 16 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.2-3
- Rebuild for Rails 5.2

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.2-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)

* Tue Oct 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.1.2-1
- Update rubygem-clamp to 1.1.2 (martin.bacovsky@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-5
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0.0-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.0.0-3
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 1.0.0-2
- Convert clamp to SCL (dcleal@redhat.com)

* Wed Jun 10 2015 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- update clamp to 1.0.0 (kvedulv@kvedulv.de)
- Modernise spec file (dcleal@redhat.com)

* Wed Aug 13 2014 Dominic Cleal <dcleal@redhat.com> 0.6.2-3
- refs #5787 - i18n support for clamp (tstrachota@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 0.6.2-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Fri Nov 08 2013 Marek Hulan <mhulan@redhat.com> 0.6.2-1
- Clamp version bump (mhulan@redhat.com)

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-9
- Final bump

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-8
- Bump one more time

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-7
- Bump version to match up tags

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-6
- Use macros provided by rubygems-devel on Fedora (shk@redhat.com)
- gem_instdir (shk@redhat.com)
- gem_instdir (shk@redhat.com)
- Remove rubygems-devel (shk@redhat.com)
- Use rubygems-devel (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.6.1-5
- Don't require ruby(abi) on F19+ (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-4
- Rebuild with the proper whitelist

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-3
- Rebuild

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-2
- Import the package into tito

* Wed Jul 31 2013  <shk@linux.com> - 0.6.1-1
- Initial package
