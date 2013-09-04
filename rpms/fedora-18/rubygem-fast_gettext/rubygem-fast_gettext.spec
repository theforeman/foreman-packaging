%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fast_gettext

Summary: A simple, fast, memory-efficient and threadsafe implementation of GetText
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.8.0
Release: 1%{?dist}
Group: Development/Languages
# fast_gettext is MIT. However the files in lib/vendor directory
# are GPLv2+ or Ruby licensed.
# https://github.com/grosser/fast_gettext/issues/50
License: MIT and (GPLv2+ or Ruby)
URL: http://github.com/grosser/fast_gettext
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
Requires: %{?scl_prefix}ruby(rubygems)
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(activerecord)
#BuildRequires: %{?scl_prefix}rubygem(protected_attributes)
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A simple, fast, memory-efficient and threadsafe implementation of GetText

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/Readme.md
%exclude %{gem_instdir}/fast_gettext.gemspec
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile*
%{gem_instdir}/Appraisals
%{gem_instdir}/Rakefile
%{gem_instdir}/benchmark
%doc %{gem_instdir}/examples
%{gem_instdir}/gemfiles
%{gem_instdir}/spec
%doc %{gem_docdir}

%changelog
* Fri Aug 30 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.8.0-1
- update to 0.8.0 (multi-domain support)
- renamed spec name to comply with standards
- new SPEC content derived from F19 (0.7.1-1) and spec2scl

* Mon Aug 19 2013 Vít Ondruch <vondruch@redhat.com> - 0.7.1-1
- Update to fast_gettext 0.7.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Vít Ondruch <vondruch@redhat.com> - 0.7.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to fast_gettext 0.7.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.6.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.1-1
- Update to fast_gettext 6.1.

* Mon Aug 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.13-1
- Initial package
