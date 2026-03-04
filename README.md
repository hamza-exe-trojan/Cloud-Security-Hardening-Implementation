# 🛡️ SecureAuth: Enterprise-Grade Authentication System

Developed by **Ameer Hamza Khan (Jani)** *BSCS Student at Virtual University of Pakistan | Aspiring SOC Analyst*

This project implements a multi-layered security approach to protect user identity and data, focusing on **Identity & Access Management (IAM)**.

## 🚀 Key Security Features
* **AES-256 Encryption:** Encrypts sensitive metadata like IP addresses to ensure data-at-rest security.
* **TOTP Multi-Factor Authentication:** Integrated 2FA using Google Authenticator for an added layer of defense.
* **Microsoft Azure OAuth 2.0:** Secure third-party login via Azure Entra ID for enterprise-level authentication.
* **Secure Database Management:** Using SQLAlchemy with hashed passwords and encrypted session handling.



## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Database:** SQLite (SQLAlchemy)
- **Identity Provider:** Microsoft Azure (Entra ID)
- **Encryption:** Cryptography (Fernet)

## 📋 How to Run
1. Clone the repo: `git clone https://github.com/YourUsername/SecureAuth-Project.git`
2. Install libraries: `pip install -r requirements.txt`
3. Setup `.env` with your Azure credentials.
4. Run the app: `python app.py`