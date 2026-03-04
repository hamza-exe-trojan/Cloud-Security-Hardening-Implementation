from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Ye line database file ka rasta batati hai
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Table ka structure (Blueprint)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(20))
    ip_address = db.Column(db.String(50)) # Phase 2 mein hum isay encrypt karenge
    password_hash = db.Column(db.String(200)) # Security ke liye hashing
    otp_secret = db.Column(db.String(32))

# Database create karne ka function
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Mubarak ho Jani! 'users.db' file aur 'User' table ban chuki hai.")