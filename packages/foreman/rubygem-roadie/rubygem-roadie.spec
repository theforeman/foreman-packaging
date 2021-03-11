%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name roadie

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.4.0
Release: 4%{?dist}
Summary: Making HTML emails comfortable for the Ruby rockstars
Group: Development/Languages
License: MIT
URL: https://github.com/Mange/roadie
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(css_parser) >= 1.4.0
Requires: %{?scl_prefix}rubygem(css_parser) < 2.0.0
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.5.0
Requires: %{?scl_prefix}rubygem(nokogiri) < 2.0.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Roadie tries to make sending HTML emails a little less painful by
inlining stylesheets and rewriting relative URLs for you inside your
emails.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}


%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}/%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/autotest

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.4.0-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.0-2
- Update spec to remove the ror scl

* Fri Feb 15 2019 Michael Moll <mmoll@mmoll.at> - 3.4.0-1
- Bump rubygem-roadie to 3.4.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.2.2-1
- Bump rubygem-roadie to 3.2.2 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Jan 09 2017 Dominic Cleal <dominic@cleal.org> 3.2.1-1
- Update roadie to 3.2.1 (dominic@cleal.org)

* Thu Jan 05 2017 Dominic Cleal <dominic@cleal.org> 3.2.0-1
- Update roadie to 3.2.0 (dominic@cleal.org)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 3.1.1-1
- new package built with tito

