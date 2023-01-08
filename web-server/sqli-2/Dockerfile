FROM php:8-apache
COPY challenge/ /var/www/html/
WORKDIR /var/www/html
RUN php setup.php && rm -f setup.php