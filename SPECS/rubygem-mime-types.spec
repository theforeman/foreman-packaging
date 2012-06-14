%define rbname mime-types
%define version 1.18
%define release 1

Summary: This library allows for the identification of a file's likely MIME content type
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://mime-types.rubyforge.org/
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(mime-types) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This library allows for the identification of a file's likely MIME content
type. This is release 1.17.2. The identification of MIME content type is based
on a file's filename extensions.
MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copyright 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.
:include: Licence.rdoc


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/mime-types-1.18/.gitignore
%{gemdir}/gems/mime-types-1.18/.hoerc
%doc %{gemdir}/gems/mime-types-1.18/History.rdoc
%doc %{gemdir}/gems/mime-types-1.18/Licence.rdoc
%doc %{gemdir}/gems/mime-types-1.18/Manifest.txt
%doc %{gemdir}/gems/mime-types-1.18/README.rdoc
%{gemdir}/gems/mime-types-1.18/Rakefile
%{gemdir}/gems/mime-types-1.18/lib/mime/types.rb
%{gemdir}/gems/mime-types-1.18/lib/mime/types/application
%{gemdir}/gems/mime-types-1.18/lib/mime/types/application.mac
%{gemdir}/gems/mime-types-1.18/lib/mime/types/application.nonstandard
%{gemdir}/gems/mime-types-1.18/lib/mime/types/application.obsolete
%{gemdir}/gems/mime-types-1.18/lib/mime/types/audio
%{gemdir}/gems/mime-types-1.18/lib/mime/types/audio.nonstandard
%{gemdir}/gems/mime-types-1.18/lib/mime/types/audio.obsolete
%{gemdir}/gems/mime-types-1.18/lib/mime/types/image
%{gemdir}/gems/mime-types-1.18/lib/mime/types/image.nonstandard
%{gemdir}/gems/mime-types-1.18/lib/mime/types/image.obsolete
%{gemdir}/gems/mime-types-1.18/lib/mime/types/message
%{gemdir}/gems/mime-types-1.18/lib/mime/types/message.obsolete
%{gemdir}/gems/mime-types-1.18/lib/mime/types/model
%{gemdir}/gems/mime-types-1.18/lib/mime/types/multipart
%{gemdir}/gems/mime-types-1.18/lib/mime/types/multipart.nonstandard
%{gemdir}/gems/mime-types-1.18/lib/mime/types/multipart.obsolete
%{gemdir}/gems/mime-types-1.18/lib/mime/types/other.nonstandard
%{gemdir}/gems/mime-types-1.18/lib/mime/types/text
%{gemdir}/gems/mime-types-1.18/lib/mime/types/text.nonstandard
%{gemdir}/gems/mime-types-1.18/lib/mime/types/text.obsolete
%{gemdir}/gems/mime-types-1.18/lib/mime/types/text.vms
%{gemdir}/gems/mime-types-1.18/lib/mime/types/video
%{gemdir}/gems/mime-types-1.18/lib/mime/types/video.nonstandard
%{gemdir}/gems/mime-types-1.18/lib/mime/types/video.obsolete
%{gemdir}/gems/mime-types-1.18/mime-types.gemspec
%{gemdir}/gems/mime-types-1.18/test/test_mime_type.rb
%{gemdir}/gems/mime-types-1.18/test/test_mime_types.rb
%doc %{gemdir}/gems/mime-types-1.18/type-lists/application.txt
%doc %{gemdir}/gems/mime-types-1.18/type-lists/audio.txt
%doc %{gemdir}/gems/mime-types-1.18/type-lists/image.txt
%doc %{gemdir}/gems/mime-types-1.18/type-lists/message.txt
%doc %{gemdir}/gems/mime-types-1.18/type-lists/model.txt
%doc %{gemdir}/gems/mime-types-1.18/type-lists/multipart.txt
%doc %{gemdir}/gems/mime-types-1.18/type-lists/text.txt
%doc %{gemdir}/gems/mime-types-1.18/type-lists/video.txt
%{gemdir}/gems/mime-types-1.18/.gemtest


%doc %{gemdir}/doc/mime-types-1.18
%{gemdir}/cache/mime-types-1.18.gem
%{gemdir}/specifications/mime-types-1.18.gemspec

%changelog
