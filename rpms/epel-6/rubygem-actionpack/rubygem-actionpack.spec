%define rbname actionpack
%define version 3.2.13
%define release 1

Summary: Web-flow and rendering framework putting the VC in MVC (part of Rails).
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
Requires: rubygem-activesupport = %{version}
Requires: rubygem-activemodel = %{version}
Requires: rubygem-rack-cache => 1.2
Requires: rubygem-rack-cache < 2
Requires: rubygem-builder => 3.0.0
Requires: rubygem-builder < 3.1
Requires: rubygem-rack => 1.4.5
Requires: rubygem-rack < 1.5
Requires: rubygem-rack-test => 0.6.1
Requires: rubygem-rack-test < 0.7
Requires: rubygem-journey => 1.0.4
Requires: rubygem-journey < 1.1
Requires: rubygem-sprockets => 2.2.1
Requires: rubygem-sprockets < 2.3
Requires: rubygem-erubis => 2.7.0
Requires: rubygem-erubis < 2.8

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10

BuildArch: noarch

Provides: rubygem(actionpack) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.


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
%{gemdir}/gems/actionpack-%{version}/CHANGELOG.md
%{gemdir}/gems/actionpack-%{version}/README.rdoc
%{gemdir}/gems/actionpack-%{version}/MIT-LICENSE
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/asset_paths.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/base.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/callbacks.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/collector.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/helpers.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/layouts.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/logger.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/railties/routes_helpers.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/rendering.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/translation.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/url_for.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller/view_paths.rb
%{gemdir}/gems/actionpack-%{version}/lib/abstract_controller.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/base.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/caching/actions.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/caching/fragments.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/caching/pages.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/caching/sweeping.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/caching.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/deprecated/integration_test.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/deprecated/performance_test.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/deprecated.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/log_subscriber.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/compatibility.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/conditional_get.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/cookies.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/data_streaming.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/exceptions.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/flash.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/force_ssl.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/head.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/helpers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/hide_actions.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/http_authentication.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/implicit_render.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/instrumentation.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/mime_responds.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/params_wrapper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/rack_delegation.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/redirecting.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/renderers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/rendering.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/request_forgery_protection.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/rescue.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/responder.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/session_management.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/streaming.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/testing.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal/url_for.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/metal.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/middleware.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/railtie.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/railties/paths.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/record_identifier.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/test_case.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/vendor/html-scanner/html/document.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/vendor/html-scanner/html/node.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/vendor/html-scanner/html/sanitizer.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/vendor/html-scanner/html/selector.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/vendor/html-scanner/html/tokenizer.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/vendor/html-scanner/html/version.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller/vendor/html-scanner.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_controller.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/cache.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/filter_parameters.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/headers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/mime_negotiation.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/mime_type.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/mime_types.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/parameter_filter.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/parameters.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/rack_cache.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/request.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/response.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/upload.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/http/url.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/best_standards_support.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/body_proxy.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/callbacks.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/cookies.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/debug_exceptions.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/exception_wrapper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/flash.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/head.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/params_parser.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/public_exceptions.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/reloader.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/remote_ip.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/request_id.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/rescue.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/session/abstract_store.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/session/cache_store.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/session/cookie_store.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/session/mem_cache_store.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/show_exceptions.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/stack.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/static.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/_request_and_response.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/_trace.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/diagnostics.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/layout.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/missing_template.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/routing_error.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/template_error.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/middleware/templates/rescues/unknown_action.erb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/railtie.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/routing/mapper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/routing/polymorphic_routes.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/routing/redirection.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/routing/route_set.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/routing/routes_proxy.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/routing/url_for.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/routing.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/assertions/dom.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/assertions/response.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/assertions/routing.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/assertions/selector.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/assertions/tag.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/assertions.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/integration.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/performance_test.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/test_process.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/test_request.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch/testing/test_response.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_dispatch.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_pack/version.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_pack.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/asset_paths.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/base.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/buffers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/context.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/flows.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/active_model_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/asset_paths.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/asset_tag_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/asset_tag_helpers/asset_include_tag.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/asset_tag_helpers/asset_paths.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/asset_tag_helpers/javascript_tag_helpers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/asset_tag_helpers/stylesheet_tag_helpers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/atom_feed_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/cache_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/capture_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/controller_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/csrf_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/date_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/debug_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/form_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/form_options_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/form_tag_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/javascript_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/number_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/output_safety_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/record_tag_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/rendering_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/sanitize_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/tag_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/text_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/translation_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers/url_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/helpers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/locale/en.yml
%{gemdir}/gems/actionpack-%{version}/lib/action_view/log_subscriber.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/lookup_context.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/path_set.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/railtie.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/renderer/abstract_renderer.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/renderer/partial_renderer.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/renderer/renderer.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/renderer/streaming_template_renderer.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/renderer/template_renderer.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/template/error.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/template/handlers/builder.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/template/handlers/erb.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/template/handlers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/template/resolver.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/template/text.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/template.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/test_case.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view/testing/resolvers.rb
%{gemdir}/gems/actionpack-%{version}/lib/action_view.rb
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/assets.rake
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/bootstrap.rb
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/compressors.rb
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/helpers/isolated_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/helpers/rails_helper.rb
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/helpers.rb
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/railtie.rb
%{gemdir}/gems/actionpack-%{version}/lib/sprockets/static_compiler.rb


%doc %{gemdir}/doc/actionpack-%{version}
%{gemdir}/cache/actionpack-%{version}.gem
%{gemdir}/specifications/actionpack-%{version}.gemspec

%changelog
* Fri Apr 12 2013 shk@rdhat.com 3.2.13-1
- Updated to 3.2.13
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updates to 3.0.19
