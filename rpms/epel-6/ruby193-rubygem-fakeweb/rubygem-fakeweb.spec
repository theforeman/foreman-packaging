%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from fakeweb-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fakeweb

Summary: A tool for faking responses to HTTP requests
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.0
Release: 9%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/chrisk/fakeweb
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: patch_out_samuel.patch
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems-devel
# The following BR are there for %%check
BuildRequires: %{?scl_prefix}rubygem(mocha)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(right_http_connection)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
FakeWeb is a helper for faking web requests in Ruby. It works at a global
level, without modifying code or writing extensive stubs.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.


%prep
mkdir -p ./%{gem_dir}
%{?scl:scl enable %scl "}
gem install \
        --local \
        --install-dir .%{gem_dir} \
        --force \
        --rdoc \
        -V \
%{SOURCE0}
%{?scl:"}

pushd ./%{gem_instdir}/test
%patch0 -p0
popd

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Don't vendor all your gems...srsly
rm -rf %{buildroot}%{gem_instdir}/test/vendor/right_http*
rm -rf %{buildroot}%{gem_instdir}/test/vendor/samuel*

# rpmlint cleanup
rm -f %{buildroot}%{gem_instdir}/test/vendor/samuel-0.2.1/.gitignore
rm -f %{buildroot}%{gem_instdir}/.autotest
rm -f %{buildroot}%{gem_instdir}/.gitignore
# This file is also in specifications
rm -f %{buildroot}%{gem_instdir}/*.gemspec


%check
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %scl "}
testrb -Ilib test
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/test
%{gem_instdir}/Rakefile

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.0-9
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.0-8
- Specfile cleanup

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.0-7
- Rebuilt for scl.

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.0-6
- Rebuilt for Ruby 1.9.3.

* Sun Jan 08 2012 Michael Stahnke <mastahnke@gmail.com> - 1.3.0-5
- Bug bz#715907 FTBFS on rawhide

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 17 2010 Michael Stahnke <stahnma@fedoraproject.org> - 1.3.0-3
- A few minor fixes in spec per review

* Mon Sep 13 2010 Michael Stahnke <stahnma@fedoraproject.org> - 1.3.0-2
- Removing 'vendored' items

* Sun Sep 12 2010 Michael Stahnke <stahnma@fedoraproject.org> - 1.3.0-1
- Initial package
