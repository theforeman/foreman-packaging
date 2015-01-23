%global gem_name foreman_scap_client
%global config_dir %{_sysconfdir}/%{gem_name}

Name: rubygem-%{gem_name}
Version: 0.0.1
Release: 2%{?dist}
Summary: Client script that runs OpenSCAP scan and uploads the result to foreman proxy
Group: Development/Languages
License: GPLv3
URL: https://github.com/openscap/foreman_scap_client
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
%if 0%{?rhel} >= 5 && 0%{?rhel} <= 6
BuildRequires: ruby(abi) >= %{rubyabi}
Requires: ruby(abi) >= %{rubyabi}
Requires: openscap-utils
%else
BuildRequires: ruby(release)
Requires: ruby(release)
Requires: openscap-scanner
%endif
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Client script that runs OpenSCAP scan and uploads the result to foreman proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# create config directory
mkdir -p %{buildroot}%{config_dir}

%files
%dir %{gem_instdir}
%{_bindir}/foreman_scap_client
%{config_dir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/config

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jan 13 2015 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-2
- allow build for rhel6

* Tue Jan 13 2015 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-1
- Initial package
