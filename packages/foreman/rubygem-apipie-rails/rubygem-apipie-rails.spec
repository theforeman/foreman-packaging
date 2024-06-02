# template: default
%global gem_name apipie-rails

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 1%{?dist}
Summary: Rails REST API documentation tool
#This gem is released under MIT license. Copy is included in file MIT-LICENSE.
#
#Twitter Bootstrap and google-code-prettify are licensed under Apache License
#2.0. Copy is included in file APACHE-LICENSE-2.0.
License: MIT and ASL 2.0
URL: https://github.com/Apipie/apipie-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6.0
BuildRequires: ruby >= 2.6.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This gem adds new methods to Rails controllers that can be used to describe
resources exposed by API. Information entered with provided DSL are used
to generate documentation, client or to validate incoming requests.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.vscode/
%license %{gem_instdir}/APACHE-LICENSE-2.0
%license %{gem_instdir}/MIT-LICENSE
%license %{gem_instdir}/NOTICE
%exclude %{gem_instdir}/PROPOSAL_FOR_RESPONSE_DESCRIPTIONS.md
%{gem_instdir}/app
%{gem_instdir}/config
%exclude %{gem_instdir}/gemfiles
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/images
%{gem_libdir}
%exclude %{gem_instdir}/rel-eng
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rst
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/apipie-rails.gemspec
%{gem_instdir}/spec

%changelog
* Sun Jun 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.4.0-1
- Update to 1.4.0

* Sun Dec 31 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.3.0-1
- Update to 1.3.0

* Thu Oct 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.2.3-1
- Update to 1.2.3

* Wed Jul 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.2.2-1
- Update to 1.2.2

* Sun Jun 25 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.2.1-1
- Update to 1.2.1

* Tue May 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.0-1
- Update to 1.1.0

* Wed May 10 2023 Evgeni Golov 1.0.0-1
- Update to 1.0.0

* Sun Sep 18 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.8.2-1
- Update to 0.8.2

* Mon Aug 29 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.1-1
- Update to 0.8.1

* Fri Jul 22 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.20-1
- Update to 0.5.20

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.17-4
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.17-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.17-2
- Update spec to remove the ror scl

* Wed Jan 15 2020 Oleh Fedorenko <ofedoren@redhat.com> 0.5.17-1
- Update to 0.5.17

* Mon Nov 19 2018 Ivan Nečas <inecas@redhat.com> 0.5.14-1
- Update to 0.5.14

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.5.9-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jun 29 2018 Andrew Kofink <akofink@redhat.com> 0.5.9-1
- Update to 0.5.9

* Thu Mar 29 2018 Amit Karsale <karsale.amit@gmail.com> 0.5.7-1
- Update to 0.5.7

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.6-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)

* Wed Dec 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.5.6-1
- Update apipie-rails to 0.5.6 (pcreech@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Sep 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.5.4-1
- Update apipie-rails to 0.5.4 (ares@users.noreply.github.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Apr 26 2017 Dominic Cleal <dominic@cleal.org> 0.5.1-1
- Update apipie-rails to 0.5.1 (dominic@cleal.org)

* Mon Apr 24 2017 Dominic Cleal <dominic@cleal.org> 0.5.0-1
- Update apipie-rails to 0.5.0 (dominic@cleal.org)

* Tue Feb 21 2017 Dominic Cleal <dominic@cleal.org> 0.4.0-2
- Fix SCL prefix on rails dep (dominic@cleal.org)

* Mon Feb 20 2017 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- Update apipie-rails to 0.4.0 (dominic@cleal.org)

* Thu Oct 13 2016 Dominic Cleal <dominic@cleal.org> 0.3.7-1
- Update apipie-rails to 0.3.7 (dominic@cleal.org)

* Fri Feb 26 2016 Dominic Cleal <dominic@cleal.org> 0.3.6-1
- Update apipie-rails to 0.3.6 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.3.5-1
- Update apipie-rails to 0.3.5 (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.2.6-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Aug 29 2014 Dominic Cleal <dcleal@redhat.com> 0.2.6-1
- Bump version to 0.2.6 (dcleal@redhat.com)

* Fri Aug 22 2014 Dominic Cleal <dcleal@redhat.com> 0.2.5-1
- Bump version to 0.2.5 (dcleal@redhat.com)

* Mon Aug 11 2014 Dominic Cleal <dcleal@redhat.com> 0.2.4-1
- Bump version to 0.2.4 (dcleal@redhat.com)

* Sat Aug 09 2014 Dominic Cleal <dcleal@redhat.com> 0.2.3-1
- Bump version to 0.2.3 (dcleal@redhat.com)

* Thu Jul 24 2014 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Bump version to 0.2.2 (dcleal@redhat.com)

* Tue May 13 2014 Ivan Nečas <inecas@redhat.com> 0.2.0-1
- Bump version to 0.2.0 (inecas@redhat.com)

* Thu Mar 20 2014 Ivan Nečas <inecas@redhat.com> 0.1.2-1
- Bump version of apipie-rails to 0.1.2 (inecas@redhat.com)

* Thu Mar 13 2014 Ivan Nečas <inecas@redhat.com> 0.1.1-1
- Bump version of apipie-rails to 0.1.1 (inecas@redhat.com)

* Mon Mar 03 2014 Ivan Nečas <inecas@redhat.com> 0.1.0-1
- Bump version of apipie-rails to 0.1.0 (inecas@redhat.com)

* Wed Sep 04 2013 Ivan Necas <inecas@redhat.com> 0.0.23-1
- bumping version of apipie-rails to 0.0.23 (inecas@redhat.com)

* Wed Jun 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.22-3
- add ASL to license (msuchy@redhat.com)

* Wed Jun 12 2013 Lukas Zapletal <lzap+git@redhat.com> 0.0.22-2
- bumping version of apipie-rails to 0.0.22

* Wed May 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.21-2
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Fri May 10 2013 Ivan Necas <inecas@redhat.com> 0.0.21-1
- Use new version of apipie-rails - needed by the Foreman (inecas@redhat.com)
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.0.18-4
- fixing ruby193 scl package (lzap+git@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.18-3
- remove false positive scl macro (msuchy@redhat.com)

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.18-2
- new package built with tito

* Mon Feb 25 2013 Ivan Necas <inecas@redhat.com> 0.0.18-1
- param_group and def_param_group keywords
- :action_aware options for reusing param groups for create/update actions
- support for multiple see links at action and ability to provide
  description of see links

* Wed Feb 06 2013 Ivan Necas <inecas@redhat.com> 0.0.16-1
- New version of apipie from upstream (inecas@redhat.com)

* Thu Nov 29 2012 Petr Chalupa <pchalupa@redhat.com> 0.0.13-1
- New version of apipie (0.0.13) from upstream (pchalupa@redhat.com)

* Tue Oct 09 2012 Ivan Necas <inecas@redhat.com> 0.0.12-1
- New version of apipie from upstream (inecas@redhat.com)

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.11-3
- summary should not end with dot (msuchy@redhat.com)
- fix spelling (msuchy@redhat.com)
- do not package Gemfile.lock (msuchy@redhat.com)

* Fri Aug 17 2012 Ivan Necas <inecas@redhat.com> 0.0.11-2
- fix building for F17 reusing the macros from rubygem- devel

* Wed Aug 15 2012 Pavel Pokorný <pajkycz@gmail.com> 0.0.11-1
- apipie-rails v0.0.11
- cli client improvements

* Tue Jul 31 2012 Pavel Pokorný <pajkycz@gmail.com> 0.0.9-2
- exclude documentation from rpm

* Tue Jul 31 2012 Pavel Pokorný <pajkycz@gmail.com> 0.0.9-1
- New version of apipie-rails gem (pajkycz@gmail.com)
- fixed client generator
- resource level error descriptions
- response supported formats

* Thu Jul 26 2012 Pavel Pokorný <pajkycz@gmail.com> 0.0.8-3
- Require rubygems in spec file

* Thu Jul 26 2012 Pavel Pokorný <pajkycz@gmail.com> 0.0.8-2
- New version of apipie-rails gem
- Generated client improvements

* Thu Jul 26 2012 Pavel Pokorný <pajkycz@gmail.com> 0.0.7-2
- removed doc files from rpm

* Wed Jul 25 2012 Pavel Pokorný <pajkycz@gmail.com> 0.0.7-1
- new package built with tito
