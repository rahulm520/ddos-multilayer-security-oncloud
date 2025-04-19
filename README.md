# 🛡️ DDoS Prevention System using Multi-Layered Architecture (Azure-Based)

A cloud-native project that implements a robust, three-layered defense system to detect and prevent Distributed Denial-of-Service (DDoS) attacks using Microsoft Azure. Combines WAF, ML anomaly detection, and honeypots with CAPTCHA.

---

## 📚 Table of Contents

- [Overview](#-project-overview)
- [Architecture](#-architecture)
- [Technologies Used](#-technologies-used)
- [Deployment Steps](#-deployment-steps)
  - [Layer 1: Web Application Firewall](#1️⃣-layer-1-web-application-firewall)
  - [Layer 2: Machine Learning API](#2️⃣-layer-2-machine-learning-api)
  - [Layer 3: Honeypot with CAPTCHA](#3️⃣-layer-3-honeypot-with-captcha)
- [Testing Tools](#-testing-tools)
- [Screenshots](#-screenshots)
- [Project Outcome](#-project-outcome)
- [Author](#-author)

---

## 🧠 Project Overview

This project showcases a multi-tiered strategy to combat DDoS attacks by:
1. Filtering requests at the **perimeter using Azure WAF**.
2. Detecting anomalies in traffic patterns using a **Flask-based ML API**.
3. Logging suspicious users through a **honeypot login system with reCAPTCHA**.

---

## 🏗️ Architecture

```
            ┌────────────────────────┐
            │     Azure WAF Layer    │
            └──────────┬─────────────┘
                       │
             [Filtered Legit Traffic]
                       │
            ┌──────────▼──────────┐
            │   ML Detection API  │
            └──────────┬──────────┘
                       │
             [Suspicious Traffic]
                       │
            ┌──────────▼──────────┐
            │ Honeypot w/ CAPTCHA │
            └─────────────────────┘
```

---

## 🛠️ Technologies Used

- **Microsoft Azure (Student Account)**
- **Azure Application Gateway WAF**
- **Azure Ubuntu VM**
- **Python, Flask**
- **Scikit-learn (RandomForest)**
- **Joblib, Requests**
- **hping3, slowloris (testing)**
- **HTML + Google reCAPTCHA**
- **VS Code + Git + GitHub**

---

## 🚀 Deployment Steps

### 1️⃣ Layer 1: Web Application Firewall

1. Create Azure **Application Gateway**.
2. Enable **WAF Policy** → Activate OWASP 3.2+.
3. Add **Custom Rules**:
   - Block specific IPs
   - Geo-block countries
   - Rate limit traffic

4. Associate WAF to the **VM's public IP**.

### 2️⃣ Layer 2: Machine Learning API

1. Launch a **Linux VM (Ubuntu)**.
2. Open port `5000` in NSG.
3. Clone and run Flask API:

```bash
pip install flask scikit-learn joblib
python3 app.py
```

4. Sample API Request:
```bash
curl -X POST http://<vm_ip>:5000/predict \
-H "Content-Type: application/json" \
-d '{"packet_rate":750,"connection_count":120,"ip_entropy":0.2}'
```

Returns:
```json
{ "is_anomalous": true }
```

### 3️⃣ Layer 3: Honeypot with CAPTCHA

1. Reuse or create new **VM**.
2. Install Flask and run:

```bash
sudo python3 honeypot.py
```

3. Fake login page captures:
   - Username
   - IP
   - Timestamp

4. Logs are saved in `attack_logs.txt`.

---

## 🧪 Testing Tools

| Tool     | Command Example                                  |
|----------|--------------------------------------------------|
| Slowloris | `python3 slowloris.py <IP>`                    |
| hping3   | `sudo hping3 -S --flood -p 80 <IP>`             |
| curl     | `curl -X POST -d '{}' http://<IP>:5000/predict` |

---

## 📸 Screenshots

Add your screenshots here:
- Azure WAF custom rule page
- ML API running (`🚀 API is Live`)
- Honeypot login page
- Logs from `attack_logs.txt`

---

## ✅ Project Outcome

- 🔐 First-layer security via **Azure WAF**.
- 🧠 Intelligent real-time traffic analysis via **ML API**.
- 🕵️ Trap + log intruders via **Honeypot System**.
- ✅ Real-world testing simulated with DDoS tools.

---

## 👨‍💻 Author

**Rahul Rao M**  
MCA @ Jain University  
Security + Cloud Enthusiast | Builder of Secure Azure Apps  

---

## 📎 License

This project is open-sourced.
```
