import os
from flask import Flask, redirect, url_for, session, request, render_template_string
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from models import db, User, app as flask_app

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

# OAuth Setup
oauth = OAuth(app)
azure = oauth.register(
    name='azure',
    client_id=os.getenv('AZURE_CLIENT_ID'),
    client_secret=os.getenv('AZURE_CLIENT_SECRET'),
    server_metadata_url=f"https://login.microsoftonline.com/{os.getenv('AZURE_TENANT_ID')}/v2.0/.well-known/openid-configuration",
    client_kwargs={'scope': 'openid email profile'}
)

@app.route('/')
def home():
    user = session.get('user')
    if user:
        return f"<h1>Mubarak ho Jani!</h1><p>Aap {user['name']} ke naam se login hain.</p><a href='/logout'>Logout</a>"
    return "<h1>Secure Auth System</h1><a href='/login'>Login with Microsoft</a>"

@app.route('/login')
def login():
    redirect_uri = os.getenv('AZURE_REDIRECT_URI')
    return azure.authorize_redirect(redirect_uri)

@app.route('/callback')
def callback():
    # Microsoft se token lena
    token = azure.authorize_access_token()
    user_info = token.get('userinfo')
    
    if user_info:
        session['user'] = user_info
        email = user_info.get('email')

        # Database check: Kya ye user pehle se mojood hai?
        with flask_app.app_context():
            existing_user = User.query.filter_by(email=email).first()
            
            if not existing_user:
                # Agar user naya hai, toh usay save karein
                new_user = User(
                    first_name=user_info.get('given_name', 'Azure'),
                    last_name=user_info.get('family_name', 'User'),
                    email=email,
                    password_hash="OAUTH_USER", # OAuth users ka password hum nahi rakhte
                    otp_secret=None # 2FA in ke liye optional rakh sakte hain
                )
                db.session.add(new_user)
                db.session.commit()
                print(f"✅ Naya user {email} database mein save ho gaya!")
            else:
                print(f"ℹ️ User {email} pehle se database mein mojood hai.")
            
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(port=5000, debug=True)