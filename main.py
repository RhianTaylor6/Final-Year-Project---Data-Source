import flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os



app = flask.Flask(__name__, static_url_path='/web_contents/')
app.config['SECRET_KEY'] = '2f76c03428808188004157ebf4932088'
#app.config.from_object(os.environ['APP_SETTINGS'])

#DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="rhian" ,pw="P4n8c?!S",url="postgresql://localhost/",db="data_source_db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datasource.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db = SQLAlchemy(app)

class User(db.Model):
    
    f_name = db.Column(db.String(20), nullable = False)
    l_name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20), unique=True, nullable = False, primary_key = True)
    password = db.Column(db.String(20), nullable = False)
    company = db.Column(db.String(60), nullable = False)
    #last_login = db.column(db.DateTime, nullable = False, default = datetime.utcnow )

    def __init__(self, f_name, l_name, email, password, company):
        self.fname = f_name
        self.lname = l_name
        self.email = email
        self.password = password
        self.company = company

    def __repr__(self):
        #how the object is printed
        return f"User('{self.f_name} ', '{self.l_name} ', '{self.email} ', '{self.password} ', '{self.company} ')"
    
    def serialize(self):
        return {
            'f_name': self.f_name,
            'l_name': self.l_name,
            'email': self.email,
            'password':self.password,
            'company':self.company
        }


class os_drug_data(db.Model):
    Appl_No = db.Column(db.Integer, primary_key=True)
    Product_No = db.Column(db.Integer)
    Patent_No = db.Column(db.String)
    Submission_Date = db.Column(db.DateTime)
    Exclusivity_Code = db.Column(db.String)
    Exclusivity_Date = db.Column(db.DateTime)
    Trade_Name = db.Column(db.String)
    Ingredient = db.Column(db.String)
    Applicant = db.Column(db.String)
    Approval_Date = db.Column(db.DateTime)
    Type = db.Column(db.String)

    def __init__(self, Appl_No, Product_No, Patent_No, Submission_Date, Exclusivity_Code, Exclusivity_Date, Trade_Name,Ingredient,Applicant, Approval_Date, Type):
        self.Appl_No = Appl_No
        self.Product_No = Product_No
        self.Patent_No = Patent_No 
        self.Submission_Date = Submission_Date
        self.Exclusivity_Code = Exclusivity_Code
        self.Exclusivity_Date = Exclusivity_Date
        self.Trade_Name = Trade_Name
        self.Ingredient = Ingredient
        self.Applicant = Applicant
        self.Approval_Date = Approval_Date
        self.Type = Type

    def __repr__(self):
        #how the object is printed
        return f"User('{self.Appl_No} ', '{self.Product_No} ', '{self.Patent_No} ', '{self.Submission_Date} ', '{self.Exclusivity_Code}', '{self.Exclusivity_Date} ', '{self.Trade_Name} ', '{self.Ingredient} ', '{self.Applicant} ',  '{self.Approval_Date} ', '{self.Type} ')"
    
    def serialize(self):
        return {
            'Appl_No': self.Appl_No,
            'Product_No': self.Product_No, 
            'Patent_No': self.Patent_No,  
            'Submission_Date': self.Submission_Date ,
            'Exclusivity_Code': self.Exclusivity_Code,
            'Exclusivity_Date': self.Exclusivity_Date,
            'Trade_Name': self.Trade_Name, 
            'Ingredient': self.Ingredient,
            'Applicant': self.Applicant ,
            'Approval_Date': self.Approval_Date ,
            'Type': self.Type
            }

@app.route("/<path:path>")
def serve_webpage(path):
    return flask.send_from_directory('./web_contents/', path)


@app.route("/register", methods=["POST"])
def register_post():
    
    f_name = flask.request.form['f_name']
    l_name = flask.request.form['l_name']
    password = flask.request.form['password']
    c_password = flask.request.form['c-password']
    email = flask.request.form['email']
    company = flask.request.form['company']
    """
    f_name = flask.request.args.get('f_name')
    l_name = flask.request.args.get('l_name')
    password = flask.request.args.get('password')
    c_password = flask.request.args.get('c-password')
    email = flask.request.args.get('email')
    company = flask.request.args.get('company')
    """
    print(password)
    try:
        user=User(
            f_name = f_name,
            l_name = l_name,
            password = password,
            email = email,
            company = company
        )
        db.session.add(user)
        db.session.commit()
        return '{},{},{},{},{},{}'.format(f_name, l_name, password, c_password, email, company)
    except Exception as e:
        return(str(e))

@app.route("/login", methods=["POST", "GET"])
def login():

        email = flask.request.form['email-login']
        password = flask.request.form['password-login']          
        if(email == 'test@gmail.com' and password == 'test1'):
            return flask.redirect('welcome.html')
        else:
            flask.flash('Login Unsuccessful')
            return flask.redirect('failed-login.html')

@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')
        

app.run(debug=True, port=80)
