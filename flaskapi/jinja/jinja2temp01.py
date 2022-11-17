#!/usr/bin/env python3

## Jinja is a template engine ./templates
## able to populate templates with data and use programming logic to make static documents (HTML) render dynamically

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/<username>')
def index(username):
    # {{ name }} defined in html
    return render_template("hellobasic.html", name=username)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224)
