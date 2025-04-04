DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'titus') THEN
      CREATE USER titus WITH PASSWORD 'newpassword';
   END IF;
END
$$;
