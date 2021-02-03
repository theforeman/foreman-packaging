build:
	cp cache/* /usr/share/foreman/vendor/cache/
	cp $(PLUGIN).rb /usr/share/foreman/bundler.d/
	cd /usr/share/foreman && ( \
		/usr/bin/foreman-ruby /usr/bin/bundle install --local && \
		if [ "$(PLUGIN_HAS_PACKAGE_JSON)" = "true" ]; then /usr/bin/npm install --no-audit --no-optional --unsafe-perm; fi && \
		if [ "$(PLUGIN_HAS_ASSETS)" = "true" ] || [ "$(PLUGIN_HAS_WEBPACK)" = "true" ]; then /usr/bin/foreman-ruby /usr/bin/bundle exec rake plugin:assets:precompile[$(PLUGIN)] RAILS_ENV=production DATABASE_URL=nulldb://nohost; fi && \
		if [ "$(PLUGIN_HAS_API)" = "true" ]; then \
			/usr/bin/foreman-ruby /usr/bin/bundle exec rake plugin:apipie:cache[$(PLUGIN)] cache_part=resources \
				OUT=/var/lib/foreman/public/apipie-cache/plugin/$(PLUGIN) RAILS_ENV=development \
				DATABASE_URL=nulldb://nohost FOREMAN_APIPIE_LANGS=en_US; \
		fi \
	)
	GEM_PATH=$$(cd /usr/share/foreman && /usr/bin/foreman-ruby /usr/bin/bundle show $(PLUGIN)) && \
	if [ "$(PLUGIN_HAS_ASSETS)" = "true" ]; then cp -rp $${GEM_PATH}/public/assets ./; fi && \
	if [ "$(PLUGIN_HAS_WEBPACK)" = "true" ]; then cp -rp $${GEM_PATH}/public/webpack ./; fi
	[ -e apipie-cache ] || mkdir apipie-cache/
	if [ "$(PLUGIN_HAS_API)" = "true" ]; then cp -rp /var/lib/foreman/public/apipie-cache/plugin/$(PLUGIN) ./apipie-cache/; fi

%:
	dh $@
