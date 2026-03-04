import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from models import db, User, app

# 1. Key load karna
load_dotenv()
key = os.getenv('ENCRYPTION_KEY')
cipher_suite = Fernet(key.encode())

def encrypt_database_ips():
    with app.app_context():
        users = User.query.all()
        for user in users:
            if user.ip_address and not user.ip_address.startswith('gAAAA'): # Check agar pehle se encrypted toh nahi
                # Encrypt karna
                encrypted_ip = cipher_suite.encrypt(user.ip_address.encode())
                user.ip_address = encrypted_ip.decode()
        
        db.session.commit()
        print("Mubarak ho! Saare IP Addresses AES-256 se encrypt ho gaye hain.")

if __name__ == "__main__":
    encrypt_database_ips()