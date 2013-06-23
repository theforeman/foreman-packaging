%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ruby-progressbar
%global rubyabi 1.9.1

Summary: Ruby/ProgressBar is a flexible text progress bar library for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.2
Release: 7%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/jfelchner/ruby-progressbar
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygem(rdoc)
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

# for check section
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(simplecov)
%endif

%description
Ruby/ProgressBar is an extremely flexible text progress bar library for Ruby.
The output can be customized with a flexible formatting system including:
percentage, bars of various formats, elapsed time and estimated time
remaining.


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
gem install --local --install-dir .%{gem_dir} --no-ri \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.rspec,.rvmrc,.travis.yml,.yardoc}

%check
pushd .%{gem_instdir}
%if 0%{?fedora} > 18
%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
%endif
popd



%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/spec
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%{gem_instdir}/Guardfile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.2-7
- new package built with tito

* Fri Dec 07 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.2-6
- add BR on rubygem(rdoc) (msuchy@redhat.com)

* Fri Dec 07 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.2-5
- do not generate documentation (msuchy@redhat.com)

* Tue Dec 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.2-4
- fix files section (msuchy@redhat.com)

* Tue Dec 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.2-3
- simplecov is only available in rawhide (F19) for now (msuchy@redhat.com)

* Tue Dec 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.2-2
- new package built with tito

* Tue Dec 04 2012 Miroslav Suchý <msuchy@redhat.com> - 1.0.2-1
- Initial package
