import flask

app = flask.Flask(__name__, static_url_path='/web_contents/')
@app.route("/<path:path>")
def serve_webpage(path):
    return flask.send_from_directory('./web_contents/', path)


@app.route("/register", methods=["POST"])
def register_post():
    username = flask.request.form['username']
    password = flask.request.form['password']
    c_password = flask.request.form['c-password']
    email = flask.request.form['email']
    company = flask.request.form['company']

    print(username + password + c_password + email + company)
    return '{},{},{},{}'.format(username, password, c_password, email, company)


app.run(debug=True, port=80)
