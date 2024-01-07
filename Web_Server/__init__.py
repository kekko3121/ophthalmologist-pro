import os
import atexit
from flask import Flask, render_template, redirect, request, url_for, jsonify, session, send_file
from Auth import Auth
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from dotenv import load_dotenv
from DB import DB
from User import User
import pdfkit
from io import BytesIO

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("KEY")

db = DB(os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("SERVICE"), os.getenv("IP"), os.getenv("PORT"))

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id, session.get('Role'))

#home page
@app.route('/')
def index():
    return render_template('index.html')

#signup page
@app.route('/signup')
def signup():
    #redirect link for create account
    return redirect("https://uniparthenope.esse3.cineca.it/AddressBook/ABStartProcessoRegAction.do", code = 302)

#login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('homepage'))
    
    elif request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')
        
        authentication = Auth("https://api.uniparthenope.it/UniparthenopeApp/v1/login", username, password)
        
        if authentication.connect():
            if db.is_Doctor(authentication.search("user", "codFis")):
                session['Role'] = "doctor"

            else:
                session['Role'] = "user"
            login_user(User(str(username), session.get('Role')), remember =  bool(remember.lower() == 'true'))
            session['user_data'] = authentication.getDate()
            session.permanent = bool(remember.lower() == 'true')
            return jsonify({'redirect': url_for('homepage')})

        else:
            return jsonify({'error': 'Invalid username or password'})

    return render_template('login.html', boolean = True)

#logout page
@app.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("login"))

#login home page
@app.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html')

@app.route('/account')
@login_required
def account():
    return render_template('MyAccount.html', authentication = session['user_data'])

@app.route('/myprescription')
@login_required
def myprescription():
    return render_template('MyPrescription.html', authentication = session['user_data'], prescription = db.searchPresciption(current_user.get_id()))

@app.route('/newprescription', methods = ['GET', 'POST'])
@login_required
def newprescription():
    if current_user.getRole() == 'doctor':
        if request.method == 'POST':
            data = request.form
            db.ins_patient(data)
            db.ins_prescription(data)
            db.conn_med(current_user.get_id())
            
            return redirect(url_for("newprescription"))
        
        return render_template('NewPrescription.html')
    else:
        return redirect(url_for("homepage"))

@app.route('/download/pdf/<int:prescription_id>')
@login_required
def downloadPdf(prescription_id):
    x = db.pdfDownload(prescription_id)
    html_content = render_template('pdfContent.html', x = x)
    return send_file(BytesIO(pdfkit.from_string(html_content, False)), mimetype='application/pdf', as_attachment=True, download_name = f"prescription_{x[1]}.pdf")

atexit.register(db.closeConn)

#settings server ip and port
#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port = 80)