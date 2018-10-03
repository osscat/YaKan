YaKan
====

YaKan is a simple task management tool.
It has a feature to automatically count man-hours of tasks.

## Description

## Install
We have prepared DockerFile.

  Dockerfile
  conf/
  docker-compose.xml
  init/
  settings/
  startup.sh

Please rewrite the contents of "settings/prod.env.js" before execution.
Replace 153.126.177.192 with your server's IP address.

It forwards to port 10080.
If you change the port, please rewrite docker-compose.xml.

When you are ready, execute the following command.

  docker-compose build  // create image file
  docker-compose up -d  // create container
  docker exec -it yakan-main /bin/bash  // execute

After execution, create a Django administrator user in the container.

  cd /home/java/app/YaKan
  python3.6 manage.py createsuperuser


After completing the above work, you access "http://xxx.xxx.xxx.xxx:10080/#/login".

## Licence

## Author