# Generated from wicked-1.3.3.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name wicked

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.3
Release: 1%{?dist}
Summary: Use Wicked to turn your controller into a wizard
Group: Development/Languages
License: MIT
URL: https://github.com/schneems/wicked
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.0.7
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end generated dependencies

%description
Wicked is a Rails engine for producing easy wizard controllers.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/Appraisals
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/gemfiles
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/wicked.gemspec

%changelog
* Wed Sep 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.3-1
- Update to 1.3.3-1

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 11 2018 Eric D. Helms <ericdhelms@gmail.com> 1.3.2-1
- Bump rubygem-wicked to 1.3.2 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-2
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Nov 03 2014 Daniel Lobato Garcia <dlobatog@redhat.com> 1.1.0-1
- Update release to 1.1.0 (dlobatog@redhat.com)

* Fri Jun 06 2014 Dominic Cleal <dcleal@redhat.com> 1.0.2-3
- Modernise and update for EL7 (dcleal@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 1.0.2-2
- Fixing wicked-doc dependency (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 1.0.2-1
- new package built with tito
