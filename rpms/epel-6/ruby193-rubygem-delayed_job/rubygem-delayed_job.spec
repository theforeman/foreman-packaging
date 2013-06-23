%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from delayed_job-2.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name delayed_job

%global rubyabi 1.9.1

Summary: Database-backed asynchronous priority queue system
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.2
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/collectiveidea/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(activesupport) => 3.0
Requires: %{?scl_prefix}rubygem(activesupport) < 4
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(bundler) => 1.0.0
BuildRequires: %{?scl_prefix}rubygem(rspec-core)
BuildRequires: %{?scl_prefix}rubygem(actionmailer) => 3.0.0
BuildRequires: %{?scl_prefix}rubygem(activerecord) => 3.0.0
BuildRequires: %{?scl_prefix}rubygem(sqlite3) => 1.3.0
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Delayed_job (or DJ) encapsulates the common pattern of asynchronously
executing longer tasks in the background. It is a direct extraction from
Shopify where the job table is responsible for a multitude of core tasks.
This gem is collectiveidea's fork
(http://github.com/collectiveidea/delayed_job).


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# https://github.com/collectiveidea/delayed_job/issues/390
sed -i '32,36 s|^|#|' spec/yaml_ext_spec.rb
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_instdir}/contrib
%{gem_instdir}/recipes
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.textile
%{gem_instdir}/spec

%changelog
* Tue Apr 09 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.2-3
- new package built with tito

* Mon Apr 08 2013 Eric D Helms <ehelms@redhat.com> 3.0.2-2
- tune up spec for ruby193 SC (ehelms@redhat.com)
- import rubygem-delayed_job 3.0.2 (ehelms@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)
- Automatic commit of package [ruby193-rubygem-delayed_job] minor release
  [2.1.4-3]. (msuchy@redhat.com)
- tune up spec for ruby193 SC (msuchy@redhat.com)
- tune up spec for ruby193 SC (msuchy@redhat.com)
- cp -a rubygem-delayed_job ruby193-rubygem-delayed_job (msuchy@redhat.com)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.2-1
- Update to delayed_job 3.0.2.

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.4-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.4-1
- Update to the delayed_job 2.1.4.

* Thu Feb 10 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.3-1
- Initial package
