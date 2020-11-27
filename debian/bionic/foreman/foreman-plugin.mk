build:
	cp cache/* /usr/share/foreman/vendor/cache/
	cp $(PLUGIN).rb /usr/share/foreman/bundler.d/
	cd /usr/share/foreman && ( \
		/usr/bin/foreman-ruby /usr/bin/bundle install --local && \
		/usr/bin/npm install --no-audit --no-optional --unsafe-perm && \
		/usr/bin/foreman-ruby /usr/bin/bundle exec rake plugin:assets:precompile[$(PLUGIN)] RAILS_ENV=production DATABASE_URL=nulldb://nohost && \
		/usr/bin/foreman-ruby /usr/bin/bundle exec rake plugin:apipie:cache[$(PLUGIN)] cache_part=resources \
			OUT=/var/lib/foreman/public/apipie-cache/plugin/$(PLUGIN) RAILS_ENV=development \
			DATABASE_URL=nulldb://nohost FOREMAN_APIPIE_LANGS=en_US \
	)
	GEM_PATH=$$(cd /usr/share/foreman && /usr/bin/foreman-ruby /usr/bin/bundle show $(PLUGIN)) && \
	cp -rp $${GEM_PATH}/public/assets ./ && \
	cp -rp $${GEM_PATH}/public/webpack ./
	[ -e apipie-cache ] || mkdir apipie-cache/
	cp -rp /var/lib/foreman/public/apipie-cache/plugin/$(PLUGIN) ./apipie-cache/

%:
	dh $@
