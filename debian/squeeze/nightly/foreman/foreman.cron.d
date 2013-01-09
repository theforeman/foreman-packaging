SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

RAILS_ENV=production
FOREMAN_HOME=/usr/share/foreman

# Clean up the session entries in the database
15 23 * * *     foreman    cd ${FOREMAN_HOME} && /usr/bin/rake db:sessions:clear >/var/log/foreman/cron.log 2>&1

# Send out daily summary
0 7 * * *       foreman    cd ${FOREMAN_HOME} && /usr/bin/rake reports:summarize >/var/log/foreman/cron.log 2>&1

# Expire old reports
30 7 * * *      foreman    cd ${FOREMAN_HOME} && /usr/bin/rake reports:expire >/var/log/foreman/cron.log 2>&1

# Collects trends data
*/30 * * * *    foreman    cd ${FOREMAN_HOME} && /usr/bin/rake trends:counter >/var/log/foreman/cron.log 2>&1


# Only use the following cronjob if you're using stored configs!
# Populate hosts
*/30 * * * *    foreman    cd ${FOREMAN_HOME} && /usr/bin/rake puppet:migrate:populate_hosts >/var/log/foreman/cron.log 2>&1


# Only uncomment the following cronjob if you're not using stored configs!
# Send facts to Foreman.
#*/2 * * * *    puppet     ${FOREMAN_HOME}/extras/puppet/foreman/files/push_facts.rb >/var/log/foreman/cron.log 2>&1

