# template: default
%global gem_name http

Name: rubygem-%{gem_name}
Version: 5.2.0
Release: 1%{?dist}
Summary: HTTP should be easy
License: MIT
URL: https://github.com/httprb/http
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

Requires: (rubygem(base64) or ruby-default-gems < 3.4)

%description
An easy-to-use client library for making requests from Ruby. It uses a simple
method chaining system for building requests, similar to Python's Requests.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g base64

# Replace llhttp-ffi with llhttp because it's more performant and easier to
# package. We also don't care about non-MRI Ruby implementations.
# https://github.com/httprb/http/issues/797
%gemspec_remove_dep -g llhttp-ffi "~> 0.5.0"
%gemspec_add_dep -g llhttp "~> 0.6.0"

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.yardopts
%doc %{gem_instdir}/CHANGES_OLD.md
%exclude %{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/SECURITY.md
%{gem_libdir}
%{gem_instdir}/logo.png
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/http.gemspec
%{gem_instdir}/spec

%changelog
* Sun May 11 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 5.2.0-1
- Update to 5.2.0-1

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.3.0-2
- Rebuild for Ruby 2.7

* Wed Apr 24 2019 Moti Asayag <masayag@redhat.com> 3.3.0-1
- Update to 3.3.0
