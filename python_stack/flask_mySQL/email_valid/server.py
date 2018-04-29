from flask import Flask,render_template,request,redirect,flash,session
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX=  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key='supersupersecret'
mysql = MySQLConnector(app,'emails')


@app.route('/')
def index():
    return render_template('index.html')


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
        query ='INSERT INTO email_record (email,created_at,updated_at) VALUES (:email,NOW(),NOW())'
        data = {
            'email':request.form['find_email']
        }
        mysql.query_db(query,data)

        return redirect('/')       




@app.route('/display_record') # show all emails that are added
def display_record():
    query = 'SELECT id,email,created_at FROM email_record'
    found = mysql.query_db(query)

    return render_template('index.html',email_found=found) # send it view file



@app.route('/find_email_record',methods=["POST"]) # search for email in database
def find_email():
    if len(request.form['find_email']) < 1 :
        flash('email cannot be blank!')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['find_email']):
        flash('invalid email')
        return redirect('/')
    else: #search data base!
        flash('email you entered is valid,Thank you')
        query ='SELECT * FROM email_record WHERE email = :check_email'
        data = {
            "check_email":request.form['find_email']
        }
        found= mysql.query_db(query,data)
        return  render_template('index.html',email_found=found)  


@app.route('/delete_user/<id>')
def delete_user(id):
    data = {
        'id':id
    }
    query = 'DELETE FROM email_record WHERE id = :id'
    mysql.query_db(query,data)

    return redirect('/')

@app.route('/edit_user/<id>')
def edit_user(id):

    session['save_id']= id
   
    return render_template('/edit.html')



@app.route('/edit_saved_id',methods=['POST'])
def edit_saved_id():
    data= {
        'id' : session['save_id'],
        'email': request.form['new_email']
        
    }
    query = 'UPDATE email_record SET email = :email, updated_at = NOW() WHERE id = :id'
    mysql.query_db(query,data)
    
    
    return redirect("/")



app.run(debug="True")
