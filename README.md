# okerr-status

Custom status-page for project (part of [Okerr](https://okerr.com/))

## Install
~~~
apt install libapache2-mod-wsgi-py3
~~~
## Apache config
~~~
<VirtualHost *:443>
    ServerName status.okerr.com

    WSGIDaemonProcess okerr-status user=www-data group=www-data threads=5
    WSGIScriptAlias / /var/www/virtual/status.okerr.com/status.wsgi

    ErrorLog /var/log/apache2/status.okerr.com-err.log

    <Directory /var/www/virtual/status.okerr.com/>
        WSGIProcessGroup okerr-status
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/status.okerr.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/status.okerr.com/privkey.pem
  
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"

</VirtualHost>

<VirtualHost *:80>
    ServerName status.okerr.com
    Alias /.well-known/acme-challenge/ /var/www/_certbot/.well-known/acme-challenge/

    RewriteEngine On
    RewriteCond %{HTTPS} !=on
    RewriteCond %{REQUEST_URI} !^/\.well\-known        
    RewriteRule (.*) https://%{SERVER_NAME}$1 [R=301,L]
</VirtualHost>
~~~

# Other okerr resources
- [Okerr main website](https://okerr.com/)
- [Okerr-server source code repository](gitlab.com/yaroslaff/okerr-dev/) and [okerr server wiki doc](https://gitlab.com/yaroslaff/okerr-dev/wikis/)
- [Okerr client (okerrupdate) repositoty](https://gitlab.com/yaroslaff/okerrupdate) and [okerrupdate wiki doc](https://gitlab.com/yaroslaff/okerrupdate/wikis/)
- [Okerrbench network server benchmark](https://gitlab.com/yaroslaff/okerrbench)
- [Okerr custom status page](https://gitlab.com/yaroslaff/okerr-status)
- [Okerr network sensor](https://gitlab.com/yaroslaff/sensor)
