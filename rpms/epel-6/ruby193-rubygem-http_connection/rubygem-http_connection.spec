%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name http_connection

Summary: RightScale's robust HTTP/S connection module
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.1
Release: 7%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/appoxy/http_connection
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: %{?scl_prefix}rubygem(right_http_connection)

%description
Rightscale::HttpConnection is a robust HTTP(S) library. It implements a retry
algorithm for low-level network errors.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README.txt
%doc %{gem_docdir}
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-7
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-6
- Specfile cleanup

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-5
- Rebuilt for scl.

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Michal Fojtik <mfojtik@redhat.com> - 1.4.1-2
- Added rubygem-right_http_connection to Provide and Obsolete

* Thu Jun 16 2011 Michal Fojtik <mfojtik@redhat.com> - 1.4.1-1
- Renaming package rubygem-right_http_connection

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.4-2
- Fixed duplicated files
- Fixed ruby dependency

* Wed Mar 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.4-1
- Initial package
