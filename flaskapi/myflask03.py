#!/usr/bin/env python3

from flask import Flask, redirect, url_for

# $ curl localhost:2224/user/admin -L

app=Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty}"

@app.route("/user/<name>")
def hello_user(name):
    if name == 'admin':
        # return a 302 response to redirect to /admin
        # Option 1: redirect(URL) -- hardcode
        # return redirect('/admin')
        # Option 2: url_for(function): redirect to the URL of this function
        return redirect(url_for('hello_admin'))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for('hello_guest',guesty=name))

if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
