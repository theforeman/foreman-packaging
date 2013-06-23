%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fastercsv

Summary:	Faster, smaller and cleaner replacement to standard CSV library
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	1.5.4
Release:	4%{?dist}
License:	GPLv2 or Ruby
Group:		Development/Languages
URL:		http://fastercsv.rubyforge.org/
Source:		http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:	%{?scl_prefix}ruby(abi) = 1.9.1, %{?scl_prefix}rubygems
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}
BuildRequires:	%{?scl_prefix}rubygems
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildArch:	noarch

%description
FasterCSV is intended as a complete replacement to the CSV standard library.
It is significantly faster and smaller while still being pure Ruby code. It
also strives for a better interface.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir $RPM_BUILD_ROOT%{gem_dir} --force --rdoc %{SOURCE0}
%{?scl:"}

# Find files with a shebang that do not have executable permissions
for file in $(find $RPM_BUILD_ROOT%{gem_instdir} -type f ! -perm /a+x -name "*.rb"); do
  if [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ]; then
    sed -e 's@/usr/local/bin/ruby@%{_bindir}/ruby@g' -i $file
    chmod -v 755 $file
  fi
done
%{__rm} -Rf %{buildroot}/%{gem_instdir}/.yardoc

%check
#ruby -I $RPM_BUILD_ROOT%{gem_instdir}/lib:$RPM_BUILD_ROOT%{gem_instdir}/test $RPM_BUILD_ROOT%{gem_instdir}/test/ts_all.rb

%files
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%dir %{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/INSTALL
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README
%doc %{gem_instdir}/TODO
%{gem_instdir}/Rakefile
%{gem_instdir}/examples/
%{gem_instdir}/lib/
%{gem_instdir}/setup.rb
%{gem_instdir}/test/

%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 1.5.4-4
- new package built with tito

* Mon Jul 16 2012 Miroslav Suchý <msuchy@redhat.com> 1.5.4-3
- new package built with tito

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Robert Scheck <robert@fedoraproject.org> 1.5.4-1
- Upgrade to 1.5.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 1.5.1-1
- Upgrade to 1.5.1

* Sun Aug 09 2009 Robert Scheck <robert@fedoraproject.org> 1.5.0-2
- Added missing requirement to ruby(abi) = version (#514928 #c1)
- Switched from defines to globals, updated summary in spec file
- Corrected license tag and removed duplicates in docs (#514928)

* Fri Jul 31 2009 Robert Scheck <robert@fedoraproject.org> 1.5.0-1
- Upgrade to 1.5.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
