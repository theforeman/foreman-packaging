%global gemname clamp

# Koji is not cooperating and sets the gem_dir differently on each build
# so this nasty, disgusting hack fixes that.
# TODO: make this less horrid
%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%else
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%endif

%global gem_instdir %{gem_dir}/gems/%{gemname}-%{version}


Summary: a minimal framework for command-line utilities
Name: rubygem-%{gemname}
Version: 0.6.1
Release: 7%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/mdub/clamp
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
%if 0%{?rhel} || 0%{?fedora} < 19
Requires: ruby(abi)
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
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/spec
%{gem_instdir}/examples
%{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gemname}.gemspec


%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.autotest
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%{gem_instdir}/README.md
%{gem_instdir}/CHANGES.md


%changelog
* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 0.6.1-7
- Use a horrible hack to fix koji's brokenness (shk@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 0.6.1-6
- Maybe this'll work (shk@redhat.com)

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
