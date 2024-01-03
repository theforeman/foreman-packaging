# template: default
%global gem_name mail

Name: rubygem-%{gem_name}
Version: 2.8.1
Release: 2%{?dist}
Summary: Mail provides a nice Ruby DSL for making, sending and reading emails
License: MIT
URL: https://github.com/mikel/mail
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

# Allow to consume net-smtp/net-imap/net-pop as a default gem
Requires: (rubygem(net-imap) or ruby-default-gems < 3.1)
Requires: (rubygem(net-pop) or ruby-default-gems < 3.1)
Requires: (rubygem(net-smtp) or ruby-default-gems < 3.1)

%description
A really Ruby Mail handler.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

# On EL8 rubygem-net-smtp/imap/pop are bundled into ruby-libs package and
# auto-generated dependencies will break dependency resolution
%gemspec_remove_dep -g net-smtp
%gemspec_remove_dep -g net-imap
%gemspec_remove_dep -g net-pop

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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 03 2024 Evgeni Golov - 2.8.1-2
- Correct deps for Ruby 3.0 bundled gems

* Sun Feb 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.8.1-1
- Update to 2.8.1

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.8.0.1-1
- Update to 2.8.0.1

* Tue Jan 03 2023 Evgeni Golov - 2.8.0-2
- Correct auto-requires generation to allow bundled gems in Ruby 2.7

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.8.0-1
- Update to 2.8.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.7.1-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.7.1-1
- Release rubygem-mail 2.7.1

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.7.0-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.7.0-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.7.0-2
- Bump for moving over to foreman-packaging

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.7.0-1
- Initial package
