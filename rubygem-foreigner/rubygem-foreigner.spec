%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from foreigner-0.9.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name foreigner
%global rubyabi  1.9.1

Summary:       Foreign Keys for Rails
Name:          %{?scl_prefix}rubygem-%{gem_name}
Version:       1.7.0
Release:       1%{?dist}
License:       MIT

URL:           http://github.com/matthuhiggins/foreigner
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem

Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

BuildArch:     noarch

%if 0%{?fedora} >= 19
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}ruby
%endif

BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

%if 0%{?fedora} >= 19
Requires:      %{?scl_prefix}ruby(release)
%else
Requires:      %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:      %{?scl_prefix}ruby
%endif
Requires:      %{?scl_prefix}rubygems
Requires:      %{?scl_prefix}rubygem(activerecord) >= 3.0.0


%description
Adds helpers to migrations and correctly dumps foreign keys to schema.rb.


%package doc
Summary:   Documentation for %{pkg_name}
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch


%description doc
%{summary}.


%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}


%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Sep 10 2013 Dominic Cleal <dcleal@redhat.com> 1.4.2-1
- Rebased on foreigner 1.4.2 (dcleal@redhat.com)

* Fri Apr 19 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-4
- wrap up "gem spec" in scl macro (msuchy@redhat.com)

* Thu Apr 18 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-3
- add BR rubygems (msuchy@redhat.com)

* Thu Apr 18 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-2
- new package built with tito

* Mon Apr  8 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.4.1-1
- Rebased on foreigner 1.4.1.

* Wed Mar 13 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.4.0-2
- Updated the specfile to meet current Ruby packaging guidelines.

* Tue Feb 26 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.4.0-1
- Rebased on Foreigner 1.4.0.

* Wed Jan 16 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.3.0-1
- Rebased on foreigner 1.3.0.

* Mon Jan  7 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.2.1-1.1
- Package now installs recreated gemfile.

* Thu Dec 20 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.2.1-1
- Rebased on foreigner 1.2.1.
- Updated the specfile to reflect current Ruby packaging guidelines.

* Wed Jul 18 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.2.0-1
- Rebased on foreigner release 1.2.0.
- Removed the tests since they were not invoked.

* Thu Apr 05 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.6-1
- Release 1.1.6 of Foreigner.
- Added BuildRequires: {ruby(rubygems), ruby(abi) ruby} fields to the spec.

* Thu Mar 08 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.5-1
- Release 1.1.5 of Foreigner.

* Tue Mar 06 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.4-1
- Release 1.1.4 of Foreigner.

* Sat Feb 18 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.2-1
- Release 1.1.2 of Foreigner.

* Wed Feb 08 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.1-4
- Fixed broken dependencies.

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug  9 2011 Darryl L. Pierce <dpierce@redhat.com> - 1.1.1-1
- Release 1.1.1 of Foreigner gem.

* Mon Aug  1 2011 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-1
- Release 1.1.0 of Foreigner gem.
- Added the doc subpackage.
- Added requirement on rubygem-activerecord >= 3.0.0

* Wed Jul 20 2011 Darryl L. Pierce <dpierce@redhat.com> - 1.0.3-1
- New release of Foreigner gem.
- Added version requirement for rubygems.

* Tue May 10 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.9.2-2
- Fixed license.
- Added dependency on Ruby 1.8.
- Fixed global macros.

* Tue Apr 19 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.9.2-1
- Initial package
