%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ruby-rc4

Summary: Pure Ruby implementation of the RC4 algorithm
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.5
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/caiges/Ruby-RC4
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
%if 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygem-rspec
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
RC4 is a pure Ruby implementation of the RC4 algorithm.

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
rm %{buildroot}%{gem_instdir}/{README.md,LICENSE}

%check
%if 0%{?fedora} > 16
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
rspec spec/
%{?scl:"}
popd
%endif

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_cache}
%{gem_spec}
%doc LICENSE

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%doc README.md
%{gem_instdir}/spec

%changelog
* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.5-5
- new package built with tito

* Wed Aug 15 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.5-4
- do not run test on Fedora 16 and el6 (msuchy@redhat.com)

* Wed Aug 15 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.5-3
- 845819 - run test suite in instdir (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.5-2
- use test suite (msuchy@redhat.com)
- edit spec for Fedora review (msuchy@redhat.com)

* Sun Aug 05 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.5-1
- new package built with tito


