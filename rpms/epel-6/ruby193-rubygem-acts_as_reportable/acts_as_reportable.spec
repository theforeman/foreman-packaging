%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name acts_as_reportable

Summary: ActiveRecord support for Ruby Reports
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.1
Release: 13%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyreports.org
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
acts_as_reportable provides ActiveRecord support for Ruby Reports

%prep
%setup -q -c -T -n  %{gem_name}-%{version}

%build
mkdir -p .%{gem_dir}

# We set that to be a local directory so that we can move it into the
# buildroot in %%install
%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{SOURCE0}
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/

%doc %{gem_dir}/doc/%{gem_name}-%{version}


%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 1.1.1-13
- fixing acts_as_reportable
- require ruby193-build for tagging

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.1-12
- tune up spec for SC (msuchy@redhat.com)

* Sun Feb 24 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.1-11
- require rubygems-devel (msuchy@redhat.com)

* Sun Feb 24 2013 Miroslav Suchý <msuchy@redhat.com> 1.1.1-10
- new package built with tito

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-9
- fix BR condition (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-8
- fix BR condition (msuchy@redhat.com)

* Tue Jul 03 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-7
- narrow BR condition for fedora (msuchy@redhat.com)

* Tue Jul 03 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-6
- ruby macros in fedora are defined in rubygems-devel (msuchy@redhat.com)

* Tue Jul 03 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-5
- define gem_dir even on Fedora 16 (msuchy@redhat.com)

* Tue Jul 03 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-4
- gem_name should be defined on all platforms (msuchy@redhat.com)

* Tue Jul 03 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-3
- edit spec for Fedora 17

* Thu Oct 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.1.1-2
- fixed acts_as_reportable spec file (dmitri@redhat.com)

* Thu Oct 06 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.1.1-1
- new package built with tito

* Thu Oct 06 2011  <wb@killing-time.appliedlogic.ca> - 1.1.1-1
- Initial package
