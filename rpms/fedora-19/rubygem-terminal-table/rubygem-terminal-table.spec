%global gemname terminal-table

%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif
%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Simple, feature rich ascii table generation library
Name: rubygem-%{gemname}
Version: 1.4.5
Release: 8%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/visionmedia/terminal-table
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
%if 0%{?rhel} || 0%{?fedora} < 19
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
%if 0%{?rhel} || 0%{?fedora} < 19
BuildRequires: ruby(abi)
%endif
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Simple, feature rich ascii table generation library


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

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec
%{geminstdir}/tasks
%{geminstdir}/spec
%{geminstdir}/Rakefile
%{geminstdir}/Manifest
%exclude %{geminstdir}/%{gemname}.gemspec


%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/History.rdoc
%doc %{geminstdir}/Todo.rdoc
%doc %{geminstdir}/examples

%changelog
* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 1.4.5-8
- Final version bump

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 1.4.5-7
- Bump version

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 1.4.5-6
- Use macros provided by rubygems-devel on Fedora (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 1.4.5-5
- Add more missing %% (shk@redhat.com)
- Remove ruby(abi) for f19 (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 1.4.5-4
- Remove abi version requirement (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 1.4.5-3
- Removed abi version for hammer_cli deps (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 1.4.5-2
- Initial tito build

* Wed Jul 31 2013  <shk@linux.com> - 1.4.5-1
- Initial package
