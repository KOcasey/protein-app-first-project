# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:28:53 2020

@author: casey
"""

from protein-app-first-project import basic_protein_information
import advanced_protein_information

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/advanced")
def advanced():
    return "Hello advanced World!"

if __name__ == "__main__":
    app.run()