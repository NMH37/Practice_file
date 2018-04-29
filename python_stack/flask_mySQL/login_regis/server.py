from flask import Flask,render_template,redirect,session,redirect,request,flash
import re, md5
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key= "supersecret"
mysql = MySQLConnector(app,'login_reg') # need to make database !
EMAIL_REGEX=  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/process', methods=['POST'])
def process_info():
    if request.form['form']=='register1': # check hidden input value
        if not(len(request.form['first_name'])>1 and request.form['first_name'].isalpha()):
            flash('Enter Valid first name, all alphabetical and atleast 2 characters')
            return redirect('/')
        if not(len(request.form['last_name'])>1 and request.form['last_name'].isalpha()):
            flash('Enter Valid last name, all alphabetical and atleast 2 characters')
            return redirect('/')
        if not EMAIL_REGEX.match(request.form['email']):
            flash('invalid email')
            return redirect('/')
        if not(len(request.form['password'])> 7 and request.form['password'].isalnum):
            flash('Password must be atleast 8 characters long and include one non-alpha charachter !@#$%^(*&')
            return redirect('/')
        if not(request.form['password']== request.form['confirm_password']):
            flash(' Password confirmation not valid')
            return redirect('/')
        print request.form['first_name'] # now add user to db

        enc_pwd = md5.new(request.form['password']).hexdigest()
        print enc_pwd
        data = { 'fn' : request.form['first_name'],
                 'ln' : request.form['last_name'],
                 'em' : request.form['email'],
                 'pw' : enc_pwd
        }
        query = 'INSERT INTO login_reg.users (first_name,last_name,email,password,created_at,updated_at) VALUES (:fn,:ln,:em,:pw,NOW(),NOW())'
        mysql.query_db(query,data)
        print ' in data base'
        return redirect('/register')
    else: # log the user in after checking user in db
        enc_pwd = md5.new(request.form['password']).hexdigest()
        data  = {
            'em': request.form['email'],
            'pw': enc_pwd
        }
        query = 'SELECT * FROM login_reg.users WHERE email= :em AND password = :pw'
        result= mysql.query_db(query,data)
        session ['user_id']= result[0]['id']
        print session['user_id']

        return redirect('/login')


@app.route('/register')
def register_user():
    print 'registered'
    return render_template('/successful.html')

@app.route('/login')
def log_in():
    print " trying to login"
    return render_template('/successful.html')

app.run(debug=True)