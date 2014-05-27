%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name awesome_print

Summary: Pretty print Ruby objects with proper indentation and colors
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.2
Release: 9%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/michaeldv/awesome_print
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires:      %{?scl_prefix}ruby(abi)
BuildRequires: %{?scl_prefix}ruby(abi)
%else
Requires:      %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
%endif

BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
#BuildRequires: %{?scl_prefix}rubygem-rspec

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Great Ruby debugging companion: pretty print Ruby objects to visualize their
structure. Supports custom object formatting via plugins.


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
%{gem_instdir}/CHANGELOG
%{gem_instdir}/README.md
%{gem_instdir}/spec/
%{gem_instdir}/spec/colors_spec.rb
%{gem_instdir}/spec/formats_spec.rb
%{gem_instdir}/spec/methods_spec.rb
%{gem_instdir}/spec/objects_spec.rb
%{gem_instdir}/spec/spec_helper.rb
%{gem_instdir}/Rakefile

%changelog
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
