%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name anemone

Summary:    Anemone web-spider framework
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.7.2
Release:    18%{?dist}
License:    MIT
Group:      Development/Languages
URL:        http://anemone.rubyforge.org/
Source:     https://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix}rubygem(robotex) >= 1.0.0
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.3.0

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)

BuildArch:  noarch
Provides:   %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Anemone is a Ruby library that makes it quick and painless to write programs that spider a website. It provides a simple DSL for performing actions on every page of a site, skipping certain URLs, and calculating the shortest path to a given page on a site.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
%{__rm} -Rf %{buildroot}/%{gem_instdir}/.yardoc
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%dir %{gem_dir}/gems/%{gem_name}-%{version}/
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bin/anemone
%exclude %{gem_dir}/bin/anemone
%{gem_instdir}/Rakefile
%{gem_instdir}/lib/
%{gem_instdir}/spec/

%doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/VERSION

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.2-18
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.2-17
- Update spec to remove the ror scl

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.2-16
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 0.7.2-15
- new package built with tito

* Wed Apr 27 2016 Justin Sherrill <jsherril@redhat.com> 0.7.2-14
- more updates for ror42 builds (jsherril@redhat.com)

* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 0.7.2-13
- rebuild for ror42 scl (jsherril@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.7.2-12
- Build rubygem-anemone for rh22 SCL (ericdhelms@gmail.com)

* Fri Aug 28 2015 Eric D. Helms <ericdhelms@gmail.com> 0.7.2-11
- new package built with tito

* Wed May 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.2-10
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Mon Mar 18 2013 Lukas Zapletal <lzap+git@redhat.com> 0.7.2-8
- adding missing provide for anemone

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.7.2-7
- fixing ruby193 scl package (lzap+git@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.2-6
- new package built with tito

* Tue Jan 29 2013 Justin Sherrill <jsherril@redhat.com> 0.7.2-5
- dropping abi requires for robotex & anemone (jsherril@redhat.com)

* Tue Jan 22 2013 Justin Sherrill <jsherril@redhat.com> 0.7.2-4
- fixing abi spec requires (jsherril@redhat.com)

* Mon Dec 03 2012 Eric D Helms <ehelms@redhat.com> 0.7.2-3
- Rubygem-anemone - Defines some common gem variables for RHEL6.
  (ehelms@redhat.com)

* Mon Dec 03 2012 Eric D Helms <ehelms@redhat.com>
- Rubygem-anemone - Defines some common gem variables for RHEL6.
  (ehelms@redhat.com)

* Fri Nov 30 2012 Justin Sherrill <jsherril@redhat.com> 0.7.2-2
- new package built with tito


* Mon Jul 16 2012 Justin Sherrill <jsherril@redhat.com>  0.7.2-1
- new package built with tito

