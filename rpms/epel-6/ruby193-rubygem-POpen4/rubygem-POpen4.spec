%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from POpen4-0.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name POpen4
%global rubyabi 1.9.1

Summary: Open4 cross-platform
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.4
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2 or Ruby
URL: http://github.com/pka/popen4
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(Platform) >= 0.4.0
Requires: %{?scl_prefix}rubygem(open4)
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(Platform) >= 0.4.0
BuildRequires: %{?scl_prefix}rubygem(open4)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
POpen4 provides the Rubyist a single API across platforms for executing
a command in a child process with handles on stdout, stderr, stdin streams
as well as access to the process ID and exit status. It does very little other
than to provide an easy way to use either Ara Howard’s Open4 library
or the win32-popen3 library by Park Heesob and Daniel Berger depending on your
platform and without having to code around the slight differences
in their APIs.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %{scl} "}
testrb tests/*_test.rb
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/lib
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/VERSION
%{gem_instdir}/tests

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.4-3
- BR rubygem(minitest) (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.4-2
- new package built with tito

* Sat Jun 30 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.4-1
- new package built with tito

* Mon Jun 13 2011 Vít Ondruch <vondruch@redhat.com> - 0.1.4-1
- Initial package
