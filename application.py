from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>This is my first Web App!</h1> <h2> I am updating this from my mobile </h2> </body></html>\n"
