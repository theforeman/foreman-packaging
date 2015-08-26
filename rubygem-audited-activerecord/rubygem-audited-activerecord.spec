%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from audited-activerecord-3.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name audited-activerecord
%global rubyabi 1.9.1

Summary: Log all changes to your ActiveRecord models
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.0
Release: 4%{?dist}
Group: Development/Languages
# The license information is missing in the .gem file ATM.
# https://github.com/collectiveidea/audited/pull/127
License: MIT
URL: https://github.com/collectiveidea/audited
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Hopefully the tests will be included in the gem in the future.
# https://github.com/collectiveidea/audited/pull/125
#
# git clone https://github.com/collectiveidea/audited.git && cd audited && git checkout 224786f
# tar czvf audited-activerecord-3.0.0-tests.tgz spec/audited/adapters/active_record \
#   spec/rails_app spec/support/active_record spec/*.rb test
Source1: %{gem_name}-%{version}-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(audited) = 3.0.0
Requires: %{?scl_prefix_ruby}rubygem(activerecord) => 3.0
Requires: %{?scl_prefix_ruby}rubygem(activerecord) < 4
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(audited) = 3.0.0
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ruby}rubygem(rails) => 3.0
BuildRequires: %{?scl_prefix_ruby}rubygem(rails) < 4
BuildRequires: %{?scl_prefix}rubygem(rspec-rails)
BuildRequires: %{?scl_prefix_ruby}rubygem(sqlite3)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Log all changes to your ActiveRecord models


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
tar xzvf %{SOURCE1} -C .%{gem_instdir}
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
# This is ugly. It should be probably reported to upstream ;)
%{?scl:scl enable %{scl} - << \EOF}
RUBYOPT='-Ilib -rrails/all -raudited-activerecord' testrb test/*_test.rb
%{?scl:EOF}
popd



%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.0-2
- new package built with tito

* Wed Nov 28 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.0-1
- Initial package
