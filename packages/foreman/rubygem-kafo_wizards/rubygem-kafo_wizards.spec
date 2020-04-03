# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name kafo_wizards

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.1
Release: 4%{?dist}
Summary: Wizard like interfaces in terminal
Group: Development/Languages
License: GPLv3+
URL: https://github.com/theforeman/kafo_wizards
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(highline)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%{?scl:Obsoletes: rubygem-%{gem_name} <= 0.0.1}

%description
This gem helps to create wizard like interfaces in terminal applications, has
support for nesting and value validation.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Fri Apr 03 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.1-4
- Obsolete non-scl version

* Thu Apr 02 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.1-3
- Build for SCL

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-2
- Use gem_install macro (dominic@cleal.org)

* Tue Jan 26 2016 Dominic Cleal <dcleal@redhat.com> 0.0.1-1
- new package built with tito

