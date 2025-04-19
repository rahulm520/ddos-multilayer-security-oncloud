# 🛡️ Azure-Based Multi-Layered DDoS Prevention System

This project implements a **three-layered DDoS protection architecture** entirely on Microsoft Azure. Designed to run even on the **Azure Student subscription**, the system features:

- **Layer 1**: Azure WAF using Application Gateway  
- **Layer 2**: Machine Learning API (Random Forest) to detect traffic anomalies  
- **Layer 3**: Honeypot system with reCAPTCHA to trap and log intrusion attempts  

---

## 📂 Project Structure

```
├── ddos-ml-detector/
│   ├── train.py          # ML model trainer (Random Forest)
│   ├── app.py            # Flask API for live predictions
│   └── model.pkl         # Trained ML model
│
├── honeypot/
│   ├── honeypot.py       # Fake login page + attack logger
│   └── attack_logs.txt   # Honeypot log file
│
└── Project Complete Guide.pdf   # Project setup and usage guide (replacing PDF)
```

---

## 🚀 Quick Overview

| Layer | Purpose | Technology |
|-------|---------|------------|
| **1** | Block known IPs, countries, rate-limited traffic | Azure WAF (App Gateway) |
| **2** | Detect unknown traffic spikes | Flask + Scikit-learn |
| **3** | Log attacker details and bot traffic | Honeypot + Google reCAPTCHA |

---

## 🔧 Getting Started

To deploy the full solution step-by-step, **please refer to**:

📘 [`Project Complete Guide.pdf`](./Project%20Complete%20Guide.pdf)

It contains:
- Setup instructions for VMs, networks, ports
- Screenshots & image references
- Code integration steps for all three layers
- Testing checklist (slowloris, curl, VPN testing, reCAPTCHA setup)

---

## 🔗 Live Source Code

- **ML Training**: [`train.py`](https://github.com/rahulm520/ddos-multilayer-security-oncloud/blob/main/train.py)  
- **Prediction API**: [`app.py`](https://github.com/rahulm520/ddos-multilayer-security-oncloud/blob/main/app.py)  
- **Honeypot Server**: [`honeypot.py`](https://github.com/rahulm520/ddos-multilayer-security-oncloud/blob/main/honeypot.py)

---
## 📸 Screenshots
![honeypot Intrusion Report](https://github.com/user-attachments/assets/620a71a1-817a-41a2-aa73-c4b83d9a21e9)
![Honeypot](https://github.com/user-attachments/assets/65aacd8f-e193-4aa2-9138-e7895ee8277c)
![ML Anomly Detection API](https://github.com/user-attachments/assets/62a1e013-3a0d-48c0-a984-e839586f455e)


## 👨‍💻 Author

**Rahul Rao M**  
rahulroxx2002@gmail.com
