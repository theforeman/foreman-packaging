%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name popen4

Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        0.1.2
Release:        3%{?dist}
Summary:        Open4 cross-platform
Group:          Development/Languages
License:        Ruby
URL:            http://github.com/shairontoledo/popen4
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires:       %{?scl_prefix}ruby(release)
%else
Requires:       %{?scl_prefix}ruby(abi)
%endif
Requires:       %{?scl_prefix}ruby(rubygems)
Requires:       %{?scl_prefix}ruby
Requires:       %{?scl_prefix}rubygem(Platform) >= 0.4.0
Requires:       %{?scl_prefix}rubygem(open4) >= 0.4.0

%if 0%{?fedora} > 18
BuildRequires:  %{?scl_prefix}ruby(release)
%else
BuildRequires:  %{?scl_prefix}ruby(abi)
%endif
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildRequires:  %{?scl_prefix}ruby
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
POpen4 provides the Rubyist a single API across platforms for executing a
command in a child process with handles on stdout, stderr, stdin streams as
well as access to the process ID and exit status.

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
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/tests

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc

%changelog
* Tue Aug 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.1.2-3
- rubygem-popen4 rhel6 changes (lzap+git@redhat.com)

* Tue Aug 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.1.2-2
- new package built with tito

* Tue Aug 06 2013 Lukáš Zapletal <lzap+rpm@redhat.com> - 0.1.2-1
- Initial package
