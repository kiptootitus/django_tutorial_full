FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr and writing pyc files
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install system dependencies, including one version of netcat
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*  # Clean up after apt-get

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set up app home
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME/static $APP_HOME/media

# Copy project files
COPY . $APP_HOME

# Set working directory to app
WORKDIR $APP_HOME

# Copy entrypoint script and set permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh  # Ensure it's executable

# Set entrypoint script to run before the main command
ENTRYPOINT ["/entrypoint.sh"]

# Expose port for Django development server
EXPOSE 8050

# Default command (runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8050"]
