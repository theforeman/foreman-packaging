# Generated from rgen-0.8.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rgen

Name: rubygem-%{gem_name}
Version: 0.8.2
Release: 1%{?dist}
Summary: Ruby Modelling and Generator Framework
Group: Development/Languages
License: 
URL: http://ruby-gen.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby 
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: ruby 
BuildRequires: rubygems-devel 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
RGen is a framework for Model Driven Software Development (MDSD) in Ruby. This
means that it helps you build Metamodels, instantiate Models, modify and
transform Models and finally generate arbitrary textual content from it.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
