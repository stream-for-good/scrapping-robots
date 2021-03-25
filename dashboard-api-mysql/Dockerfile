FROM alpine
RUN apk update && apk add  gcc musl-dev bash openrc curl composer nano


# Install Nginx and PHP
RUN apk add  nginx php


# Install Tools & Dev Compiler
RUN apk add wget unzip git libssh2

RUN apk add php7-fpm  php7-cli php7-opcache php7-gd php7-ctype php7-tokenizer php7-session \
	php7-mbstring php7-pdo php7-pear php7-xml php7-simplexml php7-xmlrpc php7-xdebug php7-zip php7-zlib \
	php7-intl php7-soap php7-pgsql php7-mysqli php7-simplexml php7-pdo_mysql php7-zlib php7-curl php-dom




#copy conf and basic web pages
COPY ./conf/nginx.conf /etc/nginx/
COPY ./conf/www.conf /etc/php7/php-fpm.d/

RUN mkdir /var/www/html
RUN  ln -s /usr/share/nginx/html /var/www/html/ && chown -R nginx:nginx /var/www/html/

RUN rm  ./etc/nginx/conf.d/default.conf

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# Startup Script to run PHP-FPM and Nginx
COPY ./script/start.sh /tmp/
RUN chmod +x /tmp/start.sh && mkdir /run/php-fpm/


VOLUME /etc/nginx/
VOLUME /var/www/

RUN chmod 777 var/lib/php7/

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["/tmp/start.sh"]
