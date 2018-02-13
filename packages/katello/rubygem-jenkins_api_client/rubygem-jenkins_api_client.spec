%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%global gem_name jenkins_api_client

Summary: Jenkins Api client with features focused on automating Job configuration programaticaly
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.1
Release: 3%{?dist}
Group:   Development/Languages
License: MIT
URL:     https://github.com/arangamani/jenkins_api_client
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix_ruby}rubygem(thor) >= 0.16.0
Requires: %{?scl_prefix}rubygem(mixlib-shellout) >= 1.1.0
Requires: %{?scl_prefix}rubygem(terminal-table) >= 1.4.0
Requires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.6.0
Requires: %{?scl_prefix_ror}rubygem(nokogiri) < 2.0.0

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}rubygem(thor) >= 0.16.0
BuildRequires: %{?scl_prefix}rubygem(mixlib-shellout) >= 1.1.0
BuildRequires: %{?scl_prefix}rubygem(terminal-table) >= 1.4.0
BuildRequires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.6.0
BuildRequires: %{?scl_prefix_ror}rubygem(nokogiri) < 2.0.0

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A simple API client for interacting with Jenkins Continuous Integration server.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
       %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENCE
%{_bindir}/jenkinscli
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/scripts
%{gem_instdir}/java_deps
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Gemfile
%{gem_spec}

%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/travis
%exclude %{gem_instdir}/config
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Vagrantfile
%exclude %{gem_instdir}/*.png


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTORS.md

%changelog
* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 1.4.1-3
- rebuild for ror42 scl (jsherril@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 1.4.1-2
- Build rubygem-jenkins_api_client for RH22 SCL (ericdhelms@gmail.com)

* Wed Dec 02 2015 Eric D. Helms <ericdhelms@gmail.com> 1.4.1-1
- new package built with tito

* Thu Nov 05 2015 Ondrej Prazak <oprazak@redhat.com> 1.4.1-1
- initial build
