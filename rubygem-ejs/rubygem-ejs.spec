%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from ejs-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ejs

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.1
Release: 3%{?dist}
Summary: EJS (Embedded JavaScript) template compiler
Group: Development/Languages
License: MIT
URL: https://github.com/sstephenson/ruby-ejs/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sstephenson/ruby-ejs/ && cd ruby-ejs/
# git checkout v1.1.1 && tar czf ejs-1.1.1-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ror}rubygem(execjs)
BuildRequires: %{?scl_prefix_ruby}rubygem(test-unit)
BuildRequires: %{?scl_prefix_ror}rubygem(therubyracer)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Compile and evaluate EJS (Embedded JavaScript) templates from Ruby.

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

# Run the test suite
%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}

%{?scl:scl enable %{scl} %{scl_v8} - << \EOF}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
%{?scl:EOF}
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
* Thu Jan 14 2016 Daniel Lobato Garcia <elobatocs@gmail.com> - 1.1.1-3
- Changes to adapt to tfm SCL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Vít Ondruch <vondruch@redhat.com> - 1.1.1-1
- Initial package
