# Generated from google-api-client-0.23.9.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name google-api-client

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.33.2
Release: 2%{?dist}
Summary: Client for accessing Google APIs
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/google/google-api-ruby-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.4
Requires: %{?scl_prefix_ruby}ruby < 3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(representable) >= 3.0
Requires: %{?scl_prefix}rubygem(representable) < 4
Requires: %{?scl_prefix}rubygem(retriable) >= 2.0
Requires: %{?scl_prefix}rubygem(retriable) < 4.0
Requires: %{?scl_prefix}rubygem(addressable) >= 2.5
Requires: %{?scl_prefix}rubygem(addressable) < 3
Requires: %{?scl_prefix}rubygem(addressable) >= 2.5.1
Requires: %{?scl_prefix}rubygem(mini_mime) >= 1.0
Requires: %{?scl_prefix}rubygem(mini_mime) < 2
Requires: %{?scl_prefix}rubygem(signet) >= 0.12
Requires: %{?scl_prefix}rubygem(signet) < 1
Requires: %{?scl_prefix}rubygem(googleauth) >= 0.9
Requires: %{?scl_prefix}rubygem(googleauth) < 1
Requires: %{?scl_prefix}rubygem(httpclient) >= 2.8.1
Requires: %{?scl_prefix}rubygem(httpclient) < 3.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.4
BuildRequires: %{?scl_prefix_ruby}ruby < 3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Client for accessing Google APIs.


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
#%%gem_install is not used here because building docs takes to much time
mkdir -p .%{gem_dir}

CONFIGURE_ARGS="--with-cflags='%{optflags}' $CONFIGURE_ARGS" \
gem install \
        -V \
        --local \
        --build-root . \
        --force \
        --no-document \
        --bindir %{_bindir} \
        %{gem_name}-%{version}.gem
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/generate-api
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/.kokoro
%exclude %{gem_instdir}/.github
%license %{gem_instdir}/LICENSE
%{gem_instdir}/api_names.yaml
%{gem_instdir}/bin
%{gem_instdir}/generated
%{gem_libdir}
%{gem_instdir}/rakelib
%{gem_instdir}/samples
%exclude %{gem_cache}
%{gem_spec}

%files doc
#%%gem_docdir is not populated because building docs takes to much time
#%%doc %%{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/MIGRATING.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/google-api-client.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.33.2-2
- Rebuild against rh-ruby27

* Thu Oct 08 2020 Ondřej Ezr <oezr@redhat.com> 0.33.2-1
- Update to 0.33.2

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.23.9-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.23.9-2
- Update spec to remove the ror scl

* Wed Mar 13 2019 kgaikwad <kavitagaikwad103@gmail.com> 0.23.9-1
- Update to 0.23.9

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.8.2-7
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.2-6
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.8.2-5
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.8.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.8.2-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.8.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Jan 12 2015 Dominic Cleal <dcleal@redhat.com> 0.8.2-1
- Update google-api-client to 0.8.2 (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 0.8.1.1-1
- Update google-api-client to 0.8.1.1 (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.7.1-1
- Update google-api-client to 0.7.1 (dcleal@redhat.com)

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.6.4-1
- new package built with tito
