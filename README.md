# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## Project Overview

This project implements a self-healing infrastructure that automatically detects service failures and recovers them without human intervention. When the NGINX web server goes down, the system automatically restarts it within **30–45 seconds**.

## Objective

- Automatically detect service failures using Prometheus
- Trigger alerts via Alertmanager
- Execute automated recovery using Ansible
- Reduce downtime from hours to under a minute

## Tools Used

| Tool | Purpose |
|------|---------|
| **Prometheus** | Metrics collection and monitoring |
| **Alertmanager** | Alert routing and webhook delivery |
| **Ansible** | Automation and service recovery |
| **Docker** | Containerization of services |
| **Flask** | Webhook server to receive alerts |
| **Docker Compose** | Orchestrating multi-container setup |

## Project Structure

```text
self-healing-demo/
├── .git/                    
├── venv/                   
├── .gitignore               
├── alert_rules.yml          
├── alertmanager.yml         
├── docker-compose.yml       
├── prometheus.yml           
├── restart-nginx.yml        
└── webhook_server.py        
```

## How It Works

```text
1. NGINX Service Running 
        ↓
2. Prometheus Monitors Every 15 Seconds
        ↓
3. Service Fails ❌
        ↓
4. Prometheus Detects Failure
        ↓
5. Alert Fires: "NginxDown"
        ↓
6. Alertmanager Sends Webhook
        ↓
7. Flask Receives Webhook
        ↓
8. Ansible Executes Recovery Playbook
        ↓
9. NGINX Restarts Automatically ✅
        ↓
10. Service Back Online 
```

## How to Run the Project

### Prerequisites

- Docker
- Docker Compose
- Python 3
- Ansible

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shreya-Upadhya/self-healing-demo.git
cd self-healing-demo
```

### Step 2: Start Docker Containers

```bash
docker-compose up -d
```

### Step 3: Start the Webhook Server

```bash
python3 webhook_server.py
```

### Step 4: Test the Self-Healing Mechanism

```bash
# Stop the NGINX container to simulate a failure
docker stop nginx-demo

# Wait approximately 30–45 seconds
# The monitoring system will detect the failure,
# trigger Alertmanager, and Ansible will restart NGINX automatically.
```

## Access Points

| Service | URL |
|---------|-----|
| **Prometheus** | http://localhost:9090 |
| **Alertmanager** | http://localhost:9093 |
| **NGINX** | http://localhost:8080 |
| **Webhook Server** | http://localhost:5000/webhook |

## Deliverables

- Prometheus configuration (`prometheus.yml`)
- Alert rules (`alert_rules.yml`)
- Alertmanager configuration (`alertmanager.yml`)
- Ansible recovery playbook (`restart-nginx.yml`)
- Flask webhook server (`webhook_server.py`)
- Docker Compose setup (`docker-compose.yml`)

## Demo Workflow

The system was successfully tested using the following workflow:

1. Manually stopped the NGINX container.
2. Prometheus detected the service failure.
3. Alertmanager generated and forwarded an alert via webhook.
4. Flask webhook server received the alert.
5. Ansible executed the recovery playbook.
6. NGINX restarted automatically.
7. Service became available again within **30–45 seconds**.

## Conclusion

This project demonstrates several key DevOps practices:

- **Automation** – Recovery occurs without manual intervention.
- **Observability** – Continuous monitoring using Prometheus.
- **Alerting** – Immediate notifications through Alertmanager.
- **Resilience** – Services recover automatically from failures.
- **Self-Healing Infrastructure** – Reduced downtime and improved system reliability.

---

### Tech Stack

- Prometheus
- Alertmanager
- Ansible
- Docker
- Docker Compose
- Flask (Python)
- NGINX
