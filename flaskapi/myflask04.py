#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

# by default, Flask route responds the GET request
# POST method in URL routing
# create a HTML form and use POST method to send form data to a URL

# curl http://0.0.0.0:2224/login -L -d nm=Conan%20the%20Librarian

app=Flask(__name__)

# this is where we want to redirect users to
@app.route('/success/<name>')
def success(name):
    return f"Welcome {name}!\n"

# this is a landing point for users (a start) '/' or '/start'
@app.route('/') 
@app.route('/start')
def start():
    # render_template(file) renders the HTML template
    return render_template('postmaker.html') # looks for templates.postmaker.html

    ## ./template/postmaker.html has a form
    # <form action="/login" method'"POST">
    # <p><input type = "text" name = "nm"></p>
    # when the user input a value and click 'submit', it will trigger a POST request, assign the user input to 'nm', and go to '/login'

# this is where postmaker.html POSTs data to
# a user could also browser GET to this location

## by default: all routes accept GET request
@app.route('/login', methods=["POST","GET"])
def login():
    # request.method reads the client's method
    if request.method=='POST': # triggered by the form from the HTML
        if request.form.get('nm'): # if the POST request from the form has a value for nm
            user=request.form.get('nm') # user=chewbacca
        else: # no value provided by the user
            user='defaultuser'
    return redirect(url_for("success", name=user)) # url_for('function', arg=var)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
