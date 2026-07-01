```markdown
# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## 📌 Project Overview
This project implements a self-healing infrastructure that automatically detects service failures and recovers them without human intervention. When the NGINX web server goes down, the system automatically restarts it within 30-45 seconds.

## 🎯 Objective
- Automatically detect service failures using Prometheus
- Trigger alerts via Alertmanager
- Execute automated recovery using Ansible
- Reduce downtime from hours to under a minute

## 🛠️ Tools Used
| Tool | Purpose |
|------|---------|
| **Prometheus** | Metrics collection and monitoring |
| **Alertmanager** | Alert routing and webhook delivery |
| **Ansible** | Automation and service recovery |
| **Docker** | Containerization of services |
| **Flask** | Webhook server to receive alerts |
| **Docker Compose** | Orchestrating multi-container setup |

## 📁 Project Structure
```
self-healing-demo/
├── prometheus.yml          # Prometheus configuration
├── alert_rules.yml         # Alert rules for service failure
├── alertmanager.yml        # Alertmanager webhook setup
├── restart-nginx.yml       # Ansible playbook for recovery
├── webhook_server.py       # Flask webhook server
├── docker-compose.yml      # Docker orchestration
└── README.md               # Project documentation
```

## 🔄 How It Works
```
1. NGINX Service Running ✅
        ↓
2. Prometheus Monitors Every 15s
        ↓
3. Service Fails ❌
        ↓
4. Prometheus Detects Failure (30s)
        ↓
5. Alert Fires: "NginxDown"
        ↓
6. Alertmanager Sends Webhook
        ↓
7. Flask Receives Webhook
        ↓
8. Ansible Runs Playbook
        ↓
9. NGINX Restarts Automatically ✅
        ↓
10. Service Back Online! 🎉
```

## 🚀 How to Run the Project

### Prerequisites
- Docker and Docker Compose installed
- Python 3 installed
- Ansible installed

### Step 1: Clone the Repository
```bash
git clone https://github.com/Shreya-Upadhya/self-healing-demo.git
cd self-healing-demo
```

### Step 2: Start Docker Containers
```bash
docker-compose up -d
```

### Step 3: Start Webhook Server
```bash
python3 webhook_server.py
```

### Step 4: Test Auto-Healing
```bash
# In another terminal, stop NGINX to simulate failure
docker stop nginx-demo

# Wait 30-45 seconds
# NGINX will automatically restart!
```/
```
## 📊 Access Points
| Service | URL |
|---------|-----|
| **Prometheus** | http://localhost:9090 |
| **Alertmanager** | http://localhost:9093 |
| **NGINX** | http://localhost:8080 |
| **Webhook Server** | http://localhost:5000/webhook |

## 🎯 Deliverables
- ✅ Prometheus configuration (`prometheus.yml`)
- ✅ Alertmanager webhook setup (`alertmanager.yml`)
- ✅ Ansible playbook for recovery (`restart-nginx.yml`)
- ✅ Flask webhook server (`webhook_server.py`)
- ✅ Docker Compose orchestration (`docker-compose.yml`)
- ✅ Alert rules (`alert_rules.yml`)

## 📈 Demo
The system was successfully tested by:
1. Stopping the NGINX container manually
2. Prometheus detected the failure within 30 seconds
3. Alert fired and webhook was triggered
4. Ansible automatically restarted NGINX
5. Service recovered within 45 seconds

## 📝 Conclusion
This project demonstrates key DevOps principles:
- **Automation**: No manual intervention required
- **Observability**: Full monitoring and alerting
- **Resilience**: System recovers from failures automatically
- **Self-Healing**: Infrastructure that fixes itself

```
