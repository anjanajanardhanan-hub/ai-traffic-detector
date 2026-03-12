# 🚦 AI Traffic Detector

AI-Based Network Traffic Anomaly Detection System using **Machine Learning, Flask, and AWS EC2**

---

## 🚀 Project Overview

This project detects abnormal network traffic patterns that may indicate cyber threats such as **DDoS attacks**.

The system analyzes network traffic data using a **Machine Learning model (Isolation Forest)** and displays the results through a **web-based monitoring dashboard.

---

## 📸 Project Screenshots

### Login Page

![Login Page](login.png)

### Monitoring Dashboard

![Dashboard](dashboard.png)

### Traffic Graph

![Graph](graph.png)

### Traffic Data Table

![Table](table.png)

---

## ⚙️ Tech Stack

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### Machine Learning

* Isolation Forest Algorithm

### Cloud Platform

* AWS EC2

---

## 📊 System Workflow

1️⃣ User enters network traffic values

* Requests per minute
* Failed requests

2️⃣ Flask backend processes the input.

3️⃣ The Machine Learning model analyzes the traffic pattern.

4️⃣ The system determines whether the traffic is **Normal or Anomalous**.

5️⃣ The system also displays **IP location information**.

---

## 🧠 Machine Learning Model

**Algorithm Used:**
Isolation Forest

**Purpose:**
Detect abnormal network behavior based on traffic patterns.

---

## 📂 Project Structure

ai-traffic-detector
│
├── app.py
├── model.py
├── graph.py
├── dataset.csv
│
├── templates
│   ├── login.html
│   └── index.html
│
├── static
│   └── graph.png
│
├── login.png
├── dashboard.png
├── graph.png
├── table.png
└── README.md

---

## 👨‍💻 Team

**BCA Academic Project — Izee Business School**

| Name               | Role              |
| ------------------ | ----------------- |
| Anjana Janardhanan | Project Developer |
| Adithya            | Team Member       |
| Greeshma           | Team Member       |

---

## ☁️ Deployment

The application is deployed on **AWS EC2**, allowing the system to run as a cloud-based monitoring dashboard accessible through a public IP address.

---

## 📜 License

This project is developed for **educational purposes**.

---

⭐ Built using **Python, Machine Learning, and AWS**
