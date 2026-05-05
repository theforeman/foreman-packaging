# template: default
%global gem_name net-http-persistent

Name: rubygem-%{gem_name}
Version: 4.0.8
Release: 1%{?dist}
Summary: Persistent connections using Net::HTTP
License: MIT
URL: https://github.com/drbrain/net-http-persistent
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: rubygem(connection_pool) >= 2.2
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Persistent connections using Net::HTTP with a thread-safe connection pool.
Connections are reused across requests within each thread, avoiding the
overhead of TCP+TLS setup on every request.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_instdir}/Manifest.txt
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/test

%changelog
* Mon May 05 2026 Pablo Mendez Hernandez <pmendezh@redhat.com> - 4.0.8-1
- Add rubygem-net-http-persistent for Candlepin connection pooling (Katello#11726)
