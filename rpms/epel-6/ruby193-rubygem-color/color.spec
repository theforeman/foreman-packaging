%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name color

Summary: Colour management with Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.1
Release: 10%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://color.rubyforge.org/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The capabilities of the Color library are limited to pure mathematical
manipulation of the colours based on colour theory without reference to colour
profiles (such as sRGB or Adobe RGB). For most purposes, when working with the
RGB and HSL colours, this won't matter. However, some colour models (like CIE
L*a*b*) are not supported because Color does not yet support colour profiles,
giving no meaningful way to convert colours in absolute colour spaces (like
L*a*b*, XYZ) to non-absolute colour spaces (like RGB).



%prep
%setup -q -c -T -n  %{gem_name}-%{version}

%build
mkdir -p .%{gem_dir}


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
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Install.txt
%doc %{gem_instdir}/Licence.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 1.4.1-10
- fixing ruby193 scl package (lzap+git@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Tue Feb 26 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-9
- create directory in %%setup (msuchy@redhat.com)

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-8
- tune up spec for ruby193 SC (msuchy@redhat.com)

* Mon Feb 25 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-7
- new package built with tito

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 1.4.1-6
- edit spec for Fedora 17 (msuchy@redhat.com)

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com> 1.4.1-5

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com> 1.4.1-4
- another attempt at fixing version (shughes@redhat.com)

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com>
- fixing version (shughes@redhat.com)

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com>
- 

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com> 1.4.1-3
- fixing version (shughes@redhat.com)

* Wed Oct 12 2011 Shannon Hughes <shughes@redhat.com> 1.4.1-2
- fixing tag (shughes@redhat.com)

* Wed Oct 12 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.4.2-1
- Automatic commit of package [rubygem-color] release [1.4.1-2].
  (dmitri@redhat.com)
- fixed color.spec (dmitri@redhat.com)
- Automatic commit of package [rubygem-color] release [1.4.1-1].
  (dmitri@redhat.com)

* Tue Oct 11 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.4.1-2
- fixed color.spec (dmitri@redhat.com)

* Tue Oct 11 2011 Dmitri Dolguikh <dmitri@redhat.com> 1.4.1-1
- new package built with tito

* Tue Oct 11 2011  <wb@killing-time.appliedlogic.ca> - 1.4.1-1
- Initial package
