# Generated from ruby-hmac-0.4.0.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ruby-hmac

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: This module provides common interface to HMAC functionality
Group: Development/Languages
License: FIXME
URL: http://ruby-hmac.rubyforge.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
This module provides common interface to HMAC functionality. HMAC is a kind of
"Message Authentication Code" (MAC) algorithm whose standard is documented in
RFC2104. Namely, a MAC provides a way to check the integrity of information
transmitted over or stored in an unreliable medium, based on a secret key.
Originally written by Daiki Ueno. Converted to a RubyGem by Geoffrey
Grosenbach.


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
%{gem_instdir}/Manifest.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 0.4.0-1
- Update to 0.4.0-1

* Wed Jun 15 2016 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- new package built with tito

