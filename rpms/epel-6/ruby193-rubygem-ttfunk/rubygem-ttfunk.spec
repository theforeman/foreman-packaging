%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ttfunk

Summary: Font Metrics Parser for Prawn
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.3
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2 or GPLv3 or Ruby
URL: https://github.com/prawnpdf/ttfunk
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

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
mv %{buildroot}%{gem_instdir}/{CHANGELOG,COPYING,GPLv2,GPLv3,LICENSE,README.rdoc} ./

%files
%doc COPYING GPLv2 GPLv3 LICENSE
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc README.rdoc CHANGELOG
%{gem_instdir}/data
%{gem_instdir}/examples
%doc %{gem_docdir}

%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.3-5
- new package built with tito

* Thu Aug 16 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.3-4
- 845805 - move CHANGELOG to -doc package (msuchy@redhat.com)

* Thu Aug 16 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.3-3
- 845805 - move README.rdoc to -doc subpackage (msuchy@redhat.com)
- 845805 - mark gem_docdir as %%doc and exclude gem_cache (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.3-2
- fix spec for fedora review (msuchy@redhat.com)

* Sun Aug 05 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.3-1
- new package built with tito

