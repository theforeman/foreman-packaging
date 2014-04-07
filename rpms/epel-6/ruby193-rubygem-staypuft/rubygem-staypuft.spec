%{?scl:%scl_package rubygems-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name staypuft

%define _version 0.0.3
%define _summary "OpenStack Foreman Installer" 
%define _url "https://github.com/theforeman/staypuft"
%define _license GPLv3

%define desc OpenStack Foreman Installer

Requires: %{?scl_prefix}rubygem(foreman-discovery)
Requires: %{?scl_prefix}rubygem(foreman-tasks)
Requires: %{?scl_prefix}rubygem(wicked)
Requires: %{?scl_prefix}rubygem(dynflow) >= 0.6.1

%if 0%{?rhel} == 6 || 0%{?fedora} < 17
%if "%{?scl}" == "ruby193"
%define rubyabi 1.9.1
%else
%define rubyabi 1.8
%endif
%else
%define rubyabi 1.9.1
%endif

%global foreman_bundlerd_dir /usr/share/foreman/bundler.d

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

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/staypuft.rb
gem 'staypuft'
GEMFILE

%files 
%dir %{gem_instdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/config
%{gem_instdir}/Rakefile
%{foreman_bundlerd_dir}/staypuft.rb
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_instdir}/test
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri

%changelog
* Mon Apr 07 2014 Marek Hulan <mhulan@redhat.com> 0.0.3-1
- Update staypuft to 0.0.3 (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-4
- Hopefully last hack staypuft 0.0.2 version (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-3
- Another hacked version of staypuft (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-2
- Hacked staypuft version without oj dependency (mhulan@redhat.com)

* Fri Apr 04 2014 Marek Hulan <mhulan@redhat.com> 0.0.2-1
- Update staypuft to 0.0.2 (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.1-2
- Integrate staypuft into foreman (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 0.0.1-1
- new package built with tito


