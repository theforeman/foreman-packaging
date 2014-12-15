%global gemname hammer_cli_foreman_tasks

%if 0%{?rhel} < 7
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Contains the code for showing of the tasks (results and progress) in the Hammer CLI
Name: rubygem-%{gemname}
Version: 0.0.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli-katello
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem

%if !( 0%{?rhel} > 6 || 0%{?fedora} > 18 )
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
Requires: rubygem(hammer_cli_foreman) >= 0.1.1
Requires: rubygem(powerbar)
BuildRequires: ruby(rubygems)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Contains the code for showing of the tasks (results and progress) in the Hammer CLI

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
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md

%changelog
