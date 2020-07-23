# okerr-status

Custom status-page for project (part of [Okerr](https://okerr.com/))

## Install
~~~
apt install libapache2-mod-wsgi-py3
~~~
## Apache config
~~~
<VirtualHost *:80>
    ServerName status.okerr.com

    WSGIDaemonProcess okerr-status user=xenon group=xenon threads=5
    WSGIScriptAlias / /var/www/virtual/status.okerr.com/status.wsgi

    ErrorLog /var/log/apache2/status.okerr.com-err.log

    <Directory /var/www/virtual/status.okerr.com/>
        WSGIProcessGroup okerr-status
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>

</VirtualHost>
~~~

# Other okerr resources
- [Okerr main website](https://okerr.com/)
- [Okerr-server source code repository](gitlab.com/yaroslaff/okerr-dev/) and [okerr server wiki doc](https://gitlab.com/yaroslaff/okerr-dev/wikis/)
- [Okerr client (okerrupdate) repositoty](https://gitlab.com/yaroslaff/okerrupdate) and [okerrupdate wiki doc](https://gitlab.com/yaroslaff/okerrupdate/wikis/)
- [Okerrbench network server benchmark](https://gitlab.com/yaroslaff/okerrbench)
- [Okerr custom status page](https://gitlab.com/yaroslaff/okerr-status)
- [Okerr network sensor](https://gitlab.com/yaroslaff/sensor)