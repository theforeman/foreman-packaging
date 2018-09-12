%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name wicked

%define _version 1.3.2
%define _summary Wicked is a Rails engine for producing easy wizard controllers
%define _url https://github.com/schneems/wicked

%define desc Wicked is a Rails engine for producing easy wizard controllers

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   3%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   MIT
URL:       %{_url}
Source0:   https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires:  %{?scl_prefix_ruby}ruby(release)
Requires:  %{?scl_prefix_ruby}rubygems
Requires:  %{?scl_prefix_ror}rubygem(railties) >= 3.0.7

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

%description
%{desc}

%package   doc
BuildArch: noarch
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:   Documentation for %{pkg_name}

%description doc
This package contains documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/wicked.gemspec
%exclude %{gem_instdir}/Appraisals
%exclude %{gem_instdir}/gemfiles
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/Rakefile
%license %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/.gitignore

%files doc
%doc %{gem_instdir}/test
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}/rdoc
%doc %{gem_docdir}/ri
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 1.3.2-3
- Remove the use of the _license macro and just hard code it in the License line

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 11 2018 Eric D. Helms <ericdhelms@gmail.com> 1.3.2-1
- Bump rubygem-wicked to 1.3.2 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-2
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Nov 03 2014 Daniel Lobato Garcia <dlobatog@redhat.com> 1.1.0-1
- Update release to 1.1.0 (dlobatog@redhat.com)

* Fri Jun 06 2014 Dominic Cleal <dcleal@redhat.com> 1.0.2-3
- Modernise and update for EL7 (dcleal@redhat.com)

* Tue Apr 08 2014 Marek Hulan <mhulan@redhat.com> 1.0.2-2
- Fixing wicked-doc dependency (mhulan@redhat.com)

* Wed Apr 02 2014 Marek Hulan <mhulan@redhat.com> 1.0.2-1
- new package built with tito
