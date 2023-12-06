from flask import Flask, render_template, redirect, request, url_for, jsonify
from Auth import Auth
from flask_login import login_user, login_required, logout_user, current_user
from DB import DB
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_service = os.getenv("SERVICE")
db_ip = os.getenv("IP")
db_port = os.getenv("PORT")

app = Flask(__name__)

#home page
@app.route('/')
def index():
    return render_template('index.html')

#login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        authentication = Auth("https://api.uniparthenope.it/UniparthenopeApp/v1/login", str(username), str(password))
        db = DB(os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("SERVICE"), os.getenv("IP"), os.getenv("PORT"))
        if(authentication.connect() and db.seekMed(authentication.search("user", "codFis"))):
           return jsonify({'redirect': '/doctor'})
        elif(authentication.connect()):
            return jsonify({'redirect': '/login'})
    
    return render_template('login.html', boolean = True)

#signup page
@app.route('/signup')
def signup():
    #redirect link for create account
    return redirect("https://uniparthenope.esse3.cineca.it/AddressBook/ABStartProcessoRegAction.do", code = 302)

#logout page
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/doctor')
@login_required
def doctor():
    return render_template('Doctorpage.html')

#settings server ip and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug = True)