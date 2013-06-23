%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name rack-protection

%global bootstrap 0

Summary:        Ruby gem that protects against typical web attacks
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.2.0
Release:        10%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://github.com/rkh/rack-protection
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1
Requires:       %{?scl_prefix}ruby(rubygems)
Requires:       %{?scl_prefix}rubygem(rack)
BuildRequires:  %{?scl_prefix}rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires:  %{?scl_prefix}rubygem(minitest)
BuildRequires:  %{?scl_prefix}rubygem(rack)
BuildRequires:  %{?scl_prefix}rubygem(rspec)
BuildRequires:  %{?scl_prefix}rubygem(rack-test)
%endif
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem protects against typical web attacks.
Should work for all Rack apps, including Rails.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -q -c -T
%{__mkdir_p} .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force -V %{SOURCE0}
%{?scl:"}
rm .%{gem_instdir}/%{gem_name}.gemspec
rm .%{gem_cache}

%build

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
%{?scl:scl enable %scl "}
rspec spec
%{?scl:"}
popd
%endif

%install
%{__mkdir_p} %{buildroot}%{gem_dir}
cp -rv .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/License

%files doc
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%doc %{gem_docdir}

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.0-10
- remove bootstrap (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.0-9
- allow bootstrap (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.0-8
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-7
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-6
- Allowed tests running.

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-5
- Rebuilt for scl.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-4
- Set %%bootstrap to 0 to allow tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-3
- Rebuilt for Ruby 1.9.3.
- Introduced bootstrap to deal with dependency loop.

* Mon Jan 03 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-2
- Fixed BR
- Marked documentation file with doc tag
- Changed the way how to run rspec tests

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-1
- Initial import
