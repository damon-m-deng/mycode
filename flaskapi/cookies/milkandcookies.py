#!/usr/bin/env python3

## Object: export Flask APIs and interacting with cookies
## A cookie is to remember and track data pertaining to a client's usage for better visitor experience and site statistics
## A cookie is stored on a client's computer in the form of a text file

## A Request object contains a cookie’s attribute. It is a dictionary object of all the cookie variables and their corresponding values that a client has transmitted. In addition to that, a cookie also stores its expiry time, path, and domain name of the site.

# In Flask, cookies are set on response object. Use make_response() function to get response object from return value of a view function. After that, use the set_cookie() function of response object to store a cookie.

# Reading back a cookie is easy. The get() method of request.cookies attribute is used to read a cookie.

# On the client side, cookies are typically managed by browsers. However, in this lab, we're going to learn to use curl to interact with the cookies returned by APIs. Before you begin, you should read about how curl manages cookies: https://curl.haxx.se/docs/http-cookies.html

from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import url_for

app=Flask(__name__)

# entry point for users
@app.route('/')
@app.route('/login')
def index():
    return render_template('login.html')

# set the cookie and send it back to the user
@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    # if user generates a POST
    if request.method=='POST':
        if request.form.get('nm'): # if nm was assigned via the POST
            user=request.form.get('nm')
        else: # if user sents a POST without nm, the assign a default
            user='default_user'

        # Cookies are set on response objects
        # use make_response() to get response obj
        resp=make_response(render_template('readcookie.html'))
        # add a cookie to response obj
        resp.set_cookie('userID', user) # (cookieVar, value)

        # return response obj including the cookie
        return resp
    elif request.method=='GET':
        return redirect(url_for('index'))

# check users cookie for their name
@app.route('/getcookie')
def getcookie():
    # attempt to read the value of userID from user cookie
    name=request.cookies.get('userID')

    # return HTML embedded with name (value of userID read from cookie)
    return f'<h1>Welcome {name}</h1>'
if __name__=="__main__":
    app.run(host="0.0.0.0", port=2224)
