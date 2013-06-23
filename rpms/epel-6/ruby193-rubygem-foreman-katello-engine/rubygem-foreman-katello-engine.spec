%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman-katello-engine

%define rubyabi 1.9.1
%global foreman_bundlerd_dir /usr/share/foreman/bundler.d

Summary: Katello specific parts of Foreman
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.4
Release: 3%{?dist}
Group: Development/Libraries
License: GPLv2
URL: http://github.com/Katello/foreman-katello-engine
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: foreman
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(katello_api)
Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Katello specific parts of Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/katello.rb
gem 'foreman-katello-engine'
GEMFILE


%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/lib
%{gem_instdir}/config
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/katello.rb
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Apr 08 2013 Ivan Necas <inecas@redhat.com> 0.0.4-3
- fix dependency (inecas@redhat.com)

* Fri Mar 29 2013 Ivan Necas <inecas@redhat.com> 0.0.4-2
- SCL

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.0.4-1
- new package built with tito



