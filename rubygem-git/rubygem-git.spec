%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name git

Summary:        A package for using Git in Ruby code
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.2.5
Release:        6%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://rubyforge.org/projects/git/
Source0:        http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:       %{?scl_prefix_ruby}ruby(rubygems)
Requires:       %{?scl_prefix_ruby}ruby(abi) = 1.9.1
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A package for using Git in Ruby code.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} - << \EOF}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:EOF}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%doc %{gem_instdir}/README
%doc %{gem_docdir}
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.2.5-6
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Mar 18 2015 Dominic Cleal <dcleal@redhat.com> 1.2.5-5
- Import and convert for SCL

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.2.5-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.2.5-1
- New upstream version

* Wed Oct 14 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.2.4-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 02 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-4
- Fix %%doc

* Mon Sep 08 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-3
- Add ruby(abi) = 1.8 requires (#459883, tibbs)

* Sun Sep 07 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-2
- Fix up comments from review (#459883, JonRob)

* Sat Aug 23 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-1
- Initial package for review
