%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from jquery-ui-rails-4.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-ui-rails
%global rubyabi 1.9.1

Summary: jQuery UI packaged for the Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.2
Release: 7%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/joliss/jquery-ui-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems) >= 1.3.6
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(railties) >= 3.1.0
Requires: %{?scl_prefix}rubygem(jquery-rails)
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel >= 1.3.6
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
jQuery UI's JavaScript, CSS, and image files packaged for the Rails 3.1+ asset
pipeline


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

rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.gitmodules,.travis.yml,Gemfile,Rakefile}



%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/License.txt
%doc %{gem_instdir}/History.md


%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 27 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-7
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-5
- fix files section (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-4
- fix files section (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-3
- new package built with tito

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 4.0.2-2
- new package built with tito

* Thu Mar 28 2013 msuchy@redhat.com - 4.0.2-1
- Initial package
