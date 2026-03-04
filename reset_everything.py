import os
import json
import shutil
from models import db, User, app

def nuke_and_rebuild():
    with app.app_context():
        # 1. Purani Database ka khatma
        db_path = os.path.join(app.instance_path, 'users.db')
        if os.path.exists(db_path):
            os.remove(db_path)
            print("--- Purani 'users.db' delete ho gayi hai. ---")

        # 2. Nayi Table banana (naye columns ke sath)
        db.create_all()
        print("--- Nayi Table 'otp_secret' column ke sath ban gayi hai. ---")

        # 3. MOCK_DATA se data dobara load karna
        try:
            with open('MOCK_DATA.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    new_user = User(
                        first_name=item.get('first_name'),
                        last_name=item.get('last_name'),
                        email=item['email'],
                        gender=item.get('gender'),
                        ip_address=item.get('ip_address'),
                        password_hash="temporary_hash"
                    )
                    db.session.add(new_user)
                db.session.commit()
                print(f"--- Mubarak ho! {len(data)} users ka data load ho gaya hai. ---")
        except Exception as e:
            print(f"Data load karne mein masla hua: {e}")

if __name__ == "__main__":
    nuke_and_rebuild()