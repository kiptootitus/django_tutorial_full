-- Create a user
CREATE USER titus WITH PASSWORD 'newpassword';

-- Create a database
CREATE DATABASE tutorial OWNER titus;

-- Optional: Grant all privileges to the user on the database
GRANT ALL PRIVILEGES ON DATABASE tutorial TO titus;
