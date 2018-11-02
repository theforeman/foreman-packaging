# Generated from kafo_parsers-0.1.6.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name kafo_parsers

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: Puppet module parsers
Group: Development/Languages
License: GPLv3+
URL: https://github.com/theforeman/kafo_parsers
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(rdoc) >= 3.9.0
Requires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end generated dependencies

%description
This gem can parse values, validations, documentation, types, groups and
conditions of parameters from your puppet modules.


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
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Thu Nov 15 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-1
- Update to 1.0.0
- Regenerate spec file based on the current template

* Thu Jan 05 2017 Dominic Cleal <dominic@cleal.org> 0.1.6-1
- Update kafo_parsers to 0.1.6 (ares@users.noreply.github.com)

* Wed Nov 23 2016 Dominic Cleal <dominic@cleal.org> 0.1.5-1
- Update kafo_parsers to 0.1.5 (mhulan@redhat.com)

* Mon Oct 31 2016 Dominic Cleal <dominic@cleal.org> 0.1.4-1
- Update kafo_parsers to 0.1.4 (mhulan@redhat.com)

* Tue Sep 13 2016 Dominic Cleal <dominic@cleal.org> 0.1.3-1
- Update kafo_parsers to 0.1.3 (mhulan@redhat.com)

* Fri May 06 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- Update kafo_parsers to 0.1.2 (mhulan@redhat.com)

* Thu May 05 2016 Dominic Cleal <dominic@cleal.org> 0.1.1-1
- Update kafo_parsers to 0.1.1 (mhulan@redhat.com)

* Mon Apr 11 2016 Dominic Cleal <dominic@cleal.org> 0.1.0-1
- Update kafo_parsers to 0.1.0 (mhulan@redhat.com)

* Thu Feb 11 2016 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Update kafo_parsers to 0.0.6 (mhulan@redhat.com)

* Mon Jan 04 2016 Dominic Cleal <dcleal@redhat.com> 0.0.5-2
- Modernise specs for ruby193/tfm change (dcleal@redhat.com)

* Sun Mar 29 2015 Marek Hulan <mhulan@redhat.com> 0.0.5-1
- fixes #9916 - initialise Puppet using public APIs (dcleal@redhat.com)
- Pin test gems for compatibility (dcleal@redhat.com)

* Mon Sep 01 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-1
- Add support for parsing definitions (mhulan@redhat.com)

* Fri May 30 2014 Marek Hulan <mhulan@redhat.com> 0.0.3-1
- Modernise and update spec file for EL7 (dcleal@redhat.com)
- Fix annoying typo (dcleal@redhat.com)

* Mon Mar 31 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-1
- Fix validation parsing of classes without code (mhulan@redhat.com)
- Correct example in README (jcmcken@gmail.com)
- Update readme (mhulan@redhat.com)

