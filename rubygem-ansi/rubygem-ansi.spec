%{?scl:%scl_package rubygems-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ansi

%define _version 1.4.3
%define _summary "The ANSI project is a superlative collection of ANSI escape code" 
%define _url "https://github.com/rubyworks/ansi"
%define _license FreeBSD

%define desc The ANSI project is a superlative collection of ANSI escape code related libraries enabling ANSI colorization and stylization of console output. Byte for byte ANSI is the best ANSI code library available for the Ruby programming language.

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
Release:   1%{?dist}  
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
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/.yardopts
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/Config.rb
%exclude %{gem_instdir}/.ruby
%doc %{gem_instdir}/COPYING.rdoc
%doc %{gem_instdir}/DEMO.rdoc
%doc %{gem_instdir}/HISTORY.rdoc
%doc %{gem_instdir}/README.rdoc

%files doc
%doc %{gem_instdir}/demo
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
* Tue Oct 08 2013 Ivan Necas <inecas@redhat.com> 1.4.3-1
- Rebuild for katello

* Fri Sep 06 2013 Marek Hulan <mhulan@redhat.com> 1.4.3-0
- new package built with tito

