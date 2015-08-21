%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rabl

Summary: General ruby templating with json, bson, xml and msgpack support
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.11.6
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/nesquena/rabl
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygem(activesupport) >= 2.3.14
%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
RABL (Ruby API Builder Language) is a Rails and Padrino ruby
templating system for generating JSON, XML, MessagePack, PList and
BSON.

%package doc
BuildArch: noarch
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
rm %{buildroot}%{gem_instdir}/{README.md,CHANGELOG.md,CONTRIBUTING.md,MIT-LICENSE,.gitignore,\
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
%doc README.md CHANGELOG.md CONTRIBUTING.md
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
* Wed Jul 15 2015 Walden Raines <walden@redhat.com> 0.11.6-1
- Update rabl to 0.11.6 (walden@redhat.com)

* Tue Nov 25 2014 Dominic Cleal <dcleal@redhat.com> 0.11.4-1
- Update rabl to 0.11.4 (dcleal@redhat.com)

* Wed Jan 22 2014 Justin Sherrill <jsherril@redhat.com> 0.9.0-1
- upgrading to new rabl version 0.9.0 (jsherril@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.7.6-5
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.6-3
- new package built with tito

* Thu Nov 15 2012 Martin Bačovský <mbacovsk@redhat.com> 0.7.6-2
- Updated to 0.7.6 (mbacovsk@redhat.com)

* Mon Aug 20 2012 Ivan Necas <inecas@redhat.com> 0.7.1-1
- initial package
