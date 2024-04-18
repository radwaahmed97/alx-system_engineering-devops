# Puppet script tests how well our web server setup featuring Nginx is doing under pressure
exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
