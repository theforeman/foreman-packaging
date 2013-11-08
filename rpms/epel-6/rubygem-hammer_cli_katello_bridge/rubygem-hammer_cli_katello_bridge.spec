%global gemname hammer_cli_katello_bridge

%if 0%{?rhel}
%global gem_dir /usr/lib/ruby/gems/1.8
%endif

%global geminstdir %{gem_dir}/gems/%{gemname}-%{version}

Summary: Katello command plugin for the Hammer CLI
Name: rubygem-%{gemname}
Version: 0.0.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/theforeman/hammer-cli-katello-bridge
Source0: %{gemname}-%{version}.gem

%if 0%{?rhel} == 6 || 0%{?fedora} < 19
Requires: ruby(abi)
%endif
Requires: ruby(rubygems)
Requires: rubygem(hammer_cli)
BuildRequires: ruby(rubygems)
%if 0%{?fedora}
BuildRequires: rubygems-devel
%endif
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Katello command plugin for the Hammer CLI.


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

%install
mkdir -p %{buildroot}/etc/foreman
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/katello.json
/etc/foreman
%exclude %{gem_dir}/cache/%{gemname}-%{version}.gem
%{gem_dir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gemname}-%{version}


%changelog
* Fri Nov 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.7-1
- Bump to 0.0.7 (mbacovsk@redhat.com)

* Wed Oct 09 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.6-1
- Bumped to 0.0.6 (mbacovsk@redhat.com)
- added missing CLI definition file

* Tue Oct 08 2013 Martin Bačovský <mbacovsk@redhat.com> 0.0.4-1
- Bump to 0.0.4 (mbacovsk@redhat.com)

* Thu Sep 26 2013 Sam Kottler <shk@redhat.com> 0.0.3-1
- Bump the version to 0.0.3 (shk@redhat.com)

* Thu Aug 29 2013 Sam Kottler <shk@redhat.com> 0.0.1-2
- new package built with tito

* Thu Aug 29 2013 Sam Kottler <shk@redhat.com> - 0.0.1-0
- Initial package
