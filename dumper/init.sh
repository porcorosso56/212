#/usr/bin/env bash

pg_createcluster -g 1000 -u 1000 12 cluster
pg_ctlcluster 12 cluster start
su - user -c "createdb user"
su - user -c "psql -c 'CREATE SCHEMA schema_ CREATE TABLE packages (name text UNIQUE, version text)'"