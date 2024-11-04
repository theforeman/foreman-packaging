# template: default
%global gem_name builder

Name: rubygem-%{gem_name}
Version: 3.3.0
Release: 1%{?dist}
Summary: Builders for MarkUp
License: MIT
URL: https://github.com/rails/builder
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Builder provides a number of builder objects that make creating structured
data
simple to do.  Currently the following builder objects are supported:
* XML Markup
* XML Events.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

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
%doc %{gem_instdir}/CHANGES
%license %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/builder.blurb
%{gem_libdir}
%{gem_instdir}/rakelib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/builder.gemspec
%doc %{gem_instdir}/doc
%{gem_instdir}/test

%changelog
* Thu Jul 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.0-1
- Update to 3.3.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.2.4-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.4-1
- Release rubygem-builder 3.2.4

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.3-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.2.3-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 3.2.3-2
- Bump for moving over to foreman-packaging

* Thu Jul 19 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.3-1
- Initial package
