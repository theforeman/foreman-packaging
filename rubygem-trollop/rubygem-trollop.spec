%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global	gem_name trollop

Summary:	A command-line option parsing library for ruby
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	2.0
Release:	3%{?dist}
Group:		Applications/Productivity
License:	GPLv2
URL:		http://trollop.rubyforge.org/
BuildRoot:	%{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	%{?scl_prefix_ruby}ruby(rubygems)
Requires:	%{?scl_prefix_ruby}ruby(abi) = 1.9.1
BuildRequires:	%{?scl_prefix}rubygem(hoe)
BuildRequires:	%{?scl_prefix_ruby}rubygems-devel
BuildRequires:  %{?scl_prefix_ruby}rubygem(minitest)
BuildArch:	noarch
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

%description
A command-line option parsing library for ruby. Trollop is designed to
provide the maximal amount of GNU-style argument processing in the minimum
number of lines of code (for you, the programmer).

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
	--force --rdoc %{SOURCE0}
%{?scl:"}

%check
cd %{buildroot}/%{gem_instdir}
%{?scl:scl enable %{scl} "}
ruby -Ilib/ test/test_trollop.rb
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/test
%doc %{gem_instdir}/*.txt
%doc %{gem_docdir}
%{gem_cache}
%{gem_spec}

%changelog
* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 2.0-2
- new package built with tito

* Sun Aug 19 2012 Jan Klepek <jan.klepek, at gmail.com> - 2.0-1
- updated to latest release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.16.2-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Jan Klepek <jan.klepek at, gmail.com> - 1.16.2-1
- updated to 1.16.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 3 2009 Jan Klepek <jan.klepekat, gmail.com> - 1.15-1
- update of trollop to 1.15

* Thu Sep 24 2009 Jan Klepek <jan.klepekat, gmail.com> - 1.14-1
- directory ownership fix, license changed to GPLv2, redundant macro removed

* Sun Sep 20 2009 Jan Klepek <jan.klepekat, gmail.com> - 1.14-0
- Version update,

* Sat Jan 24 2009 Kyle McMartin <kyle@redhat.com> - 1.10.2-1
- Initial release of trollop.
