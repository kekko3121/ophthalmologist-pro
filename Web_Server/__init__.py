from flask import Flask, render_template, redirect

app = Flask(__name__)

#home page
@app.route('/')
def index():
    return render_template('index.html')

#login page
@app.route('/login')
def login():
    return render_template('login.html')

#signup page
@app.route('/signup')
def signup():
    #redirect link for create account
    return redirect("https://uniparthenope.esse3.cineca.it/AddressBook/ABStartProcessoRegAction.do", code = 302)

#settings server ip and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug = True)