from flask import Flask,render_template,request,redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    # gather data from DB
    # display
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    print friends
    return render_template('index.html',All_friends=friends)
    
@app.route('/friends',methods=['POST'])
def add_friend():
    query = 'INSERT INTO friends(first_name, occupation,created_at,updated_at)VALUES(:first_name,:occupt,NOW(),NOW())'
    data = {
        'first_name': request.form['first_name'],
        'occupt': request.form['occupation']
    }
    mysql.query_db(query,data)
    return redirect('/')


app.run(debug=True)

