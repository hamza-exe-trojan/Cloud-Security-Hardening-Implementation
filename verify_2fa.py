import pyotp
from models import User, app

def verify_code(email):
    with app.app_context():
        # 1. Database se user ka secret uthana
        user = User.query.filter_by(email=email).first()
        
        if user and user.otp_secret:
            # 2. TOTP object banana secret key use karte hue
            totp = pyotp.TOTP(user.otp_secret)
            
            # 3. User se mobile wala code mangna
            print(f"\n--- 2FA Verification for {user.first_name} ---")
            input_code = input("Google Authenticator se 6-digit code enter karein: ")
            
            # 4. Verify karna
            if totp.verify(input_code):
                print("\n✅ Mubarak ho! Code sahi hai. Access Granted!")
            else:
                print("\n❌ Access Denied! Code ghalat hai ya expire ho chuka hai.")
        else:
            print("User nahi mila ya 2FA setup nahi hua!")

if __name__ == "__main__":
    # Wahi email likhein jis ka QR code banaya tha
    verify_code("icloney3@independent.co.uk")