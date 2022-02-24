 from flask import Flask
app = Flask(__name__)
@app.route("/")



def home():
return '<h1> index page </h1>'
@app.route("/home")
def helloworld():
return '<h1> Hello world</h1><title> <h1> we are learning Flask </h1>'