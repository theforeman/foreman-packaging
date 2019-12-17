# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.2.1
Release: 2%{?dist}
Summary: Full-stack web application framework
Group: Development/Languages
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 5.2.1

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.2.2
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.8.11
Requires: %{?scl_prefix_ror}rubygem(activesupport) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(actionpack) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(actionview) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(activemodel) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(activerecord) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(actionmailer) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(activejob) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(actioncable) = 5.2.1
Requires: %{?scl_prefix}rubygem(activestorage) = 5.2.1
Requires: %{?scl_prefix_ror}rubygem(railties) = 5.2.1
Requires: %{?scl_prefix_ruby}rubygem(bundler) >= 1.3.0
Requires: %{?scl_prefix_ror}rubygem(sprockets-rails) >= 2.0.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.2
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.8.11
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


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

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 5.2.1-2
- Bump for moving over to foreman-packaging

* Wed Aug 22 2018 Eric D. Helms <ericdhelms@gmail.com> 5.2.1-1
- Release tfm-ror52-rubygem-rails 5.2.1

* Fri Aug 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-2
- Fix bundler requires

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-1
- Initial package
