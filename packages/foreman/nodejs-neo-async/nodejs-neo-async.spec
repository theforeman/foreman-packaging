%global npm_name neo-async

Name: nodejs-neo-async
Version: 2.6.2
Release: 2%{?dist}
Summary: Neo-Async is a drop-in replacement for Async, it almost fully covers its functionality and runs faster
License: MIT
URL: https://github.com/suguru03/neo-async
Source0: https://registry.npmjs.org/neo-async/-/neo-async-%{version}.tgz
BuildRequires: nodejs-packaging
%if 0%{?rhel} == 10
# https://issues.redhat.com/browse/RHEL-137712
BuildRequires: /usr/bin/node
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr all.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr allLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr allSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr angelFall.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr any.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr anyLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr anySeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr apply.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr applyEach.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr applyEachSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr async.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr async.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr asyncify.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr auto.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr autoInject.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr cargo.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr compose.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr concat.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr concatLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr concatSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr constant.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr createLogger.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr detect.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr detectLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr detectSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dir.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr doDuring.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr doUntil.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr doWhilst.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr during.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr each.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr eachLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr eachOf.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr eachOfLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr eachOfSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr eachSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr ensureAsync.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr every.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr everyLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr everySeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr fast.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr filter.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr filterLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr filterSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr find.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr findLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr findSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr foldl.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr foldr.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr forEach.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr forEachLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr forEachOf.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr forEachOfLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr forEachOfSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr forEachSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr forever.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr groupBy.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr groupByLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr groupBySeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr inject.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr iterator.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr log.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr map.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mapLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mapSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mapValues.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mapValuesLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mapValuesSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr memoize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr nextTick.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr omit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr omitLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr omitSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr parallel.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr parallelLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr pick.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr pickLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr pickSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr priorityQueue.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr queue.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr race.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr reduce.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr reduceRight.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr reflect.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr reflectAll.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr reject.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rejectLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rejectSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr retry.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr retryable.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr safe.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr select.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr selectLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr selectSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr seq.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr series.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr setImmediate.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr some.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr someLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr someSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr sortBy.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr sortByLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr sortBySeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr timeout.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr times.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr timesLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr timesSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr transform.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr transformLimit.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr transformSeries.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr tryEach.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr unmemoize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr until.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr waterfall.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr whilst.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr wrapSync.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Sat Jun 06 2026 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.6.2-2
- Regenerate spec file

* Tue Dec 23 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.6.2-1
- Add nodejs-neo-async generated by npm2rpm using the single strategy

