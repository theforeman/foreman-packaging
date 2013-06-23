%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name wirb
Summary: Wavy IRB: Colorizes irb results.
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.4.2
Release: 4%{dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/janlelis/wirb
Source0: %{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(wirb) = %{version}

%define gembuilddir %{buildroot}%{gem_dir}

%description
Wavy IRB: Colorizes irb results. It originated from Wirble, but only provides
result highlighting. Just call Wirb.start and enjoy the colors in your IRB ;).
You can use it with your favorite colorizer engine. See README.rdoc for more
details.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{?scl:"}
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/.gemtest

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/data
%doc %{gem_instdir}/COPYING.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/spec
%doc %{gem_dir}/doc/wirb-0.4.2
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.2-4
- put correct license in spec (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.2-3
- new package built with tito

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.4.2-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 0.4.2-1
- new package built with tito

