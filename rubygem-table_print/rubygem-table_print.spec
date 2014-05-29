%global gem_name table_print

Summary: TablePrint turns objects into nicely formatted columns for easy reading
Name: rubygem-%{gem_name}
Version: 1.5.1
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/arches/table_print
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
Requires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
TablePrint turns objects into nicely formatted columns for easy reading.
Works great in rails console, works on pure ruby objects, auto-detects
columns, lets you traverse ActiveRecord associations. Simple, powerful.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%{gem_instdir}/features
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE.txt

%changelog
* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.5.1-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Fri Mar 21 2014 Martin Bačovský <mbacovsk@redhat.com> 1.5.1-1
- Bump to 1.5.1 (mbacovsk@redhat.com)

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-3
- Fix up the spec's description and summary to remove rpmlint warnings
  (shk@redhat.com)

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-2
- new package built with tito

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-1
- Initial package creation
