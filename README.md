# 🛡️ Real-Time Network Intrusion Detection System (NIDS)

An end-to-end Machine Learning and Deep Learning project focused on detecting network anomalies and cyberattacks. Starting from classical ML baselines on historical data, moving towards Deep Learning, and aiming for deployment as a live-traffic analysis tool on edge devices (Raspberry Pi).

---

## 🚀 Project Vision & Roadmap

The project is structured into **4 operational sprints**, moving from offline data exploration to real-world edge deployment.

### 📊 Sprint 1: Data Foundations & Classical ML Baselines (Current)
* Detailed Exploratory Data Analysis (EDA) of the NSL-KDD dataset.
* Addressing heavy-tailed feature distributions and massive outliers (`src_bytes`, `dst_bytes`).
* Feature engineering: One-Hot Encoding handling high cardinality for network services.
* Implementing and evaluating classical ML models (Logistic Regression vs. Random Forest).

### 🧠 Sprint 2: Deep Learning & MLOps Refactoring
* Transitioning from scikit-learn to Deep Learning using **TensorFlow/Keras** (Multi-Layer Perceptrons).
* Decoupling code from Jupyter Notebooks into a clean, modular Python package (`src/`).
* Exporting trained models and preprocessing pipelines using `joblib`.
* Exposing the model via a high-performance **FastAPI** web service for inference.

### 🎛️ Sprint 3: Live Traffic Ingestion & Feature Aggregation
* Setting up live packet capture on local interfaces using **Tshark / Scapy**.
* **The Core Challenge:** Building a real-time data pipeline to aggregate raw, individual network packets into time-windowed statistical features that match the model's expected input structure.

### 🍓 Sprint 4: Edge Deployment on Raspberry Pi
* Optimizing the deep learning model for constrained hardware (TensorFlow Lite / ONNX quantization).
* Deploying the end-to-end capture and prediction script onto a **Raspberry Pi**.
* Establishing an alerting system for real-time anomaly detection within a local network tap.

---

## 📦 Dataset & Core Challenge

The project utilizes the **NSL-KDD dataset** (125,973 training samples, 22,544 test samples) consisting of 41 network connection features.

> ⚠️ **The Generalization Gap:** The official `KDDTest.txt` file contains **17 novel attack types** that are completely absent from the training set. This simulates realistic zero-day exploits, making it a strict test of the model's ability to generalize, rather than just memorize.

---

## 📈 Results So Far

We evaluated our models under two scenarios: the **Official Split** (testing against zero-day attacks) and a **Random Split** (testing against known attacks).

| Model | Evaluation Split | Precision (Attack) | Recall (Attack) | F1-Score | Key Insight |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Logistic Regression** | Official Split | 0.92 | 0.61 | 0.73 | Baseline. Suffers from heavy outliers and strict linearity. |
| **Random Forest** | Official Split | **0.97** | 0.63 | 0.76 | Excellent precision, but drops recall when facing unseen zero-day attacks. |
| **Random Forest** | Random 80/20 Split | **1.00** | **0.99** | **1.00** | Proves near-perfect capability in detecting *known* network attack patterns. |

### Top 15 Feature Importances (Random Forest)
Analysis shows that **`src_bytes`** and **`dst_bytes`** are the ultimate discriminators for high-volume traffic anomalies (e.g., DoS), followed closely by connection flags (`flag_SF`), which highlight structural network protocol violations.

---
