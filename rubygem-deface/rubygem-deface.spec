%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name deface

Summary: Deface is a library that allows you to customize views in Rails
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.0
Release: 7%{?dist}
Group: Development/Libraries
License: MIT
URL: https://github.com/spree/deface
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(rainbow) >= 2.1.0
Requires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.6.0
Requires: %{?scl_prefix_ror}rubygem(nokogiri) < 2.0.0
Requires: %{?scl_prefix_ror}rubygem(polyglot)
Requires: %{?scl_prefix_ror}rubygem(rails) >= 4.1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Deface is a library that allows you to customize ERB, Haml and Slim
views in a Rails application without editing the underlying view.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/init.rb
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Appraisals
%exclude %{gem_instdir}/gemfiles
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/CHANGELOG.markdown
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Mar 20 2017 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- Update deface to 1.2.0 (dominic@cleal.org)

* Mon Jan 09 2017 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update deface to 1.1.0 (dominic@cleal.org)
- Loosen nokogiri dependency to permit 1.7 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Nov 16 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- Update deface to 1.0.2 (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update deface to 1.0.1 (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.7.2-7
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 14 2013 Lukas Zapletal <lzap+git@redhat.com> 0.7.2-6
- rebuild


* Fri May 31 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.2-5
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-3
- new package built with tito

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-2
- rubygem-deface - convert to scl (inecas@redhat.com)

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-1
- new package built with tito
