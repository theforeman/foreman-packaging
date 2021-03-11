# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rack

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.2.3
Release: 2%{?dist}
Summary: a modular Ruby webserver interface
Group: Development/Languages
License: MIT
URL: https://rack.github.io/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.3.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.3.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 2.0.6

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see https://rack.github.io/.


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
rm -rf .%{gem_dir}/gems/%{gem_name}-%{version}/test
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rackup
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_instdir}/contrib
%{gem_instdir}/example
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/CONTRIBUTING.md
%exclude %{gem_instdir}/SPEC.rdoc
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/rack.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.3-2
- Rebuild against rh-ruby27

* Thu Jun 25 2020 Tomer Brisker <tbrisker@gmail.com> - 2.2.3-1
- Release rubygem-rack 2.2.3

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 2.2.2-1
- Update to 2.2.2

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.1-1
- Release rubygem-rack 2.1.1

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.6-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.6-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.0.6-2
- Bump for moving over to foreman-packaging

* Mon Mar 11 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.0.6-1
- Release tfm-ror52-rubygem-rack 2.0.6

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.5-2
- rebuilt

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.5-1
- Initial package
