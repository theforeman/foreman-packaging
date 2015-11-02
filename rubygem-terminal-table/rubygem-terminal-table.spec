%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name terminal-table

Summary: Simple, feature rich ascii table generation library
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.5.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: https://github.com/tj/terminal-table
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
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Terminal Table is a fast and simple, yet feature rich ASCII table generator written in Ruby.

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
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/lib
%{gem_instdir}/terminal-table.gemspec
%{gem_spec}

%exclude %{gem_cache}
%exclude %{gem_instdir}/examples
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Todo.rdoc
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Manifest

%files doc
%doc %{gem_instdir}/History.rdoc

%changelog
* Mon Nov 2 2015 Ondrej Prazak <oprazak@redhat.com> 1.5.2-1
- initial build
