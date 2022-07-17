# template: default
%global gem_name paint

Name: rubygem-%{gem_name}
Version: 2.3.0
Release: 1%{?dist}
Summary: Terminal painter!
License: MIT
URL: https://github.com/janlelis/paint
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.3
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Terminal painter with RGB and 256 (fallback) color and terminal effects
support. No string extensions! Usage: Paint['string', :red, :bright].


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
%license %{gem_instdir}/MIT-LICENSE.txt
%exclude %{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/paint.gemspec

%changelog
* Sun Jul 17 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.3.0-1
- Update to 2.3.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.8.7-10
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.8.7-9
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.8.7-8
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.7-7
- Final set of rebuilds (ericdhelms@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.8.7-6
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.8.7-5
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.8.7-4
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.8.7-3
- Convert to SCL

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Miroslav Suchý <miroslav@suchy.cz> 0.8.7-1
- rebase paint-0.8.7.gem

* Mon Aug 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-3
- 998459 - move README and LICENSE to main package
- 998459 - remove excessive cp
- 998459 - use virtual requires
- 998459 - remove ruby mri requires

* Mon Aug 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-2
- enable tests
- fix files section

* Mon Aug 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-1
- initial package
