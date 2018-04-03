%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name redhat_access_lib

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.4
Release: 1%{?dist}
Summary: REST client library for accessing Red Hat support
Group: Development/Languages
License: GPLv2+
URL: https://github.com/redhataccess/redhat-support-lib-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem


Requires: %{?scl_prefix_ruby}ruby(rubygems)

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
REST client library for accessing Red Hat support


%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}


%setup -q -D -T -n  %{gem_name}-%{version}


%build
mkdir -p .%{gem_dir}

# Create our gem
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

# install our gem locally, to be moved into buildroot in %%install
%{?scl:scl enable %{scl} "}
gem install --local --no-wrappers --install-dir .%{gem_dir} --force --no-rdoc --no-ri %{gem_name}-%{version}.gem
%{?scl:"}


%install
mkdir -p %{buildroot}%{gem_dir}

cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%defattr(-,root,root,-)
%{gem_dir}


%changelog

* Wed Mar 28 2018 Marek Hulan <mhulan@redhat.com>
- Initial package

