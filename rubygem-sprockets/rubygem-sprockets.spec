%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sprockets

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.5.2
Release: 1%{?dist}
Summary: Rack-based asset packaging system
Group: Development/Languages
License: MIT
URL: https://github.com/rails/sprockets
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/sprockets.git && cd sprockets/
# git checkout v3.5.2 && tar czf sprockets-3.5.2-tests.tgz test/
Source1: sprockets-%{version}-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ror}rubygem(rack) > 1
Requires: %{?scl_prefix_ror}rubygem(rack) < 3
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 1
Requires: %{?scl_prefix}rubygem(concurrent-ruby) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9.3
BuildRequires: %{?scl_prefix_ruby}rubygem(rake)
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ror}rubygem(therubyracer)
BuildRequires: %{?scl_prefix_ror}rubygem(uglifier)
BuildRequires: %{?scl_prefix_ror}rubygem(coffee-script)
BuildRequires: %{?scl_prefix_ror}rubygem(execjs)
BuildRequires: %{?scl_prefix_ror}rubygem(rack-test)
BuildRequires: %{?scl_prefix}rubygem(sass)
BuildRequires: %{?scl_prefix}rubygem(ejs)
BuildRequires: %{?scl_prefix}rubygem(nokogiri)
BuildRequires: %{?scl_prefix}rubygem(concurrent-ruby)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.

%package doc
Summary:    Documentation for %{pkg_name}
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch:  noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite

%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}

# We don't have rubygem(closure-compiler) yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=725733
mv test/test_closure_compressor.rb{,.disabled}
mv lib/sprockets/autoload/closure.rb{,.disabled}
sed -i '/:Closure/ s/^/#/' lib/sprockets/autoload.rb

# We don't have rubygem(eco) yet.
mv test/test_eco_processor.rb{,.disabled}
mv lib/sprockets/autoload/eco.rb{,.disabled}
sed -i '/:Eco/ s/^/#/' lib/sprockets/autoload.rb
sed -i '/test "eco templates" do/,/^  end/ s/^/#/' test/test_environment.rb

# We don't have rubygem(yui-compressor) yet.
# https://bugzilla.redhat.com/show_bug.cgi?id=725768
mv test/test_yui_compressor.rb{,.disabled}
mv lib/sprockets/autoload/yui.rb{,.disabled}
sed -i '/:YUI/ s/^/#/' lib/sprockets/autoload.rb

# Required by TestPathUtils#test_find_upwards test.
touch Gemfile

%{?scl:scl enable %{scl} %{scl_v8} - << \EOF}
RUBYOPT=-Ilib:test ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)' \
  | grep "777 runs, 338[3-5] assertions, 1 failures, 0 errors, [1-2] skips"
# Skipped tests are different on fc21 versus el6 and el7
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{_bindir}/sprockets
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Thu Jan 07 2016 Daniel Lobato <elobatocs@gmail.com> 3.5.2-1
- Update to 3.5.2

* Fri Dec 18 2015 Dominic Cleal <dcleal@redhat.com> 3.2.0-3
- Fix missing provides rubygem

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Vít Ondruch <vondruch@redhat.com> - 3.2.0-1
- Update to Sprockets 3.2.0.

* Tue Nov 18 2014 Josef Stribny <jstribny@redhat.com> - 2.12.3-1
- Update to 2.12.3

* Mon Aug 18 2014 Josef Strzibny <jstribny@redhat.com> - 2.12.1-3
- Fix FTBFS: ExecJS changed the exception names

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 2.12.1-2
- Filter tilt requires.

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 2.12.1-1
- Update to sprockets 2.12.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 2.8.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Josef Stribny <jstribny@redhat.com> - 2.8.2-1
- Upgraded to version 2.8.2
- Added rubygem-uglifier build dependency

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-1
- Initial package
