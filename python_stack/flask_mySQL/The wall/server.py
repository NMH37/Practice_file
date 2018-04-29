from flask import Flask,render_template,redirect,session,redirect,request,flash
import re, md5
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key= "supersecret"
mysql = MySQLConnector(app,'wall') # need to make database !
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
        query = 'INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (:fn,:ln,:em,:pw,NOW(),NOW())'
        result = mysql.query_db(query,data)
        session ['user_id']= result
        print ' in data base', result
        return redirect('/register')
    else: # log the user in after checking user in db
        enc_pwd = md5.new(request.form['password']).hexdigest()
        data  = {
            'em': request.form['email'],
            'pw': enc_pwd
        }
        query = 'SELECT * FROM users WHERE email= :em AND password = :pw'
        result= mysql.query_db(query,data)

        if len(result) !=0:
            session ['user_id']= result[0]['id']
            print session['user_id']
            return redirect('/login')

        else:
            flash('Please register first')
            return redirect('/')
        
        

@app.route('/register')
def register_user():
    flash('registered')
    return redirect('/')

@app.route('/login')
def log_in():
    print " trying to login"
    return render_template('/wall.html')

@app.route('/post',methods=['POST'])
def post_on_wall ():
    print request.form['comment']
    data = { 
        'post':request.form['comment'],
        'users_id': session['user_id']
        }
    query = 'INSERT INTO messages (`content`,`users_id`,`created_at`,`updated_at`) VALUES (:post,:users_id,NOW(),NOW())'
    mysql.query_db(query,data)
    query = 'SELECT messages.content,users.first_name,messages.created_at,messages.id, messages.users_id FROM messages JOIN users ON users.id = messages.users_id'
    all_posts= mysql.query_db(query)
    query_cmt_show = 'SELECT comments.content, first_name,messages.id,comments.message_id FROM users JOIN messages ON messages.users_id= users.id JOIN comments ON messages.id = comments.message_id'
    comment = mysql.query_db(query_cmt_show)
    print comment
   
    return render_template('/wall.html',wall_posts= all_posts,cmt_on_msg= comment)


@app.route('/add_comment/<post_id>',methods=['POST'])
def find_msg_id(post_id):
    print post_id,session['user_id']
    data = { 'msg_id': post_id,
            'user_id': session['user_id'],
            'cmt': request.form['add_comment']
            }
    query_cmt_add = 'INSERT INTO comments (`content`,`created_at`,`updated_at`,`message_id`,`user_id`) VALUES (:cmt,NOW(),NOW(),:msg_id,:user_id)'
    mysql.query_db(query_cmt_add,data)
    
    
    return render_template('/wall.html')


@app.route('/logout')
def log_out_user():
    session.clear()
    return redirect('/')

app.run(debug=True)