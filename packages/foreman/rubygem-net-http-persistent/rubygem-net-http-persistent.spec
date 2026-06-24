# template: default
%global gem_name net-http-persistent

Name: rubygem-%{gem_name}
Version: 4.0.8
Release: 1%{?dist}
Summary: An HTTP persistent connection library
License: MIT
URL: https://github.com/drbrain/net-http-persistent
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 3.0
Requires: rubygem(connection_pool) >= 2.2
BuildRequires: ruby >= 3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Manages persistent connections using Net::HTTP including a thread pool
for connecting to multiple hosts. Using persistent HTTP connections can
dramatically increase the speed of HTTP requests. Connections are kept
alive across requests and threads.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.rdoc
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc

%changelog
* Wed May 27 2026 Pablo Mendez Hernandez <pablomh@redhat.com> 4.0.8-1
- New package: net-http-persistent for persistent HTTP connection pooling
- Required by faraday-net_http_persistent 2.x
