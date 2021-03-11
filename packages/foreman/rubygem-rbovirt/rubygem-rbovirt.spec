%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rbovirt

Summary: A Ruby client for oVirt REST API
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.1.7
Release: 5%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/abenari/rbovirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
Requires: %{?scl_prefix}rubygem-nokogiri

Requires: %{?scl_prefix}rubygem-rest-client > 1.7.0
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(rbovirt) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%define gembuilddir %{buildroot}%{gem_dir}

%description
A Ruby client for oVirt REST API

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

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

rm -f %{buildroot}%{gem_instdir}/.document
rm -rf %{buildroot}%{gem_instdir}/.yardoc

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/lib
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}

%files doc
%doc %{gem_instdir}/CHANGES.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/rbovirt.gemspec
%doc %{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.7-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.7-4
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.7-3
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.7-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jul 24 2018 Ivan Nečas <inecas@redhat.com> 0.1.7-1
- Update to 0.1.7

* Tue Jun 19 2018 Ori Rabin <orrabin@gmail.com> 0.1.6-1
- Update to 0.1.6

* Tue Mar 20 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.5-1
- Update to 0.1.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.4-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Automatic commit of package [rubygem-rbovirt] minor release [0.1.4-1.fm1_16].
  (me@daniellobato.me)
- Update rbovirt to 0.1.4 (inecas@redhat.com)

* Tue Aug 29 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.4-1
- Update rbovirt to 0.1.4 (inecas@redhat.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Feb 22 2017 Dominic Cleal <dominic@cleal.org> 0.1.3-1
- Updated rbovirt to 0.1.3 (lzap+git@redhat.com)

* Thu Aug 18 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- Updated rbovirt to 0.1.2 (lzap+git@redhat.com)

* Wed May 25 2016 Dominic Cleal <dominic@cleal.org> 0.1.1-1
- Update rbovirt to 0.1.1 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.37-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.0.37-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Wed Apr 13 2016 Dominic Cleal <dominic@cleal.org> 0.0.37-1
- Update rbovirt to 0.0.37 (dominic@cleal.org)

* Fri Mar 18 2016 Dominic Cleal <dominic@cleal.org> 0.0.36-1
- Updated rubygem-rbovirt to 0.0.36 (lzap+git@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.0.35-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.35-2
- Converted to tfm SCL (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)

* Tue Feb 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.35-1
- Update rbovirt to 0.0.35 (dcleal@redhat.com)

* Mon Feb 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.34-1
- Update rbovirt to 0.0.34 (dcleal@redhat.com)

* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.0.32-1
- Update rbovirt to 0.0.32 (dcleal@redhat.com)

* Fri Dec 12 2014 Dominic Cleal <dcleal@redhat.com> 0.0.31-1
- Update rbovirt to 0.0.31 (dcleal@redhat.com)

* Thu Nov 27 2014 Dominic Cleal <dcleal@redhat.com> 0.0.30-1
- Update rbovirt to 0.0.30 (dcleal@redhat.com)

* Fri Aug 01 2014 Dominic Cleal <dcleal@redhat.com> 0.0.29-1
- Rebase to rbovirt 0.0.29 (dcleal@redhat.com)

* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> 0.0.28-1
- Rebase to rbovirt 0.0.28 (dcleal@redhat.com)

* Mon Jun 16 2014 Dominic Cleal <dcleal@redhat.com> 0.0.27-1
- Rebase to rbovirt 0.0.27 (dcleal@redhat.com)

* Mon Apr 14 2014 Dominic Cleal <dcleal@redhat.com> 0.0.26-1
- Rebase to rbovirt 0.0.26 (dcleal@redhat.com)

* Wed Apr 02 2014 Dominic Cleal <dcleal@redhat.com> 0.0.25-1
- Rebase to rbovirt 0.0.25 (dcleal@redhat.com)

* Mon Mar 24 2014 Dominic Cleal <dcleal@redhat.com> 0.0.24-1
- Rebase to rbovirt 0.0.24 (dcleal@redhat.com)

* Thu Feb 13 2014 Dominic Cleal <dcleal@redhat.com> 0.0.23-1
- Rebase to rbovirt 0.0.23 (dcleal@redhat.com)

* Wed Feb 12 2014 Dominic Cleal <dcleal@redhat.com> 0.0.22-1
- Rebase to rbovirt 0.0.22 (dcleal@redhat.com)

* Mon Jul 22 2013 Dominic Cleal <dcleal@redhat.com> 0.0.21-2
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Mon Jul 22 2013 Dominic Cleal <dcleal@redhat.com> 0.0.21-1
- Rebase to rbovirt 0.0.21 (dcleal@redhat.com)

* Thu May 23 2013 Dominic Cleal <dcleal@redhat.com> 0.0.20-1
- rebase to rbovirt-0.0.20.gem (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.16-3
- put correct license in spec (msuchy@redhat.com)

* Tue Mar 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.16-2
- rebase to rbovirt-0.0.16.gem (msuchy@redhat.com)

* Thu Jan 03 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.16-1
- rebase to rbovirt-0.0.16.gem (msuchy@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.12-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.12-1
- new package built with tito
