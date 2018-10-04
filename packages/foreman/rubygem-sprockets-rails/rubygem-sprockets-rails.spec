%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sprockets-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2.0
Release: 3%{?dist}
Summary: Sprockets Rails integration
Group: Development/Languages
License: MIT
URL: https://github.com/rails/sprockets-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9.3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(sprockets) >= 3.0.0
Requires: %{?scl_prefix_ror}rubygem(actionpack) >= 4.0
Requires: %{?scl_prefix_ror}rubygem(activesupport) >= 4.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9.3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Sprockets Rails integration.


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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.2.0-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Jul 27 2017 Eric D. Helms <ericdhelms@gmail.com> 3.2.0-1
- Update rubygem-sprockets-rails to 3.2.0 (me@daniellobato.me)
- Import sprockets-rails for F24, 2.3.3 is required (dominic@cleal.org)
- Remove packages now in sclo-ror42 (dominic@cleal.org)

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
