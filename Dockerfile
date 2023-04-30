FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y default-libmysqlclient-dev python3-dev build-essential

RUN apt-get install supervisor default-mysql-client -y
RUN mkdir -p var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV MYSQL_HOST=${MYSQL_HOST:-localhost}
ENV MYSQL_PORT=${MYSQL_PORT:-3306}
ENV MYSQL_USER=${MYSQL_USER:-xxxx}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD:-xxxxx}
ENV MYSQL_DBNAME=${MYSQL_DBNAME:-todo4}

RUN chmod +x ./entrypoint.sh

EXPOSE 3030/tcp

# CMD [ "/usr/bin/supervisord" ]
CMD [ "./entrypoint.sh" ]
