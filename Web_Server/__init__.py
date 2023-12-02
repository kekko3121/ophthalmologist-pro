from flask import Flask, render_template, redirect, request, url_for, jsonify
from Auth import Auth
from flask_login import login_user, login_required, logout_user, current_user

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
        user = Auth("https://api.uniparthenope.it/UniparthenopeApp/v1/login", str(username), str(password))
        #if(user.connect() == 200):
    
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
    return redirect("/login")

#settings server ip and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug = True)