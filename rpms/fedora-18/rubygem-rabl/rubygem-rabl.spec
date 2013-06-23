%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rabl

Summary: General ruby templating with json, bson, xml and msgpack support
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.6
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/nesquena/rabl
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(activesupport) >= 2.3.14
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.0
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
RABL (Ruby API Builder Language) is a Rails and Padrino ruby
templating system for generating JSON, XML, MessagePack, PList and
BSON.

%package doc
BuildArch: noarch
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary: Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
# Create the gem as gem install only works on a gem file
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}
rm -rf ./%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm %{buildroot}%{gem_instdir}/{README.md,CHANGELOG.md,TODO,MIT-LICENSE,.gitignore,\
.travis.yml,rabl.gemspec,test.watchr}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_cache}
%{gem_spec}
%doc MIT-LICENSE

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%doc README.md CHANGELOG.md TODO
%{gem_instdir}/test
%{gem_instdir}/fixtures
%{gem_instdir}/examples

%check
# Running tests requires: rubygem-riot, rubygem-tilt,
# rubygem-yajl-ruby, rubygem-msgpack, rubygem-bson, rubygem-plist
# Deps not available in RPMs, skipping for nown
# Running manually was green
# rake test

%changelog
* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.6-3
- new package built with tito

* Thu Nov 15 2012 Martin Bačovský <mbacovsk@redhat.com> 0.7.6-2
- Updated to 0.7.6 (mbacovsk@redhat.com)

* Mon Aug 20 2012 Ivan Necas <inecas@redhat.com> 0.7.1-1
- initial package

