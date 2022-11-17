#!/usr/bin/env python3

# at least two endpoints
# at least one of your endpoints should return JSON
# has ONE additional feature from the following list:
### one endpoint returns HTML that uses jinja2 logic
### requires a session value be present in order to get a response
### writes to/reads from a cookie
### reads from/writes to a sqlite3 database

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import json


app=Flask(__name__)

herodata= {
    "name": "Hero",
    "HP": 100,
    "MP": 100,
    "actions": [
        "go",
        "get"
              ]
            }

# landing page
@app.route('/')
def index():
    return render_template('index.html')

# returns a JSON with client calls a GET
@app.route('/status')
def check_status():
    return json.dumps(herodata)

# "Say hi" page
# use Jinja to call hero's name {{hero_name}} in an HTML
@app.route('/<name>', methods=['GET','POST'])
def say_hi(name):
    if request.method=='POST':
        if request.form.get('nm')=="hero":
            return render_template('say_hi.html', hero_name=name)
        else:
            return render_template('say_hi.html', hero_name='Heroine')
    else: # if client makes a GET request, redirect to index
        return redirect(url_for('index'))

if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
