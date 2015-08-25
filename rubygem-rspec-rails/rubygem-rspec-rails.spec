%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from rspec-rails-2.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rspec-rails
%global rubyabi 1.9.1

Summary: RSpec-2 for Rails-3
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.11.4

# Circular dependency with rubygem-ammeter.
%{!?enable_test: %global enable_test 0}

Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/rspec/rspec-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(activesupport) => 3.0
Requires: %{?scl_prefix_ruby}rubygem(activesupport) < 4
Requires: %{?scl_prefix_ruby}rubygem(actionpack) => 3.0
Requires: %{?scl_prefix_ruby}rubygem(actionpack) < 4
Requires: %{?scl_prefix_ruby}rubygem(railties) => 3.0
Requires: %{?scl_prefix_ruby}rubygem(railties) < 4
Requires: %{?scl_prefix_ruby}rubygem(rspec) => 2.11.0
Requires: %{?scl_prefix_ruby}rubygem(rspec) < 2.12
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%if 0%{enable_test} > 0
BuildRequires: %{?scl_prefix_ruby}rubygem(rspec) => 2.11.0
BuildRequires: %{?scl_prefix_ruby}rubygem(rspec) < 2.12
BuildRequires: %{?scl_prefix_ruby}rubygem(rails) => 3.0
BuildRequires: %{?scl_prefix_ruby}rubygem(rails) < 4
BuildRequires: %{?scl_prefix_ruby}rubygem(sqlite3)
# because ZenTest is optional for rspec-core, but required here
# (have been pulled by other dependencies with Ruby 1.8.7)
BuildRequires: %{?scl_prefix_ruby}rubygem(ZenTest)
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(ammeter)
#BuildRequires: %{?scl_prefix}rubygem(cucumber)
#BuildRequires: %{?scl_prefix}rubygem(aruba)
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
RSpec-2 support for Rails-3


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

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

%if 0%{enable_test} > 0
%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
# Not working. Needs to be investigated.
#cucumber
popd
%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/License.txt
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Capybara.md
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/features
%{gem_instdir}/spec

%changelog
* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 2.11.4-2
- spec2scl -i rubygem-rspec-rails.spec (msuchy@redhat.com)
- rebase to newer rubygem-rspec-rails (msuchy@redhat.com)

* Tue Oct 16 2012 Vít Ondruch <vondruch@redhat.com> - 2.11.4-1
- Update to rspec-rails 2.11.4.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 2.11.0-1
- Update to rspec-rails 2.11.0.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 2.8.1-2
- Tests enabled.

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 2.8.1-1
- Rebuilt for Ruby 1.9.3.
- Update to rspec-rails 2.8.1.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.1-3
- Fixed .gemspec to contain correct dependencies (rhbz#747405).

* Tue Aug 23 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.1-2
- Rebuilt due to the trailing slash bug of rpm-4.9.1

* Tue Jun 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.1-1
- Updated to the rspec-rails 2.6.1

* Mon May 23 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.0-1
- Initial package
