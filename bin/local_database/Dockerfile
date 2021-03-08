ARG POPSTGRES_VERSION=10.4-alpine
FROM postgres:${POPSTGRES_VERSION}

ENV POSTGRES_USER d2platform_adm
ENV POSTGRES_PASSWORD d2platform_adm
ENV POSTGRES_DB d2platform_db

RUN mkdir -p /tablespace/data \
    && mkdir -p /tablespace/index \
    && mkdir -p /tablespace/tsd_d2platform \
    && mkdir -p /tablespace/tsi_d2platform \
    && chown -R postgres:postgres /tablespace \
    && chmod 777 /tablespace/data \
    && chmod 777 /tablespace/index \
    && chmod 777 /tablespace/tsd_d2platform \
    && chmod 777 /tablespace/tsi_d2platform

COPY initial_migrate.sql /docker-entrypoint-initdb.d/