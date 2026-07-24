# 🚀 Cloud Native Monitoring Platform

A Kubernetes-based monitoring platform built using **Flask, Docker, Kubernetes, Prometheus, Grafana, and GitHub Actions**.

---

## 📌 Architecture

```
                    GitHub
                       │
                       ▼
               GitHub Actions
                       │
                       ▼
                Docker Hub Image
                       │
                       ▼
                 Kubernetes Cluster
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   Monitoring App             Prometheus
     (/metrics)                    │
          │                        │
          └──────────────┬─────────┘
                         ▼
                     Grafana
```

---

## ✨ Features

- Dockerized Flask application
- Prometheus metrics endpoint
- Kubernetes Deployment & Service
- Prometheus monitoring
- Grafana dashboards
- GitHub Actions CI/CD pipeline
- Custom Prometheus alert rules

---

## 🛠 Tech Stack

- Python
- Flask
- Docker
- Kubernetes (Minikube)
- Prometheus
- Grafana
- GitHub Actions
- Docker Hub

---

## 📂 Project Structure

```
monitoring-platform/

├── app/
├── kubernetes/
├── monitoring/
│   ├── prometheus/
│   ├── grafana/
│   └── alertmanager/
├── dashboards/
├── alerts/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md
```

---

## 🚀 CI/CD Pipeline

```
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Install Dependencies
    │
    ▼
Build Docker Image
    │
    ▼
Push Image to Docker Hub
```

---

## 📊 Monitoring Flow

```
Flask Application
       │
       ▼
   /metrics endpoint
       │
       ▼
Prometheus Scrapes Metrics
       │
       ▼
Stores Time-Series Data
       │
       ▼
Grafana Dashboards
```

---

## 🚨 Alert Rules

Implemented alerts:

- Application Down
- High Response Time
- No Traffic
- Prometheus Down

---

## ▶️ Run Locally

### Start Minikube

```bash
minikube start
```

### Deploy Application

```bash
kubectl apply -f kubernetes/
```

### Deploy Monitoring Stack

```bash
kubectl apply -f monitoring/prometheus/
kubectl apply -f monitoring/grafana/
```

---

## Access Services

Application

```bash
kubectl port-forward svc/monitoring-service 5000:5000 -n monitoring
```

Open:

```
http://localhost:5000
```

Prometheus

```bash
kubectl port-forward svc/prometheus-service 9090:9090 -n monitoring
```

Open:

```
http://localhost:9090
```

Grafana

```bash
kubectl port-forward svc/grafana-service 3000:3000 -n monitoring
```

Open:

```
http://localhost:3000
```

Default Login

```
Username: admin
Password: admin
```

---

## 📈 Screenshots

- Application
- Prometheus
- Grafana Dashboard
- GitHub Actions Pipeline

(Add screenshots from your project here.)

---

## 👨‍💻 Author

**Harish M**

GitHub: https://github.com/HARISH07-1
