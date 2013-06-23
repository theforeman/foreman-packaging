%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from sass-rails-3.2.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sass-rails
%global rubyabi 1.9.1

Summary: Sass adapter for the Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2.5
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/rails/sass-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(sass) >= 3.1.10
Requires: %{?scl_prefix}rubygem(railties) => 3.2.0
Requires: %{?scl_prefix}rubygem(railties) < 3.3
Requires: %{?scl_prefix}rubygem(tilt) => 1.3
Requires: %{?scl_prefix}rubygem(tilt) < 2
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
# BuildRequires: %{?scl_prefix}rubygem(minitest)
# BuildRequires: %{?scl_prefix}rubygem(mocha)
# BuildRequires: %{?scl_prefix}rubygem(sass) >= 3.1.10
# BuildRequires: %{?scl_prefix}rubygem(railties) => 3.2.0
# BuildRequires: %{?scl_prefix}rubygem(railties) < 3.3
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Sass adapter for the Rails asset pipeline.


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
pushd .%{gem_instdir}
# Test suite is relying on git and Bundler especially so heavily, that all my
# attempts to execute the test suite failed so far :/
# https://github.com/rails/sass-rails/issues/114
# https://github.com/rails/sass-rails/issues/115

# Get rid of Bundler
# sed -i "/require 'bundler\/setup'/d" test/test_helper.rb
# sed -i "15,26d" test/test_helper.rb
# sed -i "1,4d" test/support/sass_rails_test_case.rb

# sed -i "s/bundle install/bundle install --local/" test/support/sass_rails_test_case.rb

# sfl is not needed for Ruby 1.9.
# https://github.com/rails/sass-rails/pull/113
# sed -i "/require 'sfl'/d" test/test_helper.rb

# ruby -I.:lib:test -e 'Dir.glob("test/**/*_test.rb").each {|t| require t}'
popd


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/sass-rails.gemspec
# Test suite can't be executed and rpmlint complains a lot about dot files:
# https://github.com/rails/sass-rails/issues/116
%exclude %{gem_instdir}/test

%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 3.2.5-3
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.5-2
- Imported from Fedora again.
- Specfile cleanup

* Mon Jul 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.5-1
- Initial package
