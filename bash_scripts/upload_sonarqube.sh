#! /bin/bash

echo "Building tag of lastest sonarq image"
docker build --tag sonarq .

echo "Running docker into localhost"
docker run -d -p 9000:9000 sonarq

echo "Remember admin admin is the key"