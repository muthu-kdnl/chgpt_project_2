FROM postgres:16-alpine

# Step 2: Set environment variables (Defaults - can be overridden)
ENV POSTGRES_USER=test
ENV POSTGRES_PASSWORD=test_123
ENV POSTGRES_DB=test_db

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

