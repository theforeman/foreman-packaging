%{?scl:%scl_package rubygems-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# check files-sections at the end of this file and

%global gem_name hashie

%define _version 2.0.5
%define _summary Your friendly neighborhood hash toolkit.
%define _url https://github.com/intridea/hashie
%define _license MIT

%define desc Hashie is a small collection of tools that make hashes more powerful. Currently includes Mash (Mocking Hash) and Dash (Discrete Hash)

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   0%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && 0%{!?scl:1})
Requires:  %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}ruby(abi)
%else
Requires:  %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
%endif
Requires:  %{?scl_prefix}rubygems

BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

%description
%{desc}

%package   doc
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:   Documentation for %{pkg_name}

%description doc
This package contains documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%if 0%{?fedora} > 18
%gem_install
%else
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V --local --install-dir .%{gem_dir} --force --rdoc \
    %{gem_name}-%{version}.gem
%{?scl:"}
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/Guardfile
%exclude %{gem_instdir}/spec
%dir %{gem_instdir}
%{gem_instdir}/hashie.gemspec
%{gem_instdir}/Gemfile
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.markdown
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
* Fri Sep 06 2013 Marek Hulan <mhulan@redhat.com> 2.0.5-0
- new package built with tito

