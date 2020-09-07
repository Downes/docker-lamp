downes/lamp
==========

This is a fork of furia/lamp (full Readme below). It adds Perl to the set of supported environments, and sets up a cgi-bin directory at /var/www/html/cgi-bin

Docker image is here: https://hub.docker.com/r/downes/docker-lamp

To run:
```
docker pull downes/docker-lamp

docker run --publish 80:80 --detach --name bb3 downeslamp
```


Setup from repo as follows:

Process:

```
git clone  https://github.com/Downes/docker-lamp
```
        (or git pull origin master if reloading the changed repo)


```
cd docker-lamp

docker build --tag downeslamp .

docker run --publish 80:80 --detach --name bb3 downeslamp
```

Testing the server

http://localhost  (should show Apache index page)

http://localhost/index.php  (should show PHP index page)

http://localhost/cgi-bin/server_test.cgi  (should show Perl test page)     

 

If Perl CGI isn't running properly, try:
```
docker exec -it bb3 /etc/init.d/apache2 reload
```

   (you can't docker exec -it bb3 apache2ctl restart because it crashes the entire container - see https://stackoverflow.com/questions/37523338/how-to-restart-apache2-without-terminating-docker-container )

   ( if you crash it, docker start bb3 )

Open a shell inside
```
docker exec -i -t bb3 bash
```

What I've changed from furia/lamp
=================================

Dockerfile:

Inserted the following lines (this is just a starter, I'll be adding more later):

```
RUN apt-get install -y \

      libcgi-session-perl \
      
      libwww-perl \
      
      libmime-types-perl

RUN a2enmod cgid 

RUN rm -f /etc/apache2/conf-available/serve-cgi-bin.conf 

COPY cgi-enabled.conf /etc/apache2/conf-available/

RUN mkdir /var/www/html/cgi-bin

RUN a2enconf cgi-enabled 


COPY index.php /var/www/html/

COPY server_test.cgi /var/www/html/cgi-bin

RUN chmod 705 /var/www/html/cgi-bin/server_test.cgi

COPY run-lamp.sh /usr/sbin/
```
Also:

- remove existing serve-cgi-bin.conf because it redirects cgi-bin to /usr/lib/cgi-bin

- Created cgi-enabled.conf to set up cgi-bin configuration 

- Created server_test.cgi which tests Perl modules 



fauria/lamp
==========

![docker_logo](https://raw.githubusercontent.com/fauria/docker-lamp/master/docker_139x115.png)![docker_fauria_logo](https://raw.githubusercontent.com/fauria/docker-lamp/master/docker_fauria_161x115.png)

[![Docker Pulls](https://img.shields.io/docker/pulls/fauria/lamp.svg?style=plastic)](https://hub.docker.com/r/fauria/lamp/)
[![Docker Build Status](https://img.shields.io/docker/build/fauria/lamp.svg?style=plastic)](https://hub.docker.com/r/fauria/lamp/builds/)
[![](https://images.microbadger.com/badges/image/fauria/lamp.svg)](https://microbadger.com/images/fauria/lamp "fauria/lamp")

This Docker container implements a last generation LAMP stack with a set of popular PHP modules. Includes support for [Composer](https://getcomposer.org/), [Bower](http://bower.io/) and [npm](https://www.npmjs.com/) package managers and a Postfix service to allow sending emails through PHP [mail()](http://php.net/manual/en/function.mail.php) function.

If you dont need support for MySQL/MariaDB, or your app runs on PHP 5.4, maybe [fauria/lap](https://hub.docker.com/r/fauria/lap) suits your needs better.

Includes the following components:

 * Ubuntu 16.04 LTS Xenial Xerus base image.
 * Apache HTTP Server 2.4
 * MariaDB 10.0
 * Postfix 2.11
 * PHP 7
 * PHP modules
 	* php-bz2
	* php-cgi
	* php-cli
	* php-common
	* php-curl
	* php-dbg
	* php-dev
	* php-enchant
	* php-fpm
	* php-gd
	* php-gmp
	* php-imap
	* php-interbase
	* php-intl
	* php-json
	* php-ldap
	* php-mcrypt
	* php-mysql
	* php-odbc
	* php-opcache
	* php-pgsql
	* php-phpdbg
	* php-pspell
	* php-readline
	* php-recode
	* php-snmp
	* php-sqlite3
	* php-sybase
	* php-tidy
	* php-xmlrpc
	* php-xsl
 * Development tools
	* git
	* composer
	* npm / nodejs
	* bower
	* vim
	* tree
	* nano
	* ftp
	* curl

Installation from [Docker registry hub](https://registry.hub.docker.com/r/fauria/lamp/).
----

You can download the image using the following command:

```bash
docker pull fauria/lamp
```

Environment variables
----

This image uses environment variables to allow the configuration of some parameteres at run time:

* Variable name: LOG_STDOUT
* Default value: Empty string.
* Accepted values: Any string to enable, empty string or not defined to disable.
* Description: Output Apache access log through STDOUT, so that it can be accessed through the [container logs](https://docs.docker.com/reference/commandline/logs/).

----

* Variable name: LOG_STDERR
* Default value: Empty string.
* Accepted values: Any string to enable, empty string or not defined to disable.
* Description: Output Apache error log through STDERR, so that it can be accessed through the [container logs](https://docs.docker.com/reference/commandline/logs/).

----

* Variable name: LOG_LEVEL
* Default value: warn
* Accepted values: debug, info, notice, warn, error, crit, alert, emerg
* Description: Value for Apache's [LogLevel directive](http://httpd.apache.org/docs/2.4/en/mod/core.html#loglevel).

----

* Variable name: ALLOW_OVERRIDE
* Default value: All
* All, None
* Accepted values: Value for Apache's [AllowOverride directive](http://httpd.apache.org/docs/2.4/en/mod/core.html#allowoverride).
* Description: Used to enable (`All`) or disable (`None`) the usage of an `.htaccess` file.

----

* Variable name: DATE_TIMEZONE
* Default value: UTC
* Accepted values: Any of PHP's [supported timezones](http://php.net/manual/en/timezones.php)
* Description: Set php.ini default date.timezone directive and sets MariaDB as well.

----

* Variable name: TERM
* Default value: dumb
* Accepted values: dumb
* Description: Allow usage of terminal programs inside the container, such as `mysql` or `nano`.

Exposed port and volumes
----

The image exposes ports `80` and `3306`, and exports four volumes:

* `/var/log/httpd`, containing Apache log files.
* `/var/log/mysql` containing MariaDB log files.
* `/var/www/html`, used as Apache's [DocumentRoot directory](http://httpd.apache.org/docs/2.4/en/mod/core.html#documentroot).
* `/var/lib/mysql`, where MariaDB data files are stored.
* `/etc/apache2`, where Apache configuration files are stored.

Please, refer to https://docs.docker.com/storage/volumes for more information on using host volumes.

The user and group owner id for the DocumentRoot directory `/var/www/html` are both 33 (`uid=33(www-data) gid=33(www-data) groups=33(www-data)`).

The user and group owner id for the MariaDB directory `/var/log/mysql` are 105 and 108 repectively (`uid=105(mysql) gid=108(mysql) groups=108(mysql)`).

Use cases
----

#### Create a temporary container for testing purposes:

```
	docker run -i -t --rm fauria/lamp bash
```

#### Create a temporary container to debug a web app:

```
	docker run --rm -p 8080:80 -e LOG_STDOUT=true -e LOG_STDERR=true -e LOG_LEVEL=debug -v /my/data/directory:/var/www/html fauria/lamp
```

#### Create a container linking to another [MySQL container](https://registry.hub.docker.com/_/mysql/):

```
	docker run -d --link my-mysql-container:mysql -p 8080:80 -v /my/data/directory:/var/www/html -v /my/logs/directory:/var/log/httpd --name my-lamp-container fauria/lamp
```

#### Get inside a running container and open a MariaDB console:

```
	docker exec -i -t my-lamp-container bash
	mysql -u root
```
