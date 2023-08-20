# template: default
%global gem_name xmlrpc

Name: rubygem-%{gem_name}
Version: 0.3.3
Release: 1%{?dist}
Summary: XMLRPC is a lightweight protocol that enables remote procedure calls over HTTP
License: Ruby and BSD-2-Clause
URL: https://github.com/ruby/xmlrpc
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3
BuildRequires: ruby >= 2.3
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
XMLRPC is a lightweight protocol that enables remote procedure calls over
HTTP.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/NEWS.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/xmlrpc.gemspec

%changelog
* Sun Aug 20 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.3.3-1
- Update to 0.3.3

* Sun Oct 16 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.3.2-1
- Update to 0.3.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.3.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.3.0-2
- Bump to release for EL8

* Sun Nov 11 2018  0.3.0-1
- Add rubygem-xmlrpc generated by gem2rpm using the scl template

