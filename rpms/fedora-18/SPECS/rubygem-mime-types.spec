# Generated from mime-types-1.18.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mime-types
%global rubyabi 1.9.1

Summary: This library allows for the identification of a file's likely MIME content type
Name: rubygem-%{gem_name}
Version: 1.18
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://mime-types.rubyforge.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This library allows for the identification of a file's likely MIME content
type. This is release 1.17.2. The identification of MIME content type is based
on a file's filename extensions.
MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copyright 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.
:include: Licence.rdoc


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





%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/mime-types-1.18/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Licence.rdoc
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/type-lists/application.txt
%doc %{gem_instdir}/type-lists/audio.txt
%doc %{gem_instdir}/type-lists/image.txt
%doc %{gem_instdir}/type-lists/message.txt
%doc %{gem_instdir}/type-lists/model.txt
%doc %{gem_instdir}/type-lists/multipart.txt
%doc %{gem_instdir}/type-lists/text.txt
%doc %{gem_instdir}/type-lists/video.txt

%changelog
* Thu Jun 14 2012 jason - 1.18-1
- Initial package
