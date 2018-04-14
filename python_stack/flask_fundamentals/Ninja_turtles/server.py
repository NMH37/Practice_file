from flask import Flask,render_template,redirect,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def show_all_ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def handler_function(color):
    return render_template('show_ninja.html', color= color)
    


app.run(debug=True)