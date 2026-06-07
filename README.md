# 🛡️ CyberLens Shield: AI-Powered Phishing URL Detector

CyberLens Shield is a high-performance security diagnostic tool developed as a B.Tech Capstone Project. It leverages Machine Learning to detect malicious phishing URLs in real-time, moving beyond traditional blacklist-based filtering.

## 🎯 Project Overview
In an era of increasingly sophisticated social engineering attacks, static blacklists are often insufficient. CyberLens Shield utilizes a **Random Forest Classifier** trained on extensive datasets to analyze behavioral and lexical URL patterns, identifying zero-day phishing attempts with high precision.



[Image of supervised machine learning workflow]


## 🚀 Key Features
* **AI-Driven Inference:** Uses a trained Random Forest model to predict URL safety in milliseconds.
* **Automated Feature Engineering:** Extracts 24+ critical features (e.g., URL length, domain age, presence of sensitive keywords, redirect counts, and TLD entropy).
* **Professional UI/UX:** A modern, dark-mode Command Center built with `customtkinter`, designed for a SOC (Security Operations Center) environment.
* **Real-time Diagnostics:** Provides immediate threat intelligence with clear visual indicators for "Safe" vs "Danger" status.
* **Intelligent Detection:** Random Forest model with 99%+ confidence.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Machine Learning:** `scikit-learn`, `pandas`, `joblib`
* **UI Framework:** `customtkinter`
* **Development Tools:** VS Code, Git, MacOS Terminal Automation

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Komalrai26/CYBERLENS_SHIELD.git](https://github.com/Komalrai26/CYBERLENS_SHIELD.git)
   cd CYBERLENS_SHIELD
   # 🛡️ CyberLens Shield: AI-Powered Phishing URL Detector
**B.Tech Capstone Project | Machine Learning | Cybersecurity**

CyberLens Shield is a high-performance security diagnostic tool that utilizes a **Random Forest Classifier** to identify malicious URLs in real-time, moving beyond traditional blacklist-based filtering.

## 💻 How to Run Locally
1. Clone the repo: `git clone https://github.com/Komalrai26/CYBERLENS_SHIELD.git`
2. Set up virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
3. Install dependencies: `pip install -r requirement.txt`
4. Launch: `python3 dashboard.py`
