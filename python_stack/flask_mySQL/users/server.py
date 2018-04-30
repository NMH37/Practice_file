from flask import Flask,render_template,request,redirect,flash,session
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX=  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key='supersupersecret'
mysql = MySQLConnector(app,'emails_users')


@app.route('/')
def display_record():
    query = 'SELECT id,first_name,last_name,email,created_at FROM users'
    found = mysql.query_db(query)
    return render_template('index.html',email_found=found)
    

@app.route('/add_new_user')
def add_new():
    return render_template('/add_new_user.html')


@app.route('/add_email_record',methods=["POST"]) # add email
def add_email():
    if len(request.form['find_email']) < 1 :
        flash('email cannot be blank!')
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['find_email']):
        flash('invalid email')
        return redirect('/')

    else: #search data base!
        flash('email you entered is valid,Thank you')
        query ='INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (:fn,:ln,:email,NOW(),NOW())'
        data = {
            'fn':request.form['first_name'],
            'ln':request.form['last_name'],
            'email':request.form['find_email']
        }
        mysql.query_db(query,data)

        return redirect('/')       



@app.route('/delete_user/<id>')
def delete_user(id):
    data = {
        'id':id
    }
    query = 'DELETE FROM users WHERE id = :id'
    mysql.query_db(query,data)

    return redirect('/')

@app.route('/edit_user/<id>')
def edit_user(id):

    session['save_id']= id
   
    return render_template('/edit.html')

@app.route('/show_user/<id>')
def show_user(id):

    data = { 'id':id
    }
    query = 'SELECT * FROM users WHERE id = :id'
    info = mysql.query_db(query,data)
   
    return render_template('/display.html',user_info=info)

@app.route('/edit_saved_id',methods=['POST'])
def edit_saved_id():
    data= {
        'id' : session['save_id'],
        'fn' : request.form['first_name'],
        'ln' : request.form['last_name'],
        'email': request.form['new_email']
        
    }
    query = 'UPDATE users SET first_name= :fn, last_name = :ln, email = :email, updated_at = NOW() WHERE id = :id'
    mysql.query_db(query,data)
    
    
    return redirect("/")



app.run(debug="True")
