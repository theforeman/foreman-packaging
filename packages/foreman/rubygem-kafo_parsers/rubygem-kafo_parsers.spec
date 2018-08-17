%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name kafo_parsers

Summary: Puppet module parsers
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.6
Release: 2%{?dist}
Group: Development/Libraries
License: GPLv3+
URL: https://github.com/theforeman/kafo_parsers
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix}ruby(abi)
%else
Requires: %{?scl_prefix}ruby(release)
%endif
Requires: %{?scl_prefix}rubygem(rdoc)
Requires: %{?scl_prefix}rubygem(json)
Requires: %{?scl_prefix}rubygems

BuildRequires: %{?scl_prefix}rubygems-devel

%if 0%{?el6} && 0%{!?scl:1}
BuildRequires: %{?scl_prefix}ruby(abi)
%else
BuildRequires: %{?scl_prefix}ruby(release)
%endif
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem can parse values, validations, documentation, types, groups and conditions of parameters from your puppet modules

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib

%doc %{gem_instdir}/LICENSE.txt

%exclude %{gem_instdir}/README.md
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
# add once tests are added (maybe spec dir instead)
#%exclude %{gem_instdir}/test
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md

%changelog
* Thu Aug 16 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.6-2
- Rebuild for Rails 5.2

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

