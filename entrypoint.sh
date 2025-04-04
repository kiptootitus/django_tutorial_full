#!/bin/sh
# Exit immediately on error
set -e

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT..."
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 0.5
done
echo "PostgreSQL is available!"

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Start the server
exec "$@"
