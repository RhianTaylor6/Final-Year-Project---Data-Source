import flask

app = flask.Flask(__name__, static_url_path='/web_contents/')

app.secret_key = '2f76c03428808188004157ebf4932088'

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

    
    return '{},{},{},{},{},{}'.format(f_name, l_name, password, c_password, email, company)

@app.route("/login", methods=["POST", "GET"])
def login():

        email = flask.request.form['email-login']
        password = flask.request.form['password-login']          
        if(email == 'test@gmail.com' and password == 'test1'):
            return flask.redirect('welcome.html')
        else:
            flask.flash('Login Unsuccessful')
            return flask.redirect('failed-login.html')
        

app.run(debug=True, port=80)
