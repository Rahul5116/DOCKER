# 🏗 Use the official MySQL image
FROM mysql:latest

# 📂 Copy the SQL script to the container's initialization directory
COPY rahul_demo.sql /docker-entrypoint-initdb.d/

# 🔥 Expose MySQL port
EXPOSE 3306
