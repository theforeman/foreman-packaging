%define rbname mail
%define version 2.3.3
%define release 2

Summary: Mail provides a nice Ruby DSL for making, sending and reading emails.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/mikel/mail
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-mime-types => 1.16
Requires: rubygem-mime-types < 2

Requires: rubygem-treetop => 1.4.8
Requires: rubygem-treetop < 1.5

Requires: rubygem-i18n >= 0.4.0
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(mail) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A really Ruby Mail handler.


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
%doc %{gemdir}/gems/mail-2.3.3/README.rdoc
%doc %{gemdir}/gems/mail-2.3.3/CHANGELOG.rdoc
%{gemdir}/gems/mail-2.3.3/Dependencies.txt
%{gemdir}/gems/mail-2.3.3/Gemfile
%{gemdir}/gems/mail-2.3.3/Rakefile
%doc %{gemdir}/gems/mail-2.3.3/TODO.rdoc
%{gemdir}/gems/mail-2.3.3/lib/mail/attachments_list.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/body.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/configuration.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/core_extensions/nil.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/core_extensions/object.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/core_extensions/shell_escape.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/core_extensions/smtp.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/core_extensions/string/access.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/core_extensions/string/multibyte.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/core_extensions/string.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/address.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/address_list.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/content_disposition_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/content_location_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/content_transfer_encoding_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/content_type_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/date_time_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/envelope_from_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/message_ids_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/mime_version_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/phrase_list.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements/received_element.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/elements.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/encodings/7bit.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/encodings/8bit.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/encodings/base64.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/encodings/binary.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/encodings/quoted_printable.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/encodings/transfer_encoding.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/encodings.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/envelope.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/field_list.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/bcc_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/cc_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/comments_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/common/address_container.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/common/common_address.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/common/common_date.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/common/common_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/common/common_message_id.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/common/parameter_hash.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/content_description_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/content_disposition_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/content_id_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/content_location_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/content_transfer_encoding_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/content_type_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/date_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/from_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/in_reply_to_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/keywords_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/message_id_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/mime_version_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/optional_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/received_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/references_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/reply_to_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/resent_bcc_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/resent_cc_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/resent_date_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/resent_from_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/resent_message_id_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/resent_sender_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/resent_to_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/return_path_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/sender_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/structured_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/subject_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/to_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields/unstructured_field.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/fields.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/header.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/indifferent_hash.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/mail.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/message.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/multibyte/chars.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/multibyte/exceptions.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/multibyte/unicode.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/multibyte/utils.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/multibyte.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/delivery_methods/exim.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/delivery_methods/file_delivery.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/delivery_methods/sendmail.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/delivery_methods/smtp.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/delivery_methods/smtp_connection.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/delivery_methods/test_mailer.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/retriever_methods/base.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/retriever_methods/imap.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/retriever_methods/pop3.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network/retriever_methods/test_retriever.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/network.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/address_lists.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/address_lists.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_disposition.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_disposition.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_location.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_location.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_transfer_encoding.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_transfer_encoding.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_type.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/content_type.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/date_time.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/date_time.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/envelope_from.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/envelope_from.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/message_ids.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/message_ids.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/mime_version.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/mime_version.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/phrase_lists.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/phrase_lists.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/received.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/received.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/rfc2045.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/rfc2045.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/rfc2822.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/rfc2822.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/rfc2822_obsolete.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parsers/rfc2822_obsolete.treetop
%{gemdir}/gems/mail-2.3.3/lib/mail/part.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/parts_list.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/patterns.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/utilities.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/version.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/version_specific/ruby_1_8.rb
%{gemdir}/gems/mail-2.3.3/lib/mail/version_specific/ruby_1_9.rb
%{gemdir}/gems/mail-2.3.3/lib/mail.rb
%{gemdir}/gems/mail-2.3.3/lib/tasks/corpus.rake
%{gemdir}/gems/mail-2.3.3/lib/tasks/treetop.rake
%{gemdir}/gems/mail-2.3.3/lib/VERSION


%doc %{gemdir}/doc/mail-2.3.3
%{gemdir}/cache/mail-2.3.3.gem
%{gemdir}/specifications/mail-2.3.3.gemspec
%changelog
* Tue May 08 2012 jmontleo@redhat.com - 2.3.3-2
- Cleaned up spec file
