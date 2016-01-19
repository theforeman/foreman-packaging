%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from sprockets-rails-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sprockets-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.3
Release: 1%{?dist}
Summary: Sprockets Rails integration
Group: Development/Languages
License: MIT
URL: https://github.com/rails/sprockets-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Get the tests
# git clone https://github.com/rails/sprockets-rails.git && cd sprockets-rails/
# git checkout v2.3.3
# tar czvf sprockets-rails-2.3.3-tests.tgz test/
Source2: sprockets-rails-%{version}-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(sprockets) >= 2.8
Requires: %{?scl_prefix}rubygem(sprockets) < 4
Requires: %{?scl_prefix_ror}rubygem(actionpack) >= 3.0
Requires: %{?scl_prefix_ror}rubygem(activesupport) >= 3.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygem(rake)
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ror}rubygem(railties)
BuildRequires: %{?scl_prefix}rubygem(sprockets)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %scl - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %scl - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %scl - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Move the tests into place
tar xzvf %{SOURCE2}

%{?scl:scl enable %scl - << \EOF}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
%{?scl:EOF}
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jan 19 2016 Dominic Cleal <dcleal@redhat.com> 2.3.3-1
- Update sprockets-rails to 2.3.3 for Patternfly (elobatocs@gmail.com)

* Thu Jan 29 2015 Vít Ondruch <vondruch@redhat.com> - 2.2.4-2
- Drop the boostrap and depend on railties instead of rails.

* Wed Jan 28 2015 Vít Ondruch <vondruch@redhat.com> - 2.2.4-1
- Update to sprockets-rails 2.2.4.

* Mon Jan 26 2015 Josef Stribny <jstribny@redhat.com> - 2.1.3-1
- Update to 2.1.3

* Thu Aug 08 2013 Josef Stribny <jstribny@redhat.com> - 2.0.0-3
- Enable tests

* Wed Jul 31 2013 Josef Stribny <jstribny@redhat.com> - 2.0.0-2
- Disable tests for now due to broken deps in Rails

* Mon Jul 22 2013 Josef Stribny <jstribny@redhat.com> - 2.0.0-1
- Initial package
