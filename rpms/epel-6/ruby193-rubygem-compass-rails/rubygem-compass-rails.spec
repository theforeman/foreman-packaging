%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name compass-rails
%global rubyabi 1.9.1

Summary:       Integrate Compass into Rails 2.3 and up
Name:          %{?scl_prefix}rubygem-%{gem_name}
Version:       1.0.3
Release:       8%{?dist}
Group:         Development/Languages
License:       MIT
URL:           https://github.com/Compass/compass-rails
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:      %{?scl_prefix}rubygems
Requires:      %{?scl_prefix}rubygem(compass) >= 0.12.2
Requires:      %{?scl_prefix}rubygem(actionpack)
Requires:      %{?scl_prefix}rubygem(rails)
Requires:      %{?scl_prefix}rubygem(sass-rails)
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
# For tests
#BuildRequires: %{?scl_prefix}rubygem(test-unit)
#BuildRequires: %{?scl_prefix}rubygem(compass) >= 0.12.2
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Integrate Compass into Rails 2.3 and up.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}


%build
mkdir -p ./%{gem_dir}

%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --bindir ./%{_bindir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# Cleanup stuff
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -f %{buildroot}%{gem_instdir}/*.gemspec
rm -rf %{buildroot}%{gem_instdir}/.yardoc
find %{buildroot} -iname .gitkeep -exec rm -f {} \;
chmod 0755 %{buildroot}%{gem_instdir}/Rakefile

%check
# Dont run tests until they get cleaned up, upstream
#pushd ./%{gem_instdir}
%{?scl:scl enable %{scl} "}
#testrb2 -Ilib test
%{?scl:"}
#popd

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/Appraisals
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%{gem_instdir}/gemfiles

%changelog
* Mon Mar 25 2013 Marek Hulan <ares@igloonet.cz> 1.0.3-8
- fix of SCL spec

* Mon Mar 25 2013 Marek Hulan <ares@igloonet.cz> 1.0.3-7
- new package built with tito

* Thu Feb 14 2013 Troy Dawson <tdawson@redhat.com> - 1.0.3-6
- Fix requires for 3.1+ rails versions (#901540)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Troy Dawson <tdawson@redhat.com> - 1.0.3-3
- removed Requires: ruby
- added gemfiles to doc
- comment out tests until upstream cleans them up

* Wed Dec 05 2012 Troy Dawson <tdawson@redhat.com> - 1.0.3-2
- Fixup spec file
- Added rubgem-compass for BuildRequires

* Tue Sep 11 2012 Troy Dawson <tdawson@redhat.com> - 1.0.3-1
- Initial package
