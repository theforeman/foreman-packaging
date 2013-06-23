%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from rack-cache-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rack-cache

%global rubyabi 1.9.1

Summary: HTTP Caching for Rack
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://tomayko.com/src/rack-cache/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(rack) >= 0.4
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(bacon)
BuildRequires: %{?scl_prefix}rubygem(rack) >= 0.4
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Rack::Cache is suitable as a quick drop-in component to enable HTTP caching for
Rack-based applications that produce freshness (Expires, Cache-Control) and/or
validation (Last-Modified, ETag) information

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd ./%{gem_instdir}
%{?scl:scl enable %scl "}
bacon -I. -q test/*_test.rb
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/COPYING
%exclude %{gem_instdir}/rack-cache.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/example
%{gem_instdir}/test


%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.2-3
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-2
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-1
- Updated to 1.2.
- Rebuilt for scl.

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 1.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Vít Ondruch <vondruch@redhat.com> - 1.1-1
- Updated to rack-cache 1.1.

* Fri Jul 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.2-1
- Initial package
