%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name jquery-turbolinks

Summary: jQuery plugin for binded events problem caused by Turbolinks
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/kossnocorp/jquery.turbolinks
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}rubygem(railties) >= 3.1.0
Requires: %{?scl_prefix}rubygem(turbolinks)

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Do you like Turbolinks? It's easy and fast way to improve user experience of
surfing on your website.

But if you have a large codebase with lots of $(el).bind(...) Turbolinks will
surprise you. Most part of your JavaScripts will stop working in usual way.
It's because the nodes on which you bind events no longer exist.

I wrote jquery.turbolinks to solve this problem in my project. It's easy to
use: just require it immediately after jquery.js. Your other scripts should be
loaded after jquery.turbolinks.js, and turbolinks.js should be after your
other scripts.

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

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/src
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.md

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile*
%exclude %{gem_instdir}/Guardfile
%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_instdir}/package.json

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/NOTES.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec
%{gem_instdir}/Rakefile

%changelog
* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 2.1.0-1
- new package built with tito
