

import random
from flask import Flask,redirect,session,render_template,request
app = Flask(__name__)
app.secret_key="hello it is a secret"


@app.route('/')
def index():
    if 'my_number' not in session:
        session['my_number']= random.randrange(1,100)
        print session['my_number']
    return render_template('index.html')


@app.route('/process',methods=["POST"])
def process_it():
    session['user_guess'] = int(request.form["guess"])
    print session['user_guess']
    return render_template('guess.html')

@app.route('/try_again')
def try_again():
    return redirect('/')
@app.route('/new_game')
def new_game():
    session.clear()
    return redirect('/')
    
app.run(debug=True)