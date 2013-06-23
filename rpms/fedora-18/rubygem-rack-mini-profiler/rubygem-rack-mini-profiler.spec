%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rack-mini-profiler

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.26
Release: 2%{?dist}
Summary: Profiles loading speed for rack applications
Group: Development/Languages
License: ASLv2
URL: http://miniprofiler.com
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}rubygem(rack) >= 1.1.3

BuildRequires: %{?scl_prefix}rubygems-devel 
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygem-activerecord
BuildRequires: %{?scl_prefix}rubygem-rack-test
BuildRequires: %{?scl_prefix}rubygem-rake

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Profiling toolkit for Rack applications with Rails integration. Client Side
profiling, DB profiling and Server profiling.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

# gem install installs into a directory.  We set that to be a local
# directory so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} "}
gem install --local --install-dir ./%{gem_dir} \
            --force --rdoc %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
# this gem uses ./Ruby/lib directory instead of just ./lib/
%{gem_instdir}/Ruby
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Ruby/README.md
%doc %{gem_instdir}/Ruby/CHANGELOG
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Jun 13 2013 Lukas Zapletal <lzap+git@redhat.com> 0.1.26-2
- fixing rubygem-rack-mini-profiler (lzap+git@redhat.com)

* Thu Jun 13 2013 Lukas Zapletal <lzap+git@redhat.com> 0.1.26-1
- new package built with tito

* Thu Jun 13 2013 Lukas Zapletal <lzap+git@redhat.com>
- new package built with tito

* Thu Jun 13 2013 Lukas Zapletal <lzap+git@redhat.com> 0.1.26-1
- new package built with tito

* Thu Jun 13 2013 Lukas Zapletal <lzap+rpm@redhat.com> - 0.1.26-1
- Initial package
