# flask_helloworld.py
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Hello World"

app.run()