from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/test-ext')
def hello_world():
    return render_template("test-ext.html") 
@app.route('/index')
def index():
    user = {'nickname':'Brian'}
    return render_template("index.html",
            title = 'home',
            user = user)

