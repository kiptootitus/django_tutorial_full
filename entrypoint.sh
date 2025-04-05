#!/bin/sh


if [ "$DATABASE" = "tutorial" ]
then
    echo "Waiting for tutorial..."
    while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi
python manage.py migrate
exec "$@"