#!/bin/bash

echo "Setting up mysql version 5.7.30"
docker run -d --name drupal-mysql \
    -e MYSQL_DATABASE=drupal \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=password \
    -e MYSQL_ROOT_PASSWORD=password \
mysql:5.7.30

echo "Setting up drupal version 7.69 with apache2"
docker run --name drupald -p 8012:80 --link drupal-mysql:mysql\
	-d drupal:7.69-apache

echo "Containers running"
echo "Visit http://0.0.0.0:8012 to install your drupal site"
echo "Bye"
