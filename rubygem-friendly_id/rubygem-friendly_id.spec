%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name friendly_id
%global rubyabi 1.9.1

Summary: Swiss Army bulldozer of slugging and permalinks for Active Record
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.10.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/norman/friendly_id
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

Requires: %{?scl_prefix_ruby}rubygem-activerecord >= 1:3.0
Requires: %{?scl_prefix_ruby}rubygem-activerecord < 1:4.0

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Ruby on Rails. It allows you to create pretty URLs and work with
human-friendly strings as if they were numeric ids for Active Record models.


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
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/friendly_id.gemspec
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/WhatsNew.md
%{gem_instdir}/bench.rb
%{gem_instdir}/Gemfile
%{gem_instdir}/gemfiles
%{gem_instdir}/Guide.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Mon Sep 29 2014 Dominic Cleal <dcleal@redhat.com> 4.0.10.1-1
- new package built with tito
