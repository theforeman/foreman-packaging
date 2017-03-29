%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name robotex

%define rubyabi 1.9.1

Summary:    Ruby library to obey robots.txt 
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.0.0
Release:    19%{?dist}
License:    MIT 
Group:      Development/Languages
URL:        http://www.github.com/chriskite/robotex
Source0:    https://rubygems.org/downloads/%{gem_name}-%{version}.gem

%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
Provides:   %{?scl_prefix}rubygem(%{gem_name}) = %{version}
BuildArch:  noarch

Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}ruby(release)

BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

%description
With one line of code, Robotex (pronounced like “robotics”) will download
and parse the robots.txt file and let you know if your program is allowed
to visit a given link.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep

%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%build
%if 0%{?fedora} > 18
%gem_install
%else
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{gem_name}-%{version}.gem
%{?scl:"}
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%{__rm} -Rf %{buildroot}/%{gem_instdir}/.yardoc

%check
pushd .%{gem_instdir}
# remove requires of bundler/setup
sed -i 2d spec/spec_helper.rb
%if 0%{?fedora}
%{?scl:scl enable %{scl} "}
rspec spec/
%{?scl:"}
%endif
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/VERSION

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/

%changelog
* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 1.0.0-19
- rebuilding for ruby on rails 4.2 (jsherril@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-18
- Build rubygem-robotex for rh22 SCL (ericdhelms@gmail.com)

* Thu Aug 27 2015 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-17
- new package built with tito

* Thu Sep 12 2013 Jason Montleon <jmontleo@redhat.com> 1.0.0-16
- update rubygems to include wrapper BuildRequires and Requires
  (jmontleo@redhat.com)

* Fri May 10 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-15
- rebuild for MDP1

* Wed May 08 2013 Bryan Kearney <bkearney@redhat.com> 1.0.0-14
- new package built with tito

* Mon Mar 18 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-12
- use correct path (msuchy@redhat.com)

* Mon Mar 18 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-11
- do not require bundler (msuchy@redhat.com)

* Mon Mar 18 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-10
- run tests (msuchy@redhat.com)

* Fri Mar 15 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.0-9
- comply to Fedora Guidelines (msuchy@redhat.com)

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

