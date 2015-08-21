# Generated from turbolinks-0.5.1.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name turbolinks

Summary:        Turbolinks makes following links in your web application faster
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        2.5.3
Release:        1%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://github.com/rails/turbolinks
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires:       %{?scl_prefix_ruby}ruby(release)
%else
Requires:       %{?scl_prefix_ruby}ruby(abi)
%endif
Requires:       %{?scl_prefix_ruby}ruby(rubygems)
Requires:       %{?scl_prefix_ruby}rubygem(coffee-rails)
%if 0%{?fedora} > 18
BuildRequires:  %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires:  %{?scl_prefix_ruby}ruby(abi)
%endif
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Turbolinks makes following links in your web application faster. Instead of
letting the browser recompile the JavaScript and CSS between each page change,
it keeps the current page instance alive and replaces only the body and
the title in the head. Think CGI vs persistent process. (Use with Rails Asset
Pipeline.)

%package doc
Summary:    Documentation for %{pkg_name}
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch:  noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build
%check
# To test it:
# run `rackup "test/config.ru"` to run the server and check manually serving assets
# no idea how to make it automated in koji right now

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 2.5.3-1
- Import from Fedora, SCLise and update to 2.5.3 (dcleal@redhat.com)

* Tue Oct 14 2014 Josef Stribny <jstribny@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Wed Jul 09 2014 Josef Stribny <jstribny@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Josef Stribny <jstribny@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Wed Oct 23 2013 Josef Stribny <jstribny@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Josef Stribny <jstribny@redhat.com> - 1.1.1-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to 1.1.1

* Thu Nov 15 2012 Josef Stribny <jstribny@redhat.com> - 0.5.1-1
- Initial package
