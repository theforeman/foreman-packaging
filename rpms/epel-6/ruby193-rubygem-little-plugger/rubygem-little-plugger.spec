%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from little-plugger-1.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name little-plugger

%global rubyabi 1.9.1

Summary: LittlePlugger is a module that provides Gem based plugin management
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.3
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/little-plugger
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
LittlePlugger is a module that provides Gem based plugin management.
By extending your own class or module with LittlePlugger you can easily
manage the loading and initializing of plugins provided by other gems.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
rspec spec/
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_libdir}
%{gem_cache}
%{gem_spec}
# contains licensing information
%doc %{gem_instdir}/README.rdoc

%files doc
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt

%changelog
* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.1.3-6
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.1.3-5
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.3-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.3-1
- Update to 1.1.3 version (migrates tests to rspec 2, thanks Vit Ondruch for patch for upstream).

* Wed Nov 02 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.2-3
- Introduced doc subpackage.
- Introduced check section.
- Removed rspec from Requires and moved it to BuildRequires, as it is only needed for running specs.

* Sat Apr 02 2011 Chris Lalancette <clalance@redhat.com> - 1.1.2-2
- Use the gem from rubygems.org instead of from git

* Wed Mar 16 2011 Chris Lalancette <clalance@redhat.com> - 1.1.2-1
- Initial package
