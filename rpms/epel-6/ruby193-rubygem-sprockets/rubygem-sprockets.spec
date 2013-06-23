%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from sprockets-2.4.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sprockets
%global rubyabi 1.9.1

Summary: Rack-based asset packaging system
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.4.5
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://getsprockets.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# to get tests:
# git clone https://github.com/sstephenson/sprockets.git && cd sprockets/
# git checkout v2.4.5 && tar czf sprockets-tests-2.4.5.tgz test/
Source1: sprockets-%{version}-tests.tgz
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hike) => 1.2
Requires: %{?scl_prefix}rubygem(hike) < 2
Requires: %{?scl_prefix}rubygem(multi_json) => 1.0
Requires: %{?scl_prefix}rubygem(multi_json) < 2
Requires: %{?scl_prefix}rubygem(rack) => 1.0
Requires: %{?scl_prefix}rubygem(rack) < 2
Requires: %{?scl_prefix}rubygem(tilt) => 1.1
Requires: %{?scl_prefix}rubygem(tilt) < 2
Conflicts: %{?scl_prefix}rubygem(tilt) = 1.3.0
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(coffee-script)
# these two gems aren't in Fedora yet and are only soft dependencies
# BuildRequires: %{?scl_prefix}rubygem(eco)
# BuildRequires: %{?scl_prefix}rubygem(ejs)
BuildRequires: %{?scl_prefix}rubygem(execjs)
BuildRequires: %{?scl_prefix}rubygem(hike) => 1.2
BuildRequires: %{?scl_prefix}rubygem(hike) < 2
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(multi_json)
BuildRequires: %{?scl_prefix}rubygem(rack) => 1.0
BuildRequires: %{?scl_prefix}rubygem(rack) < 2
BuildRequires: %{?scl_prefix}rubygem(rack-test)
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildRequires: %{?scl_prefix}rubygem(sass)
BuildRequires: %{?scl_prefix}rubygem(therubyracer)
BuildRequires: %{?scl_prefix}rubygem(tilt) => 1.1
BuildRequires: %{?scl_prefix}rubygem(tilt) < 2
BuildConflicts: %{?scl_prefix}rubygem(tilt) = 1.3.0
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.


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
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}
# 4 errors due to missing Gems "eco" and "ejs"
%{?scl:scl enable %{scl} "}
testrb -Ilib test | grep '390 tests, 998 assertions, 0 failures, 4 errors, 0 skips'
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{_bindir}/sprockets
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.5-3
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-2
- Imported from Fedora again.

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-1
- Initial package
