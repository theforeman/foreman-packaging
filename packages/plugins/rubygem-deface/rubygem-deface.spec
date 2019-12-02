# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name deface

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.5.3
Release: 1%{?dist}
Summary: Deface is a library that allows you to customize ERB, Haml and Slim views in Rails
Group: Development/Languages
License: MIT
URL: https://github.com/spree/deface
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.6
Requires: %{?scl_prefix_ror}rubygem(rails) >= 4.1
Requires: %{?scl_prefix}rubygem(rainbow) >= 2.1.0
Requires: %{?scl_prefix}rubygem(polyglot)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Deface is a library that allows you to customize ERB, Haml and Slim views in a
Rails application without editing the underlying view.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Appraisals
%license %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/gemfiles
%{gem_instdir}/init.rb
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.markdown
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/deface.gemspec
%{gem_instdir}/spec

%changelog
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
