# template: default
%global gem_name stomp

Name: rubygem-%{gem_name}
Version: 1.4.10
Release: 1%{?dist}
Summary: Ruby client for the Stomp messaging protocol
License: Apache-2.0
URL: https://github.com/stompgem/stomp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Ruby client for the Stomp messaging protocol.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/catstomp
%{_bindir}/stompcat
%license %{gem_instdir}/LICENSE
%{gem_instdir}/adhoc
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/notes
%{gem_instdir}/spec
%exclude %{gem_instdir}/stomp.gemspec
%{gem_instdir}/test

%changelog
* Sun Jul 24 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.10-1
- Update to 1.4.10

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.4.9-2
- Rebuild for Ruby 2.7

* Fri Jan 31 2020 Jonathon Turel <jturel@gmail.com> 1.4.9-1
- Add rubygem-stomp generated by gem2rpm using the scl template

