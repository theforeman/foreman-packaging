%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from coffee-script-source-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-script-source

%global rubyabi 1.9.1

Summary:        The CoffeeScript Compiler
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.3.3
Release:        4%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://jashkenas.github.com/coffee-script/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:       %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:       %{?scl_prefix}ruby(rubygems)
BuildRequires:  %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildRequires:  %{?scl_prefix}ruby
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
CoffeeScript is a little language that compiles into JavaScript.
Underneath all of those embarrassing braces and semicolons,
JavaScript has always had a gorgeous object model at its heart.
CoffeeScript is an attempt to expose the good parts of JavaScript
in a simple way.


%package doc
Summary:    Documentation for %{pkg_name}
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch:  noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.3-4
- new package built with tito

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-3
- Imported from Fedora again.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.3-1
- Updated to the coffee-script-source 1.3.3.

* Wed Feb 29 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-2
- Rebuilt with new gem_* macros

* Mon Feb 27 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-1
- Initial package
