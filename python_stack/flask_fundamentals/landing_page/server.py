from flask import Flask,render_template,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ninjas')
def ninjas_info():
    return render_template("ninjas.html")
@app.route('/dojo/new')
def new_ninja():
    return render_template("dojo/new.html")
app.run(debug= True)