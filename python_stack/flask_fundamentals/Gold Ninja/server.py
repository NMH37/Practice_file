from flask import Flask,session,render_template,redirect
app= Flask(__name__)
app.secret_key="wfjhgh w bchgyghfh"

@app.route('/')
def index():
    return render_template('index.html')
