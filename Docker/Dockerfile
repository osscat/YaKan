FROM centos
RUN yum -y update
RUN yum -y install httpd
RUN yum -y install epel-release
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
RUN yum -y install --enablerepo=remi mod_proxy_uwsgi
COPY ./conf/wsgi.conf /etc/httpd/conf.d
COPY ./conf/documentroot.conf /etc/httpd/conf.d
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip

RUN mkdir -p /home/java/app
RUN python3.6 -m venv /home/java/app/venv
RUN source /home/java/app/venv/bin/activate

RUN pip3.6 install --upgrade pip
RUN pip3.6 install Django==2.0.6
RUN pip3.6 install djangorestframework
RUN pip3.6 install psycopg2
RUN pip3.6 install django-cors-headers
RUN pip3.6 install django-filter==1.1.0
RUN pip3.6 install django-rest-auth
RUN pip3.6 install djangorestframework-jwt
RUN pip3.6 install django-allauth
RUN yum install -y httpd-devel
RUN yum -y install make
RUN yum -y install gcc
RUN yum -y install python-devel
RUN pip3.6 install mod_wsgi
RUN pip3.6 install mod-wsgi-httpd
RUN pip3.6 install channels_redis
RUN pip3.6 install asgi_redis
RUN pip3.6 install asgiref==2.3.0
RUN pip3.6 install -U channels
RUN pip3.6 install daphne

RUN pip3.6 install uwsgi

RUN yum install -y git
RUN yum install -y npm
RUN yum -y install uwsgi-plugin-python36u

RUN cd /home/java/app && git clone https://github.com/osscat/YaKan.git
COPY ./settings/prod.env.js /home/java/app/YaKan/Client/config
RUN cd /home/java/app/YaKan/Client && npm install && npm run build

COPY ./settings/uwsgi.ini /home/java/app/YaKan
COPY ./settings/settings.py /home/java/app/YaKan/YaKan/settings.py
COPY ./settings/asgi.py /home/java/app/YaKan/YaKan
COPY ./settings/routing.py /home/java/app/YaKan/YaKanSocket

RUN cd /home/java/app/YaKan/ && python3.6 manage.py collectstatic --noinput
RUN cp -r /home/java/app/YaKan/Client/dist/ /var/www/html/

RUN mkdir -p /home/java/app/log
RUN mkdir -p /home/java/app/YaKan

# RUN cd /home/java/app/YaKan && python3.6 manage.py createsuperuser
# RUN cd /home/java/app/YaKan && python3.6 manage.py makemigrations
# RUN cd /home/java/app/YaKan && python3.6 manage.py migrate

COPY ./conf/00-proxy.conf /etc/httpd/conf.modules.d

#RUN cd /home/java/app/YaKan/ && python3.6 manage.py makemigrations
#RUN cd /home/java/app/YaKan/ && python3.6 manage.py migrate

COPY ./startup.sh /startup.sh
RUN chmod +x /startup.sh
#ENTRYPOINT ["bash"]
#CMD ["/startup.sh"]

#CMD ["usr/sbin/httpd", "-DFOREGROUND"]
#RUN cd /home/java/app/YaKan && uwsgi --ini uwsgi.ini
#CMD ["usr/sbin/httpd", "-DFOREGROUND"]
