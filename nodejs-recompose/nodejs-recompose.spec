%global npm_name recompose
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.26.0
Release: 1%{?dist}
Summary: A React utility belt for function components and higher-order components
License: MIT
Group: Development/Libraries
URL: https://github.com/acdlite/recompose
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(change-emitter) >= 0.1.2
Requires: npm(change-emitter) < 1.0.0
Requires: npm(fbjs) >= 0.8.1
Requires: npm(fbjs) < 1.0.0
Requires: npm(hoist-non-react-statics) >= 2.3.1
Requires: npm(hoist-non-react-statics) < 3.0.0
Requires: npm(symbol-observable) >= 1.0.4
Requires: npm(symbol-observable) < 2.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr baconObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr branch.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr build %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr componentFromProp.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr componentFromStream.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr compose.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr createEventHandler.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr createSink.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr defaultProps.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr flattenProp.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr flydObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr getContext.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr getDisplayName.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr hoistStatics.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr isClassComponent.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr kefirObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lifecycle.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mapProps.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mapPropsStream.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mostObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr nest.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr onlyUpdateForKeys.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr onlyUpdateForPropTypes.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr pure.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr renameProp.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr renameProps.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr renderComponent.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr renderNothing.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rxjs4ObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rxjsObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr setDisplayName.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr setObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr setPropTypes.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr setStatic.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr shallowEqual.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr shouldUpdate.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr toClass.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr utils %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr withContext.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr withHandlers.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr withProps.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr withPropsOnChange.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr withReducer.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr withState.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr withStateHandlers.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr wrapDisplayName.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr xstreamObservableConfig.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
