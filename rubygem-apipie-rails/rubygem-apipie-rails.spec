%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name apipie-rails

Summary: Rails API documentation tool and client generator
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.5
Release: 1%{?dist}
Group: Development/Libraries
#This gem is released under MIT license. Copy is included in file MIT-LICENSE.
#
#Twitter Bootstrap and google-code-prettify are licensed under Apache License
#2.0. Copy is included in file APACHE-LICENSE-2.0.
License: MIT and ASL 2.0
URL: http://github.com/Pajk/apipie-rails
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem


Requires: %{?scl_prefix}rubygems
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem adds new methods to Rails controllers that can be used to describe
resources exposed by API. Information entered with provided DSL are used
to generate documentation, client or to validate incoming requests.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/APACHE-LICENSE-2.0

%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/rel-eng
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Gemfile.*
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/README.rst
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/NOTICE
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
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

