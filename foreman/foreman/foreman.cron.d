SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

RAILS_ENV=production
FOREMAN_HOME=/usr/share/foreman

# Clean up the session entries in the database
15 23 * * *     foreman    /usr/sbin/foreman-rake db:sessions:clear >>/var/log/foreman/cron.log 2>&1

# Send out recurring notifications
0 7 * * *       foreman    /usr/sbin/foreman-rake reports:daily >>/var/log/foreman/cron.log 2>&1
0 5 * * 0       foreman    /usr/sbin/foreman-rake reports:weekly >>/var/log/foreman/cron.log 2>&1
0 3 1 * *       foreman    /usr/sbin/foreman-rake reports:monthly >>/var/log/foreman/cron.log 2>&1

# Expire old reports
30 7 * * *      foreman    /usr/sbin/foreman-rake reports:expire >>/var/log/foreman/cron.log 2>&1

# Collects trends data
*/30 * * * *    foreman    /usr/sbin/foreman-rake trends:counter >>/var/log/foreman/cron.log 2>&1

# Refreshes ldap usergroups. Can be disabled if you're not using LDAP authentication.
*/30 * * * *    foreman    /usr/sbin/foreman-rake ldap:refresh_usergroups >>/var/log/foreman/cron.log 2>&1

# Clean expired notifications
0 6 * * 0       foreman    /usr/sbin/foreman-rake notifications:clean >>/var/log/foreman/cron.log 2>&1

# Only use the following cronjob if you're not using the ENC or ActiveRecord-based storeconfigs
# Get the node.rb / ENC script and store at /etc/puppet/node.rb:
#   https://github.com/theforeman/puppet-foreman/blob/master/templates/external_node.rb.erb
# Send facts to Foreman, using the ENC script in a fact pushing only mode
#*/2 * * * *     puppet    /usr/bin/tfm-ruby /etc/puppet/node.rb --push-facts >>/var/log/foreman/cron.log 2>&1

# Warning: ActiveRecord-based storeconfigs is deprecated from Foreman 1.1 and Puppet 3.0
#   see http://projects.theforeman.org/wiki/foreman/ReleaseNotes#11-stable
# Only use the following cronjob if you're using ActiveRecord storeconfigs!
#*/30 * * * *    foreman    /usr/sbin/foreman-rake puppet:migrate:populate_hosts >>/var/log/foreman/cron.log 2>&1

