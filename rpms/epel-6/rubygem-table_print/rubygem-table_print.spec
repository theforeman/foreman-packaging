%global gemname table_print

%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif
%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: TablePrint turns objects into nicely formatted columns for easy reading
Name: rubygem-%{gemname}
Version: 1.5.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/arches/table_print
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
%if 0%{?rhel} || 0%{?fedora} < 19
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
%if 0%{?rhel} || 0%{?fedora} < 19
BuildRequires: ruby(abi)
%endif
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

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
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec
%{geminstdir}/features
%{geminstdir}/spec
%{geminstdir}/Rakefile
%{geminstdir}/.rspec
%{geminstdir}/Gemfile
%exclude %{geminstdir}/%{gemname}.gemspec
%exclude %{geminstdir}/.document
%exclude %{geminstdir}/.gitignore
%exclude %{geminstdir}/.travis.yml

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/LICENSE.txt

%changelog
* Fri Mar 21 2014 Martin Bačovský <mbacovsk@redhat.com> 1.5.1-1
- Bump to 1.5.1 (mbacovsk@redhat.com)

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-3
- Fix up the spec's description and summary to remove rpmlint warnings
  (shk@redhat.com)

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-2
- new package built with tito

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-1
- Initial package creation
