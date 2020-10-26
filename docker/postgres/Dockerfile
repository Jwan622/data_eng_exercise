FROM postgres:11.3 AS postgres

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password

ADD CreateTables.sql /docker-entrypoint-initdb.d/CreateTables.sql
