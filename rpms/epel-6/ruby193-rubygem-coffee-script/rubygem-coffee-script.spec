%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from coffee-script-2.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-script
%global rubyabi 1.9.1

Summary: Ruby CoffeeScript Compiler
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.2.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/josh/ruby-coffee-script
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# To get the tests:
# git clone https://github.com/josh/ruby-coffee-script && cd ruby-coffee-script
# git checkout v2.2.0 && tar czf coffee-script-tests-2.2.0.tgz test/
Source1: coffee-script-tests-%{version}.tgz
# Proposed upstream https://github.com/josh/ruby-coffee-script/pull/16
# For initial report see https://github.com/josh/ruby-coffee-script/issues/15
Patch0: coffee-script-fix-newlines-in-tests.patch
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(coffee-script-source)
Requires: %{?scl_prefix}rubygem(execjs)
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(coffee-script-source)
BuildRequires: %{?scl_prefix}rubygem(execjs)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(therubyracer)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby CoffeeScript is a bridge to the JS CoffeeScript compiler.


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

%check
pushd .%{gem_instdir}
# unpack and patch the tests
tar xzf %{SOURCE1}
patch -p1 < %{PATCH0}

%{?scl:scl enable %{scl} "}
testrb -Ilib test
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.2.0-3
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.2.0-2
- Introduce test suite.
- Specfile cleanup

* Tue Jul 17 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.2.0-1
- Initial package
