# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name loofah

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.4.0
Release: 2%{?dist}
Summary: Loofah is a general library for manipulating and transforming HTML/XML documents and fragments
Group: Development/Languages
License: MIT
URL: https://github.com/flavorjones/loofah
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.5.9
Requires: %{?scl_prefix}rubygem(crass) >= 1.0.2
Requires: %{?scl_prefix}rubygem(crass) < 1.1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 2.2.2

%description
Loofah is a general library for manipulating and transforming HTML/XML
documents and fragments. It's built on top of Nokogiri and libxml2, so
it's fast and has a nice API.
Loofah excels at HTML sanitization (XSS prevention). It includes some
nice HTML sanitizers, which are based on HTML5lib's whitelist, so it
most likely won't make your codes less secure. (These statements have
not been evaluated by Netexperts.)
ActiveRecord extensions for sanitization are available in the
[`loofah-activerecord`
gem](https://github.com/flavorjones/loofah-activerecord).


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gemtest
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_instdir}/Manifest.txt
%{gem_instdir}/SECURITY.md
%{gem_instdir}/benchmark
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.4.0-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.0-1
- Release rubygem-loofah 2.4.0

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-5
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-4
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.2.2-3
- Bump for moving over to foreman-packaging

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-2
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-1
- Initial package
