%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rubyforge

# Depency loop here. Kill test when resolving dependency loop
# is needed
%global enable_test 0

Summary:       A script which automates a limited set of rubyforge operations
Name:          %{?scl_prefix}rubygem-%{gem_name}
Version:       2.0.4
Release:       4%{?dist}
Group:         Development/Languages
License:       MIT
URL:           http://rubyforge.org/projects/codeforpeople
Source0:       http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
BuildRoot:     %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      %{?scl_prefix_ruby}ruby(abi) = 1.9.1
Requires:      %{?scl_prefix_ruby}rubygems
Requires:      %{?scl_prefix_ruby}rubygem(json) >= 1.1.7
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
%if %{enable_test}
BuildRequires(check): rubygem(rake)
BuildRequires(check): rubygem(json)
# The following line causes dependency loop
BuildRequires(check): rubygem(hoe)
%endif
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A script which automates a limited set of rubyforge operations.


%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p ./%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install \
	--local \
	--install-dir ./%{gem_dir} \
	--force \
	--rdoc \
	%{SOURCE0}
%{?scl:"}

# json_pure -> json
find . -name Rakefile -or -name \*.gemspec | \
	xargs sed -i -e 's|json_pure|json|g'

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}/%{gem_dir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
chmod 0755 %{buildroot}%{gem_instdir}/lib/rubyforge.rb
chmod 0755 %{buildroot}%{gem_instdir}/bin/rubyforge

%clean
rm -rf %{buildroot}

%check
%if ! %{enable_test}
exit 0
%endif

pushd .%{gem_dir}
# Hoe needs rubyforge, so make it sure that system-widely installed
# Hoe looks for rubyforge just trying to install now first, not
# system-widely installed rubyforge
export GEM_PATH=$(pwd)
popd

pushd .%{gem_instdir}
rake test
popd

%files
%defattr(-, root, root, -)
%{_bindir}/rubyforge
%dir %{gem_instdir}
%{gem_instdir}/lib/
%{gem_instdir}/bin/
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/test/

%changelog
* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.4-3
- new package built with tito

* Mon Jul 02 2012 Lukas Zapletal <lzap+git@redhat.com> 2.0.4-2
- first build

* Thu Mar  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.4-1
- Update to 2.0.4
- Replace json_pure to json (bug 570252)

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> - 2.0.3-1
- Added new dependency on rubygem-json >= 1.1.7.
- Release 2.0.3 of RubyForge.

* Tue Sep 15 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.0.5-1
- Release 1.0.5 of RubyForge.

* Sat Aug  8 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.0.4-1
- Release 1.0.4 of RubyForge.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Darryl Pierce <dpierce@redhat.com> - 1.0.3-1
- Release 1.0.3 of RubyForge.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Darryl Pierce <dpierce@redhat.com> - 1.0.2-2
- Provided the wrong gem as source.

* Tue Jan 06 2009 Darryl Pierce <dpierce@redhat.com> - 1.0.2-1
- Release 1.0.2 of Rubyforge.

* Thu Oct 23 2008 Darryl Pierce <dpierce@redhat.com> - 1.0.1-1
- Release 1.0.1 of Rubyforge.

* Mon Jun 09 2008 Darryl Pierce <dpierce@redhat.com> - 1.0.0-1
- New version of RubyForge released.

* Wed May 14 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.5-2
- Figured out how to do a proper build.

* Mon May 12 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.5-1
- New version of the gem released.

* Tue Apr 29 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.4-3
- Fixed the executable attribute for rubyforge.rb.

* Mon Apr 28 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.4-2
- Updated the spec to comply with Ruby packaging guidelines.

* Fri Apr 18 2008 Darryl Pierce <dpierce@redhat.com> - 0.4.4-1
- Initial package
