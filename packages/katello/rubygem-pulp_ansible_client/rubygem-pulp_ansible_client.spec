# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name pulp_ansible_client

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.0
Release: 2%{?dist}
Summary: Pulp 3 Ansible API Ruby Gem
Group: Development/Languages
License: GPL-2.0+
URL: https://github.com/pulp/pulp_ansible/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(faraday) >= 0.14.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1
Requires: %{?scl_prefix_ruby}rubygem(json) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
pulp3 ansible client bindings

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/git_push.sh
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/pulp_ansible_client.gemspec
%{gem_instdir}/spec

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.6.0-2
- Rebuild for Ruby 2.7

* Mon Jan 11 2021 ianballou <ianballou67@gmail.com> 0.6.0-1
- Update to 0.6.0

* Thu Oct 15 2020 ianballou <ianballou67@gmail.com> 0.4.2-1
- Update to 0.4.2

* Fri Sep 11 2020 Justin Sherrill <jsherril@redhat.com> 0.3.0-1
- Update to 0.3.0

* Thu Aug 20 2020 Justin Sherrill <jsherril@redhat.com> 0.2.0-1
- Update to 0.2.0

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 0.2.0b13.dev01588546902-1
- Update to 0.2.0b13.dev01588546902

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 0.2.0b11-1
- Update rubygem-pulp_ansible_client to 0.2.0.b11

* Tue Jun 25 2019 Justin Sherrill <jlsherrill@gmail.com> - 0.2.0b1.dev0.1560866833-1
- initial build
