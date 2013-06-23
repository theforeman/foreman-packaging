%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name deface

%define rubyabi 1.9.1

Summary: Rails 3 plugin that allows you to customize ERB views in a Rails application without editing the underlying view.
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.2
Release: 3%{?dist}
Group: Development/Libraries
License: MIT
URL: https://github.com/spree/deface
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(nokogiri)
Requires: %{?scl_prefix}rubygem(rails)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Rails 3 plugin that allows you to customize ERB views in a
Rails application without editing the underlying view.

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

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/init.rb
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-3
- new package built with tito

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-2
- rubygem-deface - convert to scl (inecas@redhat.com)

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-1
- new package built with tito


