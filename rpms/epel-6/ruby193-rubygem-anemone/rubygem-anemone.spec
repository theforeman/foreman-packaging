%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name anemone

Summary: Anemone web-spider framework
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.7.2
Release:    8%{?dist}
License:    MIT 
Group:      Development/Languages
URL:        http://anemone.rubyforge.org/
Source:     http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

Requires:   %{?scl_prefix}rubygem-robotex >= 1.0.0
Requires:   %{?scl_prefix}rubygem-nokogiri >= 1.3.0 

BuildArch:  noarch

Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Anemone is a Ruby library that makes it quick and painless to write programs that spider a website. It provides a simple DSL for performing actions on every page of a site, skipping certain URLs, and calculating the shortest path to a given page on a site.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir $RPM_BUILD_ROOT%{gem_dir} --force --rdoc %{SOURCE0}
%{?scl:"}

mkdir -p %{buildroot}%{_bindir}/
mv  %{buildroot}%{gem_dir}/bin/%{gem_name} %{buildroot}%{_bindir}/
%{__rm} -Rf %{buildroot}/%{gem_instdir}/.yardoc

%check

%files
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{_bindir}/%{gem_name}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%dir %{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/VERSION
%{gem_instdir}/Rakefile
%{gem_instdir}/lib/
%{gem_instdir}/bin/
%{gem_instdir}/spec/

%changelog
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

