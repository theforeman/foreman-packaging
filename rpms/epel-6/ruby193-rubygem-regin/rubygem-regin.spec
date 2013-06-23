%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name regin
%global rubyabi 1.9.1

Summary: Ruby Regexp Introspection
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.8
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/josh/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/josh/regin.git && cd regin && git checkout v0.3.8
# tar czvf regin-tests.tgz spec/
Source1: %{gem_name}-tests.tgz
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Regin allows you to introspect on Ruby Regexps. Powered by an over the top
regexp syntax parser written in racc/rexical.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep

%build

%install
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%clean

%check
mkdir %{_tmppath}/%{gem_name}-%{version}
tar xzvf %{SOURCE1} -C %{_tmppath}/%{gem_name}-%{version}

pushd %{_tmppath}/%{gem_name}-%{version}
%{?scl:scl enable %{scl} - << \EOF}
RUBYOPT="-I%{buildroot}%{gem_instdir}/lib" rspec spec/
%{?scl:EOF}
popd

rm -rf %{_tmppath}/%{gem_name}-%{version}

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.8-5
- new package built with tito

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.3.8-4
- rebuild

* Mon Nov 7 2011 Steve Linabery <slinaber@redhat.com> - 0.3.8-2
- Bump release to avoid conflict with previously checked in but unbuilt 0.3.8-1

* Wed Apr 06 2011 Vít Ondruch <vondruch@redhat.com> - 0.3.8-1
- Updated to Regin 0.3.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Vít Ondruch <vondruch@redhat.com> - 0.3.7-2
- Removed obsolete cleanup from install and clean sections

* Wed Jan 19 2011 Vít Ondruch <vondruch@redhat.com> - 0.3.7-1
- Initial package
