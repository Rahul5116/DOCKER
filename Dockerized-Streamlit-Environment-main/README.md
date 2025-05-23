# Dockerized Streamlit Development Environment 🚀

## Prerequisites
Ensure you have the following installed on your machine:

- **Docker 🐳** (Ensure the Docker daemon is running)
- **Python 3.9+ 🐍** (Verify installation with `python --version`)
- **pip** (Ensure it's installed and up to date with `pip --version`)
- Basic knowledge of **Streamlit 📊**

---

## 📂 Directory Structure
```
project_root/
│── .streamlit/
│   └── config.toml
│── src/
│   └── main.py
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 📜 File Explanations

### 1️⃣ .streamlit/config.toml
Configures Streamlit settings for local development.
```toml
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
```

### 2️⃣ src/main.py
Contains the core logic of the Streamlit application:

- A **home page 🏠** for introduction.
- A **data explorer 📊** to upload and inspect CSV files.
- A **visualization page 📈** for interactive charts and graphs.

### 3️⃣ Dockerfile
Defines the containerized environment.
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8501
CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 4️⃣ requirements.txt
Contains necessary dependencies:
```
streamlit
pandas
numpy
matplotlib
plotly
```

---

## ⚡ Steps to Run the Project

1️⃣ Navigate to the project directory:
```bash
cd path/to/project_root
```

2️⃣ Build the Docker image:
```bash
docker build -t streamlit-app .
```

3️⃣ Run the container:
```bash
docker run -p 8501:8501 streamlit-app
```

4️⃣ Open in Browser:
```plaintext
http://localhost:8501 🌐
```

---

## 🎯 Conclusion
You now have a fully functional Streamlit environment running inside Docker! 🚀

