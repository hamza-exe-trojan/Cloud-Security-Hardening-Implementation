import json
from models import db, User, app

def load_data():
    # Flask app context use karna zaroori hai
    with app.app_context():
        try:
            # 1. JSON file ko kholna
            with open('MOCK_DATA.json', 'r') as f:
                users_list = json.load(f)
                
                for u in users_list:
                    # Duplicate entry check karna
                    if not User.query.filter_by(email=u['email']).first():
                        new_user = User(
                            first_name=u.get('first_name'),
                            last_name=u.get('last_name'),
                            email=u['email'],
                            gender=u.get('gender'),
                            ip_address=u.get('ip_address'),
                            password_hash="temporary_hash" 
                        )
                        db.session.add(new_user)
                
                # Sab save karna
                db.session.commit()
                print("Mubarak ho! Sara data database mein shift ho gaya hai.")
        except FileNotFoundError:
            print("Error: 'MOCK_DATA.json' file nahi mili. Check karein ke naam sahi hai?")
        except Exception as e:
            print(f"Kuch masla hua: {e}")

if __name__ == "__main__":
    load_data()
    