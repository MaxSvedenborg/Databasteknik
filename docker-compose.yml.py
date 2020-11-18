version: "3"

services:
  db:
    image: mysql:latest
    container_name: "Mysql_DB"
    ports:
      - "33007:3306"
    cap_add:
      - SYS_NICE
      environment:
        MYSQL_TOOT_PASSOWRD = mysql
        mysql_database = database2
