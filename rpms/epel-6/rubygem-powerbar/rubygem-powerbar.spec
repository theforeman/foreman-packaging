
%{?scl:%scl_package rubygems-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# check files-sections at the end of this file and 

%global gem_name powerbar

%define _version 1.0.11
%define _summary "The last progressbar-library you'll ever need" 
%define _url "https://github.com/busyloop/powerbar"
%define _license MIT

%define desc The last progressbar-library you'll ever need

Requires: %{?scl_prefix}rubygem(ansi) >= 1.4.0
Requires: %{?scl_prefix}rubygem(hashie) >= 1.1.0

%if 0%{?rhel} == 6 || 0%{?fedora} < 17
%if "%{?scl}" == "ruby193"
%define rubyabi 1.9.1
%else
%define rubyabi 1.8
%endif
%else
%define rubyabi 1.9.1
%endif

%if 0%{?rhel} == 6 &&  "%{?scl}" != "ruby193"
%global gem_dir %(ruby -rubygems -e 'puts Gem.dir' 2>/dev/null)
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_dir}/gems/%{gem_name}-%{version}/lib
%endif

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

%if 0%{?fedora} > 18
Requires:  %{?scl_prefix}ruby(release)
%else 
Requires:  %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires:  %{?scl_prefix}rubygems

%if 0%{?fedora} || "%{?scl}" == "ruby193"
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
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
%exclude %dir %{gem_instdir}/ass
%exclude %dir %{gem_instdir}/ass/screenshot.png
%exclude %{gem_cache}

%dir %{gem_instdir}
%dir %{gem_instdir}/Gemfile
%dir %{gem_instdir}/Rakefile
%dir %{gem_instdir}/powerbar.gemspec
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/bin
%{gem_dir}/bin/powerbar-demo

%files doc
%doc %{gem_instdir}/README.rdoc
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
* Fri Sep 06 2013 Marek Hulan <mhulan@redhat.com> 1.0.11-0
- new package built with tito

