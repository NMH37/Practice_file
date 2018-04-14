from flask import Flask,render_template,session,redirect


app = Flask(__name__)
app.secret_key = "sectretkey"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] +=1 
    return render_template('index.html')

@app.route('/button')
def button():
    if 'count'not in session:
        session['count'] = 0
    session['count'] +=1
    return redirect('/')
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)