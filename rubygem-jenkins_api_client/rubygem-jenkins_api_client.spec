%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%global gem_name jenkins_api_client

Summary: Jenkins Api client with features focused on automating Job configuration programaticaly
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.1
Release: 1%{?dist}
Group: Developmanet/Languages
License: MIT
URL: https://github.com/arangamani/jenkins_api_client
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby

Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix_ruby}rubygem(mixlib-shellout) >= 1.1.0
Requires: %{?scl_prefix_ruby}rubygem(terminal-table) >= 1.4.0
Requires: %{?scl_prefix_ruby}rubygem(thor) >= 0.16.0
Requires: %{?scl_prefix_ruby}rubygem(nokogiri) >= 1.6.0
Requires: %{?scl_prefix_ruby}rubygem(nokogiri) < 2.0.0

BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}rubygem(mixlib-shellout) >= 1.1.0
BuildRequires: %{?scl_prefix_ruby}rubygem(terminal-table) >= 1.4.0
BuildRequires: %{?scl_prefix_ruby}rubygem(thor) >= 0.16.0
BuildRequires: %{?scl_prefix_ruby}rubygem(nokogiri) >= 1.6.0
BuildRequires: %{?scl_prefix_ruby}rubygem(nokogiri) < 2.0.0

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
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

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
%doc %{gem_instdir}/LICENSE
%{_bindir}/jenkinscli
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/scripts
%{gem_instdir}/java_deps

%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/travis
%exclude %{gem_instdir}/config
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Vagrantfile
%exclude %{gem_instdir}/*.png
%{gem_instdir}/%{gem_name}.gemspec
%{gem_spec}


%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTORS.md

%changelog
* Thu Nov 05 2015 Ondrej Prazak <oprazak@redhat.com> 1.4.1-1
- initial build
