%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name bootstrap-datepicker-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.7.1.1
Release: 2%{?dist}
Summary: A date picker for Twitter Bootstrap
Group: Development/Languages
License: MIT
URL: https://github.com/Nerian/bootstrap-datepicker-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A date picker for Twitter Bootstrap

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
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/.*

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.7.1.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.7.1.1-1
- Update rubygem-bootstrap-datepicker-rails to 1.7.1.1 (ericdhelms@gmail.com)

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.6.1.1-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Fri Jun 10 2016 Dominic Cleal <dominic@cleal.org> 1.6.1.1-1
- new package built with tito

