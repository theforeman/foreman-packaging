%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
# Generated from multi_json-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name multi_json

%global rubyabi 1.9.1

Summary: A gem to provide swappable JSON backends
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.6
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/intridea/multi_json
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) >= 1.3.6
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel >= 1.3.6
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(json)
BuildRequires: %{?scl_prefix}rubygem(json_pure)
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# OkJson is allowed to be bundled:
# https://fedorahosted.org/fpc/ticket/113
Provides: bundled(%{?scl_prefix}okjson) = 20110719

%description
A gem to provide swappable JSON backends utilizing Yajl::Ruby, the JSON gem,
JSON pure, or a vendored version of okjson.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl:%scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove useless shebang.
sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{gem_instdir}/Rakefile

%check
pushd ./%{gem_instdir}
# simplecov gem is Ruby 1.9 only and not available in Fedora,
# so remove its usage
sed -i '9,14d' spec/helper.rb

# 1 test case fails (missing oj) and 22 are pending (missing yajl-ruby)
%{?scl:scl enable %scl - << \EOF}
rspec spec/ | grep '63 examples, 1 failure, 22 pending'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec


%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.6-2
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.6-1
- Updated to Multi_Json 1.3.6.
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-1
- Rebuilt for scl.
- Updated to 1.2.0.

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.3-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-3
- Removed useless shebang.

* Fri Nov 11 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-2
- Review fixes.

* Fri Jul 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.3-1
- Initial package
