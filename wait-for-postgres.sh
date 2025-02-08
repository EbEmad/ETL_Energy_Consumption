#!/bin/sh
set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=123456 psql -h "$host" -U "postgres" -d "energy_consumption" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 3
done

>&2 echo "Postgres is up - executing command"
exec $cmd
