%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name open4
%global rubyabi 1.9.1

Summary: Manage child processes and their IO handles easily
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.0
Release: 6%{?dist}
Group: Development/Languages
License: BSD or Ruby
URL: http://github.com/ahoward/open4/tree/master
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Open child process with handles on pid, stdin, stdout, and stderr.
Manage child processes and their IO handles easily.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

#%check
#pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %{scl} "}
#testrb -Ilib -Itest/support test/*
%{?scl:"}
#popd

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.erb
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%{gem_instdir}/rakefile
%{gem_instdir}/samples
%{gem_instdir}/test
%{gem_instdir}/white_box
%{gem_instdir}/%{gem_name}.gemspec
%{gem_docdir}

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.0-6
- new package built with tito

* Sat Jun 30 2012 Miroslav Suchý <msuchy@redhat.com> 1.3.0-5
- add undefined macros - missing due missing rubygem-devel (msuchy@redhat.com)

* Sat Jun 30 2012 Miroslav Suchý <msuchy@redhat.com> 1.3.0-4
- disable tests (msuchy@redhat.com)

* Sat Jun 30 2012 Miroslav Suchý <msuchy@redhat.com> 1.3.0-3
- remove dependency on rubygem-devel in el6 (msuchy@redhat.com)

* Sat Jun 30 2012 Miroslav Suchý <msuchy@redhat.com> 1.3.0-2
- new package built with tito

* Tue Feb 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.0-2
- Fixed the license after clarification with the author.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.0-1
- Rebuilt for Ruby 1.9.3.
- Updated to 1.3.0 version.
- Introduced %%check section for running tests.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 13 2010 Michal Fojtik <mfojtik@redhat.com> - 1.0.1-1
- Initial package
