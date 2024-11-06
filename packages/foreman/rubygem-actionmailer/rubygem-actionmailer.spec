# template: default
%global gem_name actionmailer

Name: rubygem-%{gem_name}
Version: 7.0.8.6
Release: 1%{?dist}
Summary: Email composition and delivery framework (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

# Allow to consume net-smtp/net-imap/net-pop as a default gem
Requires: (rubygem(net-imap) or ruby-default-gems < 3.1)
Requires: (rubygem(net-pop) or ruby-default-gems < 3.1)
Requires: (rubygem(net-smtp) or ruby-default-gems < 3.1)

%description
Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

# On EL9 rubygem-net-smtp/imap/pop are bundled into ruby-libs package and
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
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
* Wed Nov 06 2024 Evgeni Golov - 7.0.8.6-1
- Release rubygem-actionmailer 7.0.8.6

* Sun Oct 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.7.10-1
- Update to 6.1.7.10

* Wed Oct 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.7.9-1
- Update to 6.1.7.9

* Sun Jun 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.7.8-1
- Update to 6.1.7.8

* Thu Feb 29 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.1.7.7-1
- Update to 6.1.7.7

* Sun Aug 27 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.6-1
- Update to 6.1.7.6

* Sun Jul 02 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.4-1
- Update to 6.1.7.4

* Tue Mar 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.3-1
- Update to 6.1.7.3

* Fri Jan 27 2023 Eric D. Helms <ericdhelms@gmail.com> - 6.1.7.2-1
- Release rubygem-actionmailer 6.1.7.2

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7.1-1
- Update to 6.1.7.1

* Sun Nov 20 2022 Foreman Packaging Automation <packaging@theforeman.org> 6.1.7-1
- Update to 6.1.7

* Thu Jul 14 2022 Evgeni Golov - 6.1.6.1-1
- Release rubygem-actionmailer 6.1.6.1

* Mon May 16 2022 Eric D. Helms <ericdhelms@gmail.com> - 6.1.6-1
- Release rubygem-actionmailer 6.1.6

* Fri Mar 18 2022 Eric D. Helms <ericdhelms@gmail.com> - 6.0.4.7-1
- Release rubygem-actionmailer 6.0.4.7

* Mon May 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.7-1
- Release 6.0.3.7

* Wed Mar 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.5-2
- Rebuild against rh-ruby27

* Tue Feb 23 2021 Evgeni Golov - 6.0.3.5-1
- Release rubygem-actionmailer 6.0.3.5

* Mon Oct 26 2020 Evgeni Golov - 6.0.3.4-1
- Release rubygem-actionmailer 6.0.3.4

* Mon Jun 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.1-1
- Release rubygem-actionmailer 6.0.3.1

* Tue Apr 28 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.0.2.2-1
- Update to 6.0.2.2

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.0.2.1-1
- Release rubygem-actionmailer 6.0.2.1

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 5.2.1-2
- Bump for moving over to foreman-packaging

* Wed Aug 22 2018 Eric D. Helms <ericdhelms@gmail.com> 5.2.1-1
- Release tfm-ror52-rubygem-actionmailer 5.2.1

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-2
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-1
- Initial package
