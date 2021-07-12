# flask_w2.py
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Hello World"
    
@app.route('/hello')
def hello_world():
   return "hello page"
   
@app.route('/user/<name>')
def get_user(name):
  return "The user is " + str(name)
  
@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
  return 'Hello ! ' + first_name + ' ' + last_name + '.'

if __name__ == '__main__':
    app.run(debug=True)
