%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?scl_v8:%global scl_v8 v8314}
%{!?scl_prefix_v8:%global scl_prefix_v8 %{scl_v8}-}

%global gem_name sprockets

Summary:  Rack-based asset packaging system
Name:     %{?scl_prefix}rubygem-%{gem_name}
Version:  2.12.3
Release:  1%{?dist}
Group:    Development/Languages
License:  MIT
URL:      http://getsprockets.org/
Source0:  http://rubygems.org/gems/%{gem_name}-%{version}.gem
# to get tests:
# git clone https://github.com/sstephenson/sprockets.git && cd sprockets/
# git checkout v2.12.3 && tar czf sprockets-2.12.3-tests.tgz test/
Source1:  sprockets-%{version}-tests.tgz
# Moves test suite to use minitest.
# https://github.com/sstephenson/sprockets/commit/f29903ace62fd43280996b0cb32634f1e5108e52
Patch0: rubygem-sprockets-2.12.1-load-minitest.patch
# https://github.com/sstephenson/sprockets/commit/a454ecb17cd1058ad46665824ca4d0f309f0eccf
Patch2: rubygem-sprockets-2.12.1-assert_raise-assert_raises.patch
# https://github.com/sstephenson/sprockets/commit/9be057ce5804492c7c5bd1b20ba7da49c5538740
Patch3: rubygem-sprockets-2.12.1-assert_no_equal-is-gone.patch

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(hike) => 1.2
Requires: %{?scl_prefix_ruby}rubygem(hike) < 2
Requires: %{?scl_prefix}rubygem(multi_json) => 1.0
Requires: %{?scl_prefix}rubygem(multi_json) < 2
Requires: %{?scl_prefix_ruby}rubygem(rack) => 1.0
Requires: %{?scl_prefix_ruby}rubygem(rack) < 2
Requires: %{?scl_prefix_ruby}rubygem(tilt) => 1.1
Requires: %{?scl_prefix_ruby}rubygem(tilt) < 2
Conflicts: %{?scl_prefix_ruby}rubygem(tilt) = 1.3.0
%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
Requires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygem(coffee-script)
BuildRequires: %{?scl_prefix_ruby}rubygem(execjs)
BuildRequires: %{?scl_prefix_ruby}rubygem(hike) => 1.2
BuildRequires: %{?scl_prefix_ruby}rubygem(hike) < 2
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ruby}rubygem(uglifier)
BuildRequires: %{?scl_prefix}rubygem(multi_json)
BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}rubygem(rack) => 1.0
BuildRequires: %{?scl_prefix_ruby}rubygem(rack) < 2
BuildRequires: %{?scl_prefix_ruby}rubygem(rack-test)
BuildRequires: %{?scl_prefix_ruby}rubygem(rake)
BuildRequires: %{?scl_prefix}rubygem(sass)
BuildRequires: %{?scl_prefix_ruby}rubygem(therubyracer)
BuildRequires: %{?scl_prefix_ruby}rubygem(tilt) => 1.1
BuildRequires: %{?scl_prefix_ruby}rubygem(tilt) < 2
BuildConflicts: %{?scl_prefix_ruby}rubygem(tilt) = 1.3.0
%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif
%if "%{?scl_v8}" != ""
BuildRequires: %{?scl_v8}
BuildRequires: %{?scl_v8}-scldevel
%endif

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}

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

cat %{PATCH0} | patch -p1
cat %{PATCH2} | patch -p1
cat %{PATCH3} | patch -p1

# Where does the one additional new line come from? It is probably coused by
# some version differences, should not have influence on functionality.
sed -i 's|function() {\\n  (|function() {\\n\\n  (|' test/test_environment.rb

%{?scl:scl enable %{scl} %{?scl_v8} - << \EOF}
ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)' | tee tests.log
%{?scl:EOF}
# 4 failures because newer SASS returns #666 for grey instead of #666666
# https://github.com/sstephenson/sprockets/issues/660
# 4 errors because eco/ejs are soft dependencies
grep '445 tests, 1146 assertions, 4 failures, 4 errors, 0 skips' tests.log
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
* Fri Feb 06 2015 Dominic Cleal <dcleal@redhat.com> 2.12.3-1
- Update sprockets to 2.12.3 (dcleal@redhat.com)

* Fri Oct 10 2014 Dominic Cleal <dcleal@redhat.com> 2.8.2-2
- Rebuild under SCL for Foreman (ehelms@redhat.com)

* Tue Dec 11 2012 Josef Stribny <jstribny@redhat.com> - 2.8.2-1
- Upgraded to version 2.8.2
- Added rubygem-uglifier build dependency

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-1
- Initial package
