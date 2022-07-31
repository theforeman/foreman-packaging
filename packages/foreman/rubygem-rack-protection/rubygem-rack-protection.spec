# template: default
%global gem_name rack-protection

Name: rubygem-%{gem_name}
Version: 2.2.2
Release: 1%{?dist}
Summary: Protect against typical web attacks, works with all Rack apps, including Rails
License: MIT
URL: http://sinatrarb.com/protection/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Protect against typical web attacks, works with all Rack apps, including
Rails.


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
%license %{gem_instdir}/License
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/rack-protection.gemspec

%changelog
* Sun Jul 31 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.2.2-1
- Update to 2.2.2

* Fri Jul 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.2.1-1
- Update to 2.2.1

* Fri May 13 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-1
- Release rubygem-rack-protection 2.2.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-2
- Rebuild against rh-ruby27

* Thu Dec 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-1
- Release rubygem-rack-protection 2.1.0

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.3-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.3-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.0.3-2
- Bump for moving over to foreman-packaging

* Tue Aug 14 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-1
- Initial package
