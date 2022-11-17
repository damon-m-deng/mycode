#!/usr/bin/env python3

# A landing page rendered an HTML form asking a trivia question.
# The submitted answer was POSTed to another page
# If the answer was correct, the user was redirected to the "/correct" route
# If the answer was incorrect, the user was returned to the form to try again.

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for
import json

app=Flask(__name__)

# entry/landing page
@app.route('/')
def index():
    return render_template('trivia.html')

# correct page
@app.route('/correct')
def success():
    return render_template('correct_page.html')

# answer posting page
@app.route('/login', methods=['GET','POST'])
def guess():
    if request.method=='POST':
        if request.form.get('nm') and request.form.get('nm')=='42':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('index'))
            
if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
