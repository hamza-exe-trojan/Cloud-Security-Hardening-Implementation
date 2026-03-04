import pyotp
import qrcode
from models import db, User, app

def generate_2fa(email):
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            # 1. Aik unique secret key banana
            secret = pyotp.random_base32()
            user.otp_secret = secret
            db.session.commit()

            # 2. QR code ka link banana
            uri = pyotp.totp.TOTP(secret).provisioning_uri(
                name=user.email, 
                issuer_name="JaniSecureApp"
            )
            
            # 3. QR Code image save karna
            img = qrcode.make(uri)
            img.save(f"{user.first_name}_auth_qr.png")
            
            print(f"Mubarak ho! {user.first_name} ka QR code ban gaya hai.")
            print(f"Ab folder mein '{user.first_name}_auth_qr.png' check karein.")
        else:
            print("User nahi mila, email sahi se check karein!")

if __name__ == "__main__":
    # Database se koi bhi email yahan likhein test karne ke liye
    generate_2fa("icloney3@independent.co.uk")