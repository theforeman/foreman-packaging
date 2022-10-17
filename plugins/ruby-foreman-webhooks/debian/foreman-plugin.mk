BUNDLE = /usr/bin/bundle2.7

build:
	# prepare a local foreman installation based on packages
	mkdir -p ./usr/share
	cp -r /usr/share/foreman ./usr/share || true

	# clean up possibly existing state we copied
	mkdir -p ./var/lib/foreman
	cp -r /var/lib/foreman/db ./var/lib/foreman || true
	unlink ./usr/share/foreman/db
	mkdir ./usr/share/foreman/db
	cp -rf /usr/share/foreman/db/* ./usr/share/foreman/db/
	unlink ./usr/share/foreman/tmp
	mkdir ./usr/share/foreman/tmp
	rm ./usr/share/foreman/config/initializers/encryption_key.rb
	rm ./usr/share/foreman/config/database.yml

	# add plugin code to the local foreman installation
	cp cache/* ./usr/share/foreman/vendor/cache/
	cp $(PLUGIN).rb ./usr/share/foreman/bundler.d/

	# perform the actual build of the plugin
	cd ./usr/share/foreman && ( \
		/usr/bin/foreman-ruby $(BUNDLE) install --local && \
		if [ "$(PLUGIN_HAS_PACKAGE_JSON)" = "true" ]; then /usr/bin/npm install --no-audit --no-optional --unsafe-perm; fi && \
		/usr/bin/foreman-ruby $(BUNDLE) exec rake security:generate_encryption_key && \
		if [ "$(PLUGIN_HAS_ASSETS)" = "true" ] || [ "$(PLUGIN_HAS_WEBPACK)" = "true" ]; then /usr/bin/foreman-ruby $(BUNDLE) exec rake plugin:assets:precompile[$(PLUGIN)] RAILS_ENV=production DATABASE_URL=nulldb://nohost; fi \
	)

	# copy back generated data so it can be packaged more easily
	GEM_PATH=$$(cd ./usr/share/foreman && /usr/bin/foreman-ruby $(BUNDLE) show $(PLUGIN)) && \
	if [ "$(PLUGIN_HAS_ASSETS)" = "true" ]; then cp -rp $${GEM_PATH}/public/assets ./; fi && \
	if [ "$(PLUGIN_HAS_WEBPACK)" = "true" ]; then cp -rp $${GEM_PATH}/public/webpack ./; fi

	# mark the build step as complete
	touch $@

%:
	dh $@
