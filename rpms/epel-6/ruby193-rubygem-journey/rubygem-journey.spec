%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
# Generated from journey-1.0.1.gem by gem2rpm -*- rpm-spec -*-

# TODO: It seems that this gem carries 3D JS library. Although JS libraries
# have exeption ATM, I asked upstream if they could remove it.
#
# https://github.com/rails/journey/issues/15

%global gem_name journey
%global rubyabi 1.9.1

Summary: Journey is a router
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.4
Release: 2%{?dist}
Group: Development/Languages
# Public Domain - %%{gem_libdir}/journey/visualizer/reset.css
License: MIT and Public Domain
URL: http://github.com/rails/journey
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/schneems/journey/commit/d4b6d52191d32fd94b4f1f5e299ae6b29b44da57
Patch0: %{gem_name}-fix-tests-failing-with-new-minitest.patch
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(json)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Journey is a router. It routes requests.


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

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl "}
testrb -Ilib -Itest test
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/journey.gemspec
%{gem_instdir}/test

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.4-2
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.4-1
- Updated to Journey 1.0.4.
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.3-1
- Rebuilt for scl.
- Updated to 1.0.3.

* Mon Jan 30 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.1-2
- Move README.rdoc containing license into main package.

* Fri Jan 27 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.1-1
- Initial package
