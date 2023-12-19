# template: default
%global gem_name sassc
%global gem_require_name %{gem_name}
%define debug_package %{nil}

Name: rubygem-%{gem_name}
Version: 2.4.0
Release: 2%{?dist}
Summary: Use libsass with Ruby!
License: MIT
URL: https://github.com/sass/sassc-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby-devel >= 2.0.0
BuildRequires: rubygems-devel
BuildRequires: rubygem(ffi) >= 1.9
BuildRequires: rubygem(ffi) < 2
# end specfile generated dependencies

BuildRequires: (libsass.so.1()(64bit) if libc.so.6()(64bit))
BuildRequires: (libsass.so.1 if libc.so.6)
Requires: (libsass.so.1()(64bit) if libc.so.6()(64bit))
Requires: (libsass.so.1 if libc.so.6)

%description
Use libsass with Ruby!


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

# disable building bundled libsass
sed -i "/s\.extensions/d" ../%{gem_name}-%{version}.gemspec

%build
# use libsass.so.1 from host
sed -i "s/libsass\.\#{dl_ext}/libsass\.\#{dl_ext}\.1/" lib/sassc/native.rb
sed -i "s!__dir__!\"%{_libdir}\"!" lib/sassc/native.rb

# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
ruby -I "%{buildroot}%{gem_libdir}" -e "require '%{gem_require_name}'"

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.gitmodules
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_instdir}/ext
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/sassc.gemspec
%{gem_instdir}/test

%changelog
* Tue Dec 19 2023 Evgeni Golov - 2.4.0-2
- Update libsass.so ABI to 1 for libsass >= 3.5

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.4.0-1
- Update to 2.4.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.1-3
- Rebuild against rh-ruby27

* Fri Mar 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.1-2
- Add check section to test native library

* Tue Jan 28 2020 Ondřej Ezr <oezr@redhat.com> 2.2.1-1
- Add rubygem-sassc generated by gem2rpm using the scl template

