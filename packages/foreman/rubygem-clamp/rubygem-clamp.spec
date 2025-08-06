# template: default
%global gem_name clamp

Name: rubygem-%{gem_name}
Version: 1.3.3
Release: 1%{?dist}
Summary: a minimal framework for command-line utilities
License: MIT
URL: https://github.com/mdub/clamp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
Requires: ruby < 4
BuildRequires: ruby >= 2.5
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Clamp provides an object-model for command-line utilities.
It handles parsing of command-line options, and generation of usage help.


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
%exclude %{gem_instdir}/.autotest
%exclude %{gem_instdir}/.editorconfig
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%doc %{gem_instdir}/CHANGES.md
%exclude %{gem_instdir}/CODEOWNERS
%exclude %{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/clamp.gemspec
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Wed Aug 06 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.3.3-1
- Update to 1.3.3

* Fri May 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.3.2-1
- Update to 1.3.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.2-7
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.2-6
- Bump to release for EL8

* Thu Mar 26 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.1.2-5
- Rebuild for EL8

* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 1.1.2-4
- Use ASL 2.0 instead of Apache 2.0 or Apache-2.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.2-3
- Rebuild for Rails 5.2 and Ruby 2.5

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
