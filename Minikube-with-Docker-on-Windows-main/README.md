# Minikube with Docker on Windows ☸️

## What is Minikube?
Minikube is a tool that helps you run a local Kubernetes cluster on your machine. It's perfect for developers who want to experiment with Kubernetes without setting up a large cloud infrastructure. Minikube simplifies the process of deploying and managing Kubernetes clusters locally without the need for extensive resources.

## What is Kubernetes? ☸️
Kubernetes is an open-source platform for automating the deployment, scaling, and management of containerized applications. It allows you to:
- Deploy applications in containers across clusters.
- Scale applications up or down with ease.
- Manage containerized workloads with minimal effort.
- Ensure high availability, load balancing, and fault tolerance.

## ✅ Step 1: Install Required Tools

### 1. Install Docker Desktop 🐋
- Download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop/).
- Ensure WSL 2 backend is enabled (recommended).

### 2. Install Minikube 📦
If you have Chocolatey installed, run:
```bash
choco install minikube
```
Alternatively, install it manually from the [Minikube website](https://minikube.sigs.k8s.io/docs/).

### 3. Install kubectl
```bash
choco install kubernetes-cli
```
Verify the installation:
```bash
kubectl version --client
```

## ✅ Step 2: Start Minikube with Docker Driver 🐳
Ensure Docker Desktop is running in the background:
```bash
minikube start --driver=docker
```
Check the status:
```bash
minikube status
```

## ✅ Step 3: Deploy an Application 🚀

### 1. Create an Nginx Deployment
```bash
kubectl create deployment nginx --image=nginx
```

### 2. Expose the Deployment 🔓
```bash
kubectl expose deployment nginx --type=NodePort --port=80
```

### 3. Get the Service URL 🔗
```bash
minikube service nginx --url
```
Open the URL in your browser to see the running Nginx web server. 🌐

## ✅ Step 4: Manage Kubernetes Cluster

### 1. Check Running Pods 📋
```bash
kubectl get pods
```

### 2. Scale the Deployment 📏
```bash
kubectl scale deployment nginx --replicas=3
```
Check pods again:
```bash
kubectl get pods
```

### 3. Delete the Deployment 🧹
```bash
kubectl delete service nginx
kubectl delete deployment nginx
```

## ✅ Step 5: Stop and Delete Minikube 🗑️
```bash
minikube stop
minikube delete
```

## 🎯 Conclusion
By using Minikube with Docker, you can run Kubernetes locally without needing Hyper-V or VirtualBox. Docker provides an easy way to manage your cluster and experiment with Kubernetes.

🚀😊

