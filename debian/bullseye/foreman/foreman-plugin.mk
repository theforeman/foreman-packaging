build:
	cp cache/* /usr/share/foreman/vendor/cache/
	cp $(PLUGIN).rb /usr/share/foreman/bundler.d/
	cd /usr/share/foreman && ( \
		/usr/bin/foreman-ruby /usr/bin/bundle install --local && \
		if [ "$(PLUGIN_HAS_PACKAGE_JSON)" = "true" ]; then /usr/bin/npm install --no-audit --no-optional --unsafe-perm; fi && \
		if [ "$(PLUGIN_HAS_ASSETS)" = "true" ] || [ "$(PLUGIN_HAS_WEBPACK)" = "true" ]; then /usr/bin/foreman-ruby /usr/bin/bundle exec rake plugin:assets:precompile[$(PLUGIN)] RAILS_ENV=production DATABASE_URL=nulldb://nohost; fi \
	)
	GEM_PATH=$$(cd /usr/share/foreman && /usr/bin/foreman-ruby /usr/bin/bundle show $(PLUGIN)) && \
	if [ "$(PLUGIN_HAS_ASSETS)" = "true" ]; then cp -rp $${GEM_PATH}/public/assets ./; fi && \
	if [ "$(PLUGIN_HAS_WEBPACK)" = "true" ]; then cp -rp $${GEM_PATH}/public/webpack ./; fi

%:
	dh $@
