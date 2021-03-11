%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name awesome_print

Summary: Pretty print Ruby objects with proper indentation and colors
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.0
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/awesome-print/awesome_print
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
#BuildRequires: %{?scl_prefix}rubygem-rspec

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Great Ruby debugging companion: pretty print Ruby objects to visualize their
structure. Supports custom object formatting via plugins.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

# not running tests since it's broken in mock
#%check
#pushd ./%{gem_instdir}
%{?scl:scl enable %{scl} "}
#rspec -Ilib spec/
%{?scl:"}
#popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
echo %{gem_dir}
echo %{buildroot}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.gitignore
rm %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/Gemfile.lock
chmod -x %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/lib/awesome_print/formatter.rb
chmod -x %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/lib/ap.rb
chmod -x %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/lib/awesome_print/inspector.rb
chmod -x %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/lib/awesome_print.rb


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%{gem_instdir}/LICENSE
%{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/LICENSE
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/README.md
%{gem_instdir}/Appraisals
%{gem_instdir}/spec/
%{gem_instdir}/spec/colors_spec.rb
%{gem_instdir}/spec/formats_spec.rb
%{gem_instdir}/spec/methods_spec.rb
%{gem_instdir}/spec/objects_spec.rb
%{gem_instdir}/spec/spec_helper.rb
%{gem_instdir}/Rakefile

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.8.0-6
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.0-5
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.0-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 23 2018 Daniel Lobato Garcia <me@daniellobato.me> 1.8.0-2
- Bump rubygem-awesome_print to 1.8.0 (github@kohlvanwijngaarden.nl)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.7.0-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Sun Jun 12 2016 Dominic Cleal <dominic@cleal.org> 1.7.0-1
- Bump rubygem-awesome_print to 1.7.0 (akofink@redhat.com)
- Remove unused non-SCL gem (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-13
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-12
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-11
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.0.2-10
- Modernise and update for EL7 (dcleal@redhat.com)

* Thu Aug 15 2013 Sam Kottler <shk@redhat.com> 1.0.2-9
- Make the spec work on fedora + RHEL + scl (shk@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.2-7
- new package built with tito

* Fri Oct 26 2012  <mzatko@redhat.com> - 1.0.2-6
- Owning spec directory

* Thu Oct 04 2012  <mzatko@redhat.com> - 1.0.2-5
- Moved specs into docs, using rm instead of exclude
- Not removing Gemfile

* Thu Sep 20 2012  <mzatko@redhat.com> - 1.0.2-4
- Renamed spec file to rubygem_awesome_print.spec

* Tue Sep 04 2012  <mzatko@redhat.com> - 1.0.2-3
- Added license file to doc, files in doc use docdir instead of instdir

* Mon Sep 03 2012  <mzatko@redhat.com> - 1.0.2-2
- Removed unnecessary files & corrected license

* Wed Jul 11 2012  <mzatko@redhat.com> - 1.0.2-1
- Initial package
