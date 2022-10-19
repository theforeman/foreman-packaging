# template: default
%global gem_name net-ssh-multi

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Control multiple Net::SSH connections via a single interface
License: MIT
URL: https://github.com/net-ssh/net-ssh-multi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Control multiple Net::SSH connections via a single interface.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/CHANGES.txt
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/gem-public_cert.pem
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/net-ssh-multi.gemspec
%{gem_instdir}/test

%changelog
* Wed Oct 19 2022 Evgeni Golov 1.2.1-1
- Update to 1.2.1-1

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-10
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.2.0-9
- Update spec to remove the ror scl

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-8
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.0-7
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.2.0-6
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-5
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jun 13 2014 Julian C. Dunn <jdunn@aquezada.com> - 1.2.0-3
- Convert to Minitest (bz#1107179)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 21 2013 Julian C. Dunn <jdunn@aquezada.com> - 1.2.0-1
- Update to 1.2.0 (bz#1015287)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 16 2013 Julian C. Dunn <jdunn@aquezada.com> - 1.1-4
- Unbreak build on >= F19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.1-2
- Unified EPEL and Fedora builds

* Sat Apr 14 2012  <rpms@courteau.org> - 1.1-1
- Initial package
