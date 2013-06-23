%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from delayed_job_active_record-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name delayed_job_active_record
%global rubyabi 1.9.1

Summary: ActiveRecord back-end for DelayedJob
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.3
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/collectiveidea/delayed_job_active_record
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activerecord) > 2.1.0
Requires: %{?scl_prefix}rubygem(delayed_job) => 3.0.0
Requires: %{?scl_prefix}rubygem(delayed_job) < 3.1
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(activerecord) > 2.1.0
# The test suite needs sample_jobs from delayed_job
# https://github.com/collectiveidea/delayed_job_active_record/issues/18
BuildRequires: %{?scl_prefix}rubygem-delayed_job-doc => 3.0.0
BuildRequires: %{?scl_prefix}rubygem-delayed_job-doc < 3.1
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
ActiveRecord back-end for DelayedJob, originally authored by Tobias Luetke


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

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

%check
pushd .%{gem_instdir}
# Bundler just complicates everything in our case, remove it.
sed -i -e "s|require 'bundler/setup'||" spec/spec_helper.rb

# https://github.com/collectiveidea/delayed_job_active_record/issues/24
%{?scl:scl enable %{scl} '}
rspec spec | grep "79 examples, 1 failure"
%{?scl:'}
popd



%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec/

%changelog
* Tue Apr 09 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.3-2
- new package built with tito

* Mon Apr 08 2013 Eric D Helms <ehelms@redhat.com>
- adding spec for ruby193 rubygem-delayed_job_active_record (ehelms@redhat.com)

* Wed Oct 17 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.3-1
- Update to delayed_job_active_record 0.3.3.

* Thu May 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.2-1
- Initial package
