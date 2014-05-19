%global gem_name rack-protection

%global bootstrap 1

Summary:        Ruby gem that protects against typical web attacks
Name:           rubygem-%{gem_name}
Version:        1.3.2
Release:        3%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://github.com/rkh/rack-protection
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(rack)
BuildRequires:  rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(rack-test)
%endif
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
This gem protects against typical web attacks.
Should work for all Rack apps, including Rails.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation

Requires:	%{name} = %{version}-%{release}
Requires:	ruby(rubygems)

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T
%{__mkdir_p} .%{gem_dir}
%gem_install -n %{SOURCE0}
rm .%{gem_instdir}/%{gem_name}.gemspec
rm .%{gem_cache}

%build

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
rspec spec
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
* Tue Mar 05 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 22 2013 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Fixed rspec dependency

* Thu Feb 21 2013 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-1
- Release 1.3.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

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
