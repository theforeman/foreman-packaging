%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name robotex

Summary: Ruby library to obey robots.txt 
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.0.0
Release:    9%{?dist}
License:    MIT 
Group:      Development/Languages
URL:        http://www.github.com/chriskite/robotex
Source:     http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:   %{?scl_prefix}rubygems

Provides:   %{?scl_prefix}rubygem(%{gem_name}) = %{version}
BuildRequires:  %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch:  noarch

%description
With one line of code, Robotex (pronounced like “robotics”) will download and parse the robots.txt file and let you know if your program is allowed to visit a given link.
%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir $RPM_BUILD_ROOT%{gem_dir} --force --rdoc %{SOURCE0}
%{?scl:"}

%{__rm} -Rf %{buildroot}/%{gem_instdir}/.yardoc

%check

%files
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%dir %{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/VERSION
%{gem_instdir}/Rakefile
%{gem_instdir}/lib/
%{gem_instdir}/spec/

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-9
- new package built with tito

* Tue Jan 29 2013 Justin Sherrill <jsherril@redhat.com> 1.0.0-8
- dropping abi requires for robotex & anemone (jsherril@redhat.com)

* Tue Jan 22 2013 Justin Sherrill <jsherril@redhat.com> 1.0.0-7
- fixing robotext abi requires (jsherril@redhat.com)

* Tue Jan 22 2013 Justin Sherrill <jsherril@redhat.com> 1.0.0-6
- bumping version for build 

* Tue Jan 22 2013 Justin Sherrill <jsherril@redhat.com> 1.0.0-5
- fixing robotex build for rhel6 (jsherril@redhat.com)

* Fri Nov 30 2012 Justin Sherrill <jsherril@redhat.com> 1.0.0-4
- only require rubygems-devel on rhel 6 (jsherril@redhat.com)

* Fri Nov 30 2012 Justin Sherrill <jsherril@redhat.com> 1.0.0-3
- removing uneeded rm to fix build (jsherril@redhat.com)

* Fri Nov 30 2012 Justin Sherrill <jsherril@redhat.com> 1.0.0-2
- new package built with tito


* Mon Jul 16 2012 Justin Sherrill <jsherril@redhat.com>  0.7.2-1
- new package built with tito

