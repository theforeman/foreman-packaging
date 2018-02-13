%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from commonjs-0.2.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name commonjs

Summary: Provide access to your Ruby and Operating System runtime via the commonjs API
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.7
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/cowboyd/commonjs.rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Host CommonJS JavaScript environments in Ruby


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

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
%{gem_spec}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%{gem_instdir}/.travis.yml
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.2.7-5
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.2.7-4
- Use gem_install macro (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.7-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.2.7-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Oct 15 2014 Dominic Cleal <dcleal@redhat.com> 0.2.7-1
- Update 'commonjs' to 0.2.7 (ericdhelms@gmail.com)

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 0.2.6-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.6-4
- new package built with tito

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.6-3
- fix files section (msuchy@redhat.com)

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.2.6-2
- new package built with tito

* Fri Mar 29 2013 msuchy@redhat.com - 0.2.6-1
- Initial package
