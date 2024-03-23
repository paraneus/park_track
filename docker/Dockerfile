FROM almalinux:9.3

# Reasonable basics
RUN dnf -y install epel-release
RUN dnf -y install \
	uwsgi \
	uwsgi-plugin-python3.x86_64 \
	uwsgi-router-http.x86_64 \
	python3-pip.noarch \
	lsof \
	procps \
	which \
	supervisor \
	sudo \
	iproute \
	tcpdump \
	net-tools\
	gcc \
	python3-devel \
	libpq-devel \
	jq
RUN dnf -y update

# User, Permissions and application file dependencies
RUN groupadd app_user
RUN useradd app_user -g app_user
RUN mkdir -p /opt/backend
RUN chown app_user:app_user /opt/backend

# uWSGI
COPY docker/uwsgi_config.ini /opt/backend/
RUN mkdir /opt/backend/ssl
COPY docker/ssl/* /opt/backend/ssl/

# SupervisorD
COPY docker/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY docker/supervisor/conf.d/*.conf /etc/supervisor/conf.d-available/
RUN mkdir /etc/supervisor/conf.d

# DB Access
COPY docker/pgpass /home/app_user/.pgpass
COPY docker/pgpass /root/.pgpass
RUN chown app_user:app_user /home/app_user/.pgpass
RUN chmod 600 /home/app_user/.pgpass
RUN chmod 600 /root/.pgpass

# Startup Script
COPY docker/run-app.sh /usr/local/bin/run-app
RUN chmod +x /usr/local/bin/run-app

# Switch directories
WORKDIR /opt/backend/
USER root

CMD ["/usr/local/bin/run-app"]
