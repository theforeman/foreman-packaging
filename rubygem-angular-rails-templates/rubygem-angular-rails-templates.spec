# Template for Rubygem's spec file
# It should work with f18, f19, rhel6 and rhel6 with SCL

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name angular-rails-templates

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   1.0.2
Release:   1%{?dist}
Epoch:     1
Summary:   Use your angular templates with rails' asset pipeline
Group:     Development/Languages
License:   MIT
URL:       https://github.com/pitr/angular-rails-templates
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires:  %{?scl_prefix_ruby}ruby(rubygems)
Requires:  %{?scl_prefix_ror}rubygem(railties) >= 4.2
Requires:  %{?scl_prefix_ror}rubygem(railties) < 6
Requires:  %{?scl_prefix_ror}rubygem(sprockets) >= 3.0
Requires:  %{?scl_prefix_ror}rubygem(sprockets) < 5
Requires:  %{?scl_prefix_ror}rubygem(tilt)
Requires:  %{?scl_prefix_ruby}ruby(release)

BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)

%description
Adds your HTML templates into Angular's $templateCache using Rails asset pipeline.
It removes the need for AJAX calls to retrieve the templates (or for you to manually set them into the DOM).

%package doc
BuildArch:  noarch
Requires:   %{name} = %{epoch}:%{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{name}

%description doc
This package contains documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_instdir}/vendor/assets/javascripts/angular-rails-templates.js.erb
%{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Sep 21 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.2-1
- Update rubygem-angular-rails-templates to 1.0.2 (kvedulv@kvedulv.de)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-5
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-4
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace tfm-rubygem-sprockets with ror41-rubygem-sprockets
  (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)
- Fix typo in -doc requires on main package (dcleal@redhat.com)

* Thu Feb 12 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-2
- Fix dep to include epoch between -doc and main package (dcleal@redhat.com)

* Thu Feb 12 2015 Eric D. Helms <ericdhelms@gmail.com> 0.1.2-1
- Update rubygem-angular-rails-templates to 0.1.2 (ericdhelms@gmail.com)

* Mon Feb 09 2015 Eric D. Helms <ericdhelms@gmail.com> 0.1.3-1
- Update 'rubygem-angular-rails-templates' to 0.1.3 (ericdhelms@gmail.com)

* Thu Oct 02 2014 Dominic Cleal <dcleal@redhat.com> 0.0.4-7
- new package built with tito (ehelms@redhat.com)
