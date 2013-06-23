%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name tire

Summary: Ruby client for the ElasticSearch search engine/database
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.13
Release: 7%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/karmi/tire
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.pre.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
Requires: %{?scl_prefix}rubygem-multi_json
Requires: %{?scl_prefix}rubygem(hashr) => 0.0.16
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby client for the ElasticSearch search engine/database

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}.pre

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
        %{gem_name}-%{version}.pre.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}.pre/
%doc %{gem_dir}/doc/%{gem_name}-%{version}.pre
%{gem_dir}/cache/%{gem_name}-%{version}.pre.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.pre.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.13-7
- new package built with tito

* Sun Aug 05 2012 Miroslav Suchý <msuchy@redhat.com> 0.3.13-6
- remove unused macros (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.3.13-5
- fix build directory (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.3.13-4
- edit spec for Fedora 17 (msuchy@redhat.com)

* Fri Jun 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.3.13-3
- rebuild

* Wed Feb 29 2012 Brad Buckingham <bbuckingham@redhat.com> 0.3.13-2
- tire - bumping release to 0.3.13-2, since 0.3.13-1 was previously tagged
  (bbuckingham@redhat.com)
- tire - upgrade to 0.3.13.pre (bbuckingham@redhat.com)

* Wed Feb 29 2012 Brad Buckingham <bbuckingham@redhat.com>
- tire - upgrade to 0.3.13.pre (bbuckingham@redhat.com)

* Tue Dec 20 2011 Shannon Hughes <shughes@redhat.com> 0.3.12-1
- modify version to match gem (shughes@redhat.com)

* Mon Dec 19 2011 Shannon Hughes <shughes@redhat.com> 0.3.13-1
- new package built with tito

* Wed Dec 14 2011 Justin Sherrill <jsherril@redhat.com> - 0.3.12-1
- Initial package
