# 🚀 MySQL in Docker Container with Initialization Script

## 📂 Project Structure
```
Docker-MYSQL/
│── Dockerfile
│── Rahul_demo.sql
```

## 📌 Prerequisites
- Docker installed
- Docker running
- Basic understanding of Docker commands

---

## 🛠 Step 1: Create a Dockerfile

```dockerfile
# 🏗 Use the official MySQL image
FROM mysql:latest

# 📂 Copy the initialization script to the container
COPY Rahul_demo.sql /docker-entrypoint-initdb.d/

# 🔥 Expose MySQL port
EXPOSE 3306
```

---

## 📜 Step 2: SQL Initialization Script
Create `Rahul_demo.sql` with the following content:

```sql
CREATE DATABASE rahul;
USE rahul;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    age INT
);

INSERT INTO users (username, age) VALUES ('Rahul', 21), ('xyz', 21);

```

---

## 🏗 Step 3: Build the Docker Image

```bash
docker build -t mysql-custom .
```

---

## 🚀 Step 4: Run MySQL Container

```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -d mysql-custom
```

---

## 🔍 Step 5: Access the Running Container

```bash
docker exec -it mysql-container bash
```

---

## 💻 Step 6: Connect to MySQL

```bash
mysql -u root -p
```

(Enter the password as `root`)

---

## 🏗 Step 7: Verify Database and Tables

```sql
SHOW DATABASES;
USE Rahul;
SELECT * FROM students;
```

---

## 🎉 Conclusion
You have successfully set up MySQL in a Docker container with an initialization script. The database and tables are automatically created when the container starts. ✅

