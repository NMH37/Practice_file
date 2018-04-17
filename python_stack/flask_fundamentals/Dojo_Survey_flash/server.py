from flask import Flask,render_template,request,redirect,session,flash
app = Flask(__name__)
app.secret_key="xndskt9cmvnjfhh"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process',methods =["POST"])
def process(): 
    if len(request.form["name"]) < 1:
        flash("Enter Valid Name")  
    return redirect('/')
    else:
        flash("Success, Welcome {}" .format(request.form["name"]))
    return redirect("/success")


@app.route('/success')
def process_form():
    session["name"]=request.form["name"]
    session["city"]=request.form["city"]
    session["fav_lang"]=request.form["fav_lang"]
    session["description"]=request.form["description"]
    return redirect('/display_info')


@app.route('/display_info')
def display():
    return render_template('display_info.html', name = session["name"], city= session["city"],fav_lang= session["fav_lang"],description= session["description"])
app.run(debug=True)