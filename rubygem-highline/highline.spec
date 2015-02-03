%{?scl:%scl_package rubygem-%{gemname}}
%{!?scl:%global pkg_name %{name}}

# check files-sections at the end of this file and
# EDIT this section

%global gem_name highline

%define _version 1.6.21
%define _summary HighLine is a high-level command-line IO library
%define _url https://github.com/JEG2/highline
%define _license GPLv2+ or Ruby

# add gem dependencies, e.g. "Requires: %{?scl_prefix_ruby}rubygem(rails) > 3.2"

# end of EDIT

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   %{_version}
Release:   2%{?dist}
Summary:   %{_summary}
Group:     Development/Languages
License:   %{_license}
URL:       %{_url}
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
Requires:  %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires:  %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif
Requires:  %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

%description
A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%if 0%{?fedora} > 18
%gem_install
%else
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V --local --install-dir .%{gem_dir} --force --rdoc \
    %{gem_name}-%{version}.gem
%{?scl:"}
%endif

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%defattr(-, root, root, -)

%{gem_dir}/gems/%{gem_name}-%{version}/

%doc %{gem_dir}/doc/%{gem_name}-%{version}


%doc %{gem_instdir}/README.rdoc

%doc %{gem_instdir}/INSTALL

%doc %{gem_instdir}/TODO

%doc %{gem_instdir}/CHANGELOG

%doc %{gem_instdir}/LICENSE

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.6.21-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Mon Mar 10 2014 Marek Hulan <mhulan@redhat.com> 1.6.21-1
- Update highline to 1.6.21 (mhulan@redhat.com)

* Mon Nov 18 2013 Marek Hulan <mhulan@redhat.com> 1.6.20-2
- SCLize highline (mhulan@redhat.com)

* Mon Nov 18 2013 Marek Hulan <mhulan@redhat.com> 1.6.20-1
- Bump Highline (mhulan@redhat.com)

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 1.6.1-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 1.6.1-1
- Initial package
