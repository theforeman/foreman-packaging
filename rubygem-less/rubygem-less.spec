%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from less-2.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name less
%global rubyabi 1.9.1

Summary: Leaner CSS, in your browser or Ruby (via less.js)
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.5.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://lesscss.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}ruby 
Requires: %{?scl_prefix}rubygem(commonjs) => 0.2.7
Requires: %{?scl_prefix}rubygem(commonjs) < 0.3
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel 
BuildRequires: %{?scl_prefix}ruby 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Invoke the Less CSS compiler from Ruby


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
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.gitmodules}

%files
%dir %{gem_instdir}
%{_bindir}/lessc
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_spec}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Changelog.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/.travis.yml
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Oct 14 2014 Dominic Cleal <dcleal@redhat.com> 2.5.1-1
- Updating 'rubygem-less' and 'rubygem-less-rails' (ericdhelms@gmail.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 2.3.1-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.3.1-4
- new package built with tito

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.3.1-3
- fix files section (msuchy@redhat.com)

* Fri Mar 29 2013 Miroslav Suchý <msuchy@redhat.com> 2.3.1-2
- new package built with tito

* Fri Mar 29 2013 msuchy@redhat.com - 2.3.1-1
- Initial package
