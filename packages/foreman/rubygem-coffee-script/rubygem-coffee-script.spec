# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name coffee-script

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.4.1
Release: 5%{?dist}
Summary: Ruby CoffeeScript Compiler
Group: Development/Languages
License: MIT
URL: http://github.com/josh/ruby-coffee-script
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(coffee-script-source)
Requires: %{?scl_prefix}rubygem(execjs)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 2.4.1

%description
Ruby CoffeeScript is a bridge to the JS CoffeeScript compiler.


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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.4.1-5
- Rebuild against rh-ruby27

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.1-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.1-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.4.1-2
- Bump for moving over to foreman-packaging

* Wed Aug 15 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.4.1-1
- Initial package
