# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rsec

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.3
Release: 3%{?dist}
Summary: Extreme Fast Parser Combinator for Ruby
Group: Development/Languages
License: Ruby or BSD
URL: http://rsec.herokuapp.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9.1
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9.1
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Easy and extreme fast dynamic PEG parser combinator.


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
%{gem_libdir}
%license %{gem_instdir}/license.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/bench
%doc %{gem_docdir}
%{gem_instdir}/examples
%doc %{gem_instdir}/readme.rdoc
%{gem_instdir}/test

%changelog
* Tue Oct 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.4.3-3
- Update and rebuild into SCL

* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 0.4.3-2
- Update to add SCL build support

* Wed Mar 13 2019 Evgeni Golov 0.4.3-1
- Update to 0.4.3

* Thu May 25 2017 Dominic Cleal <dominic@cleal.org> 0.4.2-1
- new package built with tito

