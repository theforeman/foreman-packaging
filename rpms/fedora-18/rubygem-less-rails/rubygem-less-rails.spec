%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from less-rails-2.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name less-rails
%global rubyabi 1.9.1

Summary: The dynamic stylesheet language for the Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.2
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/metaskills/less-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
Requires: %{?scl_prefix}rubygem(less) => 2.3.1
Requires: %{?scl_prefix}rubygem(less) < 2.4
Requires: %{?scl_prefix}rubygem(actionpack) >= 3.1
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel 
BuildRequires: %{?scl_prefix}ruby 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The dynamic stylesheet language for the Rails asset pipeline. Allows other
gems to extend Less load path.


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

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.gitmodules}


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/.travis.yml
%{gem_instdir}/Appraisals
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Guardfile
%{gem_instdir}/gemfiles
%{gem_instdir}/test

%changelog
* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.3.2-4
- new package built with tito

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.3.2-3
- fix files section (msuchy@redhat.com)

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.3.2-2
- new package built with tito

* Fri Mar 29 2013 msuchy@redhat.com - 2.3.2-1
- Initial package
