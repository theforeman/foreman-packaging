%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name unicode

Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        0.4.4.1
Release:        5%{?dist}
Summary:        Unicode normalization library for Ruby
License:        Ruby
URL:            http://www.yoshidam.net/Ruby.html#unicode
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/blackwinter/unicode/issues/7
Source1:        https://www.ruby-lang.org/en/about/license.txt
# This is a C extension linked against MRI, it's not compatible with other
# interpreters. So we require MRI specifically instead of ruby(release).
Requires:       %{?scl_prefix_ruby}ruby
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix_ruby}ruby-devel
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}


%description
Unicode normalization library for Ruby.


%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
cp -p %{SOURCE1} .
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/specifications %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_instdir}
cp -pa .%{gem_instdir}/lib %{buildroot}%{gem_instdir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -pa .%{gem_extdir_mri}/%{gem_name} %{buildroot}%{gem_extdir_mri}/
touch %{buildroot}%{gem_extdir_mri}/gem.build_complete


%check
%{?scl:scl enable %{scl} - << \EOF}
ruby -I.%{gem_instdir}/lib:.%{gem_extdir_mri} test/test.rb
%{?scl:EOF}


%files
%doc README
%license license.txt
%{gem_instdir}
%{gem_extdir_mri}
%{gem_spec}


%changelog
* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.4.1-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.4.1-4
- Final set of rebuilds (ericdhelms@gmail.com)

* Wed Sep 27 2017 Eric D. Helms <ericdhelms@gmail.com> 0.4.4.1-3
- rubygem-unicode: Fix provides & native extensions
  (ewoud@kohlvanwijngaarden.nl)

* Tue Sep 26 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.4.4.1-2
- new package built with tito

* Mon Jul 14 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-2
- run test program in %%check
- use HTTPS for Ruby license source URL

* Thu Jun 05 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-1
- updated to upstream release 0.4.4.1
- fixed spec for rubygem changes in F21+

* Tue Jan 28 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4-1
- Initial package
