FROM mysql:5.7

# RUN apt update && apt upgrade
# RUN apt-get install -y vim tzdata && \
#     cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# ARG TZ=Asia/Tokyo
# ENV TZ ${TZ}
# RUN echo $TZ > /etc/timezone

COPY conf.d/my.cnf /etc/mysql/mysql.conf.d/
RUN touch /var/log/mysql/mysqld.log
