%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name roadie-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Hooks Roadie into your Rails application to help with email generation
Group: Development/Languages
License: MIT
URL: https://github.com/Mange/roadie-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.0
Requires: %{?scl_prefix_ror}rubygem(railties) < 5.2
Requires: %{?scl_prefix}rubygem(roadie) >= 3.1
Requires: %{?scl_prefix}rubygem(roadie) < 4.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem hooks up your Rails application with Roadie to help you
generate HTML emails.

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
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}/%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/codecov.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/Upgrading.md
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/setup.sh
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/.*

%changelog
* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.1-1
- Bump roadie-rails to 1.2.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 1.1.1-1
- new package built with tito

