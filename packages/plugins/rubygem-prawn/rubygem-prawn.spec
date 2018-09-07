%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name prawn

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.2.2
Release: 2%{?dist}
Summary: A fast and nimble PDF generator for Ruby
Group: Development/Languages
License: (GPLv2 or GPLv3 or Ruby) and APAFML
URL: http://prawnpdf.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.1
Requires: %{?scl_prefix_ruby}ruby < 3
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.6
Requires: %{?scl_prefix}rubygem(ttfunk) >= 1.5
Requires: %{?scl_prefix}rubygem(ttfunk) < 2
Requires: %{?scl_prefix}rubygem(pdf-core) >= 0.7.0
Requires: %{?scl_prefix}rubygem(pdf-core) < 0.8
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.1
BuildRequires: %{?scl_prefix_ruby}ruby < 3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.6
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Prawn is a fast, tiny, and nimble PDF generator for Ruby.


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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_instdir}/data
%{gem_libdir}
%{gem_instdir}/manual
%exclude %{gem_instdir}/prawn.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

