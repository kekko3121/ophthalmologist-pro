from flask import Flask, render_template, redirect, request, url_for, jsonify
from Auth import Auth
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from DB import DB
from dotenv import load_dotenv
from User import User
import os

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("KEY")

#db = DB(os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("SERVICE"), os.getenv("IP"), os.getenv("PORT"))

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

#home page
@app.route('/')
def index():
    return render_template('index.html')

#login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('homepage'))
    
    elif request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        authentication = Auth("https://api.uniparthenope.it/UniparthenopeApp/v1/login", str(username), str(password))
        
        if authentication.connect():
            login_user(User(str(username)), remember = True)
            return jsonify({'redirect': url_for('homepage')})

    return render_template('login.html', boolean = True)

#signup page
@app.route('/signup')
def signup():
    #redirect link for create account
    return redirect(url_for("https://uniparthenope.esse3.cineca.it/AddressBook/ABStartProcessoRegAction.do"), code = 302)

#logout page
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

#login home page
@app.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html')

#settings server ip and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug = True)