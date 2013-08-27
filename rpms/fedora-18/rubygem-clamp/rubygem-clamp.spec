%global gemname clamp
%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif
%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: a minimal framework for command-line utilities
Name: rubygem-%{gemname}
Version: 0.6.1
Release: 9%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/mdub/clamp
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
%if 0%{?rhel} || 0%{?fedora} < 19
Requires: ruby(abi)
%endif
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
Requires: ruby(rubygems)
%if 0%{?rhel} || 0%{?fedora} < 19
BuildRequires: ruby(abi)
%endif
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Clamp provides an object-model for command-line utilities.  
It handles parsing of command-line options, and generation of usage help.


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
%{geminstdir}/spec
%{geminstdir}/examples
%{geminstdir}/.rspec
%{geminstdir}/Gemfile
%{geminstdir}/Rakefile
%{geminstdir}/%{gemname}.gemspec


%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%exclude %{geminstdir}/.travis.yml
%exclude %{geminstdir}/.gitignore
%exclude %{geminstdir}/.autotest
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%{geminstdir}/README.md
%{geminstdir}/CHANGES.md


%changelog
* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-9
- Final bump

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-8
- Bump one more time

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-7
- Bump version to match up tags

* Mon Aug 26 2013 Sam Kottler <shk@redhat.com> 0.6.1-6
- Use macros provided by rubygems-devel on Fedora (shk@redhat.com)
- gem_instdir (shk@redhat.com)
- gem_instdir (shk@redhat.com)
- Remove rubygems-devel (shk@redhat.com)
- Use rubygems-devel (shk@redhat.com)

* Tue Aug 06 2013 Sam Kottler <shk@redhat.com> 0.6.1-5
- Don't require ruby(abi) on F19+ (shk@redhat.com)

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-4
- Rebuild with the proper whitelist

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-3
- Rebuild

* Thu Aug 01 2013 Sam Kottler <shk@redhat.com> 0.6.1-2
- Import the package into tito

* Wed Jul 31 2013  <shk@linux.com> - 0.6.1-1
- Initial package
