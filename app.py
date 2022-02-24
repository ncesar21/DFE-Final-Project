 from flask import Flask
app = Flask(__name__)
@app.route("/")



def home():
return '<h1> index page </h1>'
@app.route("/home")
def helloworld():
return '<h1> Hello Team</h1><title> <h1> Welcome to Fantasy Football </h1>'
