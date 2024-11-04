# template: default
%global gem_name deface

Name: rubygem-%{gem_name}
Version: 1.9.0
Release: 1%{?dist}
Summary: Deface is a library that allows you to customize ERB, Haml and Slim views in Rails
License: MIT
URL: https://github.com/spree/deface#readme
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Deface is a library that allows you to customize ERB, Haml and Slim views in a
Rails application without editing the underlying view.


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
%exclude %{gem_instdir}/Appraisals
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%exclude %{gem_instdir}/gemfiles
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.markdown
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/deface.gemspec
%{gem_instdir}/spec

%changelog
* Thu Feb 08 2024 Evgeni Golov - 1.9.0-1
- Update to 1.9.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.5.3-3
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.5.3-2
- Update spec to remove the ror scl

* Mon Dec 02 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.5.3-1
- Update to 1.5.3-1

* Mon Oct 01 2018 Ivan Nečas <inecas@redhat.com> 1.3.2-1
- Update to 1.3.2

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-9
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.0-8
- Add rubygem-polyglot and update deface (ericdhelms@gmail.com)

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.0-7
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Mar 20 2017 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- Update deface to 1.2.0 (dominic@cleal.org)

* Mon Jan 09 2017 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update deface to 1.1.0 (dominic@cleal.org)
- Loosen nokogiri dependency to permit 1.7 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Nov 16 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- Update deface to 1.0.2 (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update deface to 1.0.1 (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.7.2-7
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 14 2013 Lukas Zapletal <lzap+git@redhat.com> 0.7.2-6
- rebuild


* Fri May 31 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.2-5
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-3
- new package built with tito

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-2
- rubygem-deface - convert to scl (inecas@redhat.com)

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-1
- new package built with tito
