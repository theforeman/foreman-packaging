%global gem_name foreman_admin

Name:           rubygem-%{gem_name}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Foreman administrative actions

Group:          Development/Languages
License:        GPLv3
URL:            http://github.com/komidore64/foreman-admin
Source0:        %{gem_name}-%{version}.gem

Requires:       foreman >= 1.8
Requires:       katello >= 2.0
BuildRequires:  ruby
BuildRequires:  ruby(rubygems)
BuildRequires:  rubygems-devel
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
Foreman-admin is a command line tool for carrying out a few administrative actions on a Foreman server.

%prep
%setup -q -c -T
%{__install} --directory .%{gem_dir}
gem install --local --install-dir .%{gem_dir} --force %{SOURCE0} --no-rdoc --no-ri

%build

%install
# pre-install buildroot scrub
%{__rm} --recursive --force %{buildroot}

# throw down the gem
%{__install} --directory %{buildroot}%{gem_dir}
%{__cp} --archive .%{gem_dir}/cache %{buildroot}%{gem_dir}/
%{__cp} --archive .%{gem_dir}/doc %{buildroot}%{gem_dir}/
%{__cp} --archive .%{gem_dir}/gems %{buildroot}%{gem_dir}/
%{__cp} --archive .%{gem_dir}/specifications %{buildroot}%{gem_dir}/

# take care of the executable
%{__install} --directory %{buildroot}/usr/sbin
%{__cp} --archive %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/bin/foreman-admin %{buildroot}/usr/sbin/foreman-admin
%{__rm} --recursive --force %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/bin

%clean
%{__rm} --recursive --force %{buildroot} .%{gem_dir}

%files
%defattr(644, root, foreman, -)
%dir %{gem_instdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/LICENSE
%{gem_instdir}/README.md
%{gem_instdir}/lib/
%{gem_instdir}/test/
%{gem_spec}
%{gem_cache}
%attr(744, root, foreman) /usr/sbin/foreman-admin

%changelog
