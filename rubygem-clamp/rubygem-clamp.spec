%global gem_name clamp

Summary: a minimal framework for command-line utilities
Name: rubygem-%{gem_name}
Version: 0.6.2
Release: 3%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/mdub/clamp
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Support for localization of clamp's messages.
# Patching temporarily until https://github.com/mdub/clamp/pull/43 is merged.
Patch0: rubygem-clamp-0.6.2-i18n-support.patch

%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
Requires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Clamp provides an object-model for command-line utilities.
It handles parsing of command-line options, and generation of usage help.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

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


%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.autotest
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_instdir}/README.md
%{gem_instdir}/CHANGES.md


%changelog
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
