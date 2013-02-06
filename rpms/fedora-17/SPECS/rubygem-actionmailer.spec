# Generated from actionmailer-%{version}.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actionmailer
%global rubyabi 1.9.1

Summary: Email composition, delivery, and receiving framework (part of Rails)
Name: rubygem-%{gem_name}
Epoch: 1
Version: 3.0.20
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.rubyonrails.org
Source0: %{gem_name}-%{version}.gem
Patch0: 0001-rubygem-actionmailer-fix-dep-versions.patch
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby >= 1.8.7

Requires: rubygem(actionpack) = %{version}

Requires: rubygem(mail) => 2.2.19
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: %{name} = %{version}
%description
Email on Rails. Compose, deliver, receive, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.


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

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
cd %{buildroot}%{gem_dir} 
cp %{PATCH0} ./
patch -p0 < ./0001-rubygem-actionmailer-fix-dep-versions.patch
rm ./0001-rubygem-actionmailer-fix-dep-versions.patch

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc /usr/share/gems/gems/actionmailer-%{version}/CHANGELOG
%doc /usr/share/gems/gems/actionmailer-%{version}/MIT-LICENSE
%doc /usr/share/gems/gems/actionmailer-%{version}/README.rdoc

%changelog
* Mon Feb 4 2013 shk@redhat.com - 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com - 3.0.19-1
- Updated to 3.0.19
* Thu Jun 14 2012 jason - 3.0.17-1
- Initial package
