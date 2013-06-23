%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from logging-1.4.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name logging

%global rubyabi 1.9.1

Summary: A flexible and extendable logging library for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.1
Release: 5%{?dist}
Group: Development/Languages
License: Ruby or BSD
URL: http://rubygems.org/gems/logging
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygem(little-plugger) >= 1.1.2
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(little-plugger) >= 1.1.2
BuildRequires: %{?scl_prefix}rubygem(flexmock) >= 0.9.0
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Logging is a flexible logging library for use in Ruby programs based on the
design of Java's log4j library. It features a hierarchical logging system,
custom level names, multiple output destinations per log event, custom
formatting, and more.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.


%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
testrb test || true
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/data
# contains licensing information
%doc %{gem_instdir}/README.rdoc
# version.txt is needed for runtime
%{gem_instdir}/version.txt
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/examples
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt

%changelog
* Tue Mar 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.8.1-5
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.6.2-4
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.6.2-3
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.2-1
- Rebuilt for Ruby 1.9.3.
- Updated to version 1.6.2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.1-1
- New version.
- Removed unnecessary defattr macro in files section.
- Removed unnecessary clean section.
- Replaced define macros with more appropriate global.
- Moved gem install to the prep section.
- Added check section to run tests.
- BuildRequires now contain rubygem(little-plugger) and rubygem(flexmock) due to running tests.
- Introduced doc subpackage.

* Wed Mar 16 2011 Chris Lalancette <clalance@redhat.com> - 1.4.3-1
- Initial package
