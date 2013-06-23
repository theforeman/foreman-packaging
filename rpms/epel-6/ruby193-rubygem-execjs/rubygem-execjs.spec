%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from execjs-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name execjs
%global rubyabi 1.9.1

Summary: Run JavaScript code from Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.0
Release: 5%{?dist}
Group: Development/Languages
# Public Domain: %%{gem_libdir}/execjs/support/json2.js
License: MIT and Public Domain
URL: https://github.com/sstephenson/execjs
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sstephenson/execjs.git && cd execjs
# git checkout v1.4.0 && tar czf execjs-1.4.0-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(multi_json) => 1.0
Requires: %{?scl_prefix}rubygem(multi_json) < 2
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(multi_json) => 1.0
BuildRequires: %{?scl_prefix}rubygem(multi_json) < 2
BuildRequires: %{?scl_prefix}rubygem(therubyracer)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
ExecJS lets you run JavaScript code from Ruby. It automatically picks the
best runtime available to evaluate your JavaScript program, then returns
the result to you as a Ruby object.

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
tar xzf %{SOURCE1}
# disable test that needs internet connection
sed -i '163,168d' test/test_execjs.rb
export LANG=en_US.utf8
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
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.0-5
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.0-4
- Reimported from Fedora.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.0-2
- Removed the duplicated "git checkout" in comment.
- BR: rubygem(therubyracer) for tests, don't use deprecated js.

* Wed Jun 13 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.0-1
- Initial package
