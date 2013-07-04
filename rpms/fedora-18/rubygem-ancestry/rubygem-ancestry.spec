%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ancestry

Summary: Organise ActiveRecord model into a tree structure
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.3.0
Release: 4%{dist}
Group: Development/Languages
License: MIT
URL: http://github.com/stefankroes/ancestry
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem-activerecord >= 2.2.2
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(ancestry) = %{version}

%description
Ancestry allows the records of a ActiveRecord model to be organised in a tree
structure, using a single, intuitively formatted database column. It exposes
all the standard tree structure relations (ancestors, parent, root, children,
siblings, descendants) and all of them can be fetched in a single sql query.
Additional features are named_scopes, integrity checking, integrity
restoration, arrangement of (sub)tree into hashes and different strategies
for dealing with orphaned records.

%description
TTFunk is a TrueType font parser written in pure ruby.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

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
mv %{buildroot}%{gem_instdir}/{MIT-LICENSE,README.rdoc} ./

%files
%doc MIT-LICENSE README.rdoc
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/init.rb
%{gem_instdir}/install.rb
%{gem_instdir}/ancestry.gemspec
%{gem_cache}
%{gem_spec}

%files doc
%{gem_docdir}

%changelog
* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> 1.3.0-4
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.0-2
- new package built with tito

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.3.0-1
- new package built with tito

