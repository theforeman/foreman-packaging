%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name will_paginate


Summary:       Most awesome pagination solution for Rails
Name:          %{?scl_prefix}rubygem-%{gem_name}
Version:       3.1.5
Release:       1%{?dist}
Group:         Development/Languages
License:       MIT
URL:           http://github.com/mislav/will_paginate
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
Requires:      %{?scl_prefix_ror}rubygem(activerecord)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ror}rubygem(activesupport)
BuildRequires: %{?scl_prefix_ror}rubygem(actionpack)
BuildRequires: %{?scl_prefix_ror}rubygem(activerecord)
BuildRequires: %{?scl_prefix_ror}rubygem(mocha)
BuildRequires: %{?scl_prefix_ror}rubygem(sqlite3)
BuildRequires: %{?scl_prefix_ror}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(sequel)
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
The will_paginate library provides a simple, yet powerful and extensible API
for ActiveRecord pagination and rendering of pagination links in ActionView
templates.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
#%{?scl:scl enable %{scl} "}
#rspec spec
#%{?scl:"}
popd

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/spec

%changelog
* Wed Oct 19 2016 Dominic Cleal <dominic@cleal.org> 3.1.5-1
- Update will_paginate to 3.1.5 (dominic@cleal.org)

* Fri Sep 23 2016 Dominic Cleal <dominic@cleal.org> 3.1.3-1
- Update will_paginate to 3.1.3 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 3.1.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Wed Jan 20 2016 Dominic Cleal <dcleal@redhat.com> 3.1.0-1
- Update will_paginate to 3.1.0 (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.0.7-1
- Update will_paginate to 3.0.7 (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 3.0.2-9
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Mar 15 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.2-7
- disable tests temporary (msuchy@redhat.com)

* Fri Mar 15 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.2-6
- use rspec instead of rspec-core (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.2-5
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.2-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.2-1
- Update to will_paginate 3.0.2.

* Tue Jul 12 2011 Mo Morsi <mmorsi@redhat.com> - 3.0-0.1.pre2
- Update to 3.0.pre2 for Rails 3 compatability

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 2.3.14-1
- Version bump

* Wed May 19 2010 Michal Fojtik <mfojtik@redhat.com> - 2.3.12-2
- Fixed documents
- Fixed macros in changelog
- Added activesupport to requires

* Tue May 18 2010 Michal Fojtik <mfojtik@redhat.com> - 2.3.12-1
- Version bump
- Fixed BuildRequires


* Tue Dec 08 2009 Darryl Pierce <dpierce@redhat.com> - 2.3.11-2
- Replaced %%define with %%global.
- Fixed license.
- Replaced the source URL.

* Thu Nov 19 2009 Darryl Pierce <dpierce@redhat.com> - 2.3.11-1
- Initial package
