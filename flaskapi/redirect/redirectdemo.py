#!/usr/bin/python3
"""Alta3 Research
Simple flask application using redirect()"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort # raise an HTTPException for the given status code

app=Flask(__name__)

pic_location= "https://static.alta3.com/courses/api/lec_flaskcontrol_python/dont-panic.png"

# if user sends GET to / root
@app.route('/')
def index():
    # in ./templates/towel.html
    # <img src={{pic}} ...>
    # <form action="/login" method "POST">
    return render_template('towel.html',pic=pic_location)

# if user sends GET or POST to /login
@app.route('/login', methods=['POST','GET'])
def login():
    # POST
    if request.method=='POST':
        # towel.html
        # <form>
        #     <p><input type='text' name='answer'></p>
        if request.form.get('answer') == '42':
            return redirect(url_for('success')) # 302 to /success
        else:
            return redirect(url_for('fail')) # 302 to /fail

@app.route('/httpfail')
def httpfail():
    abort(406)

@app.route('/fail')
def fail():
    return "That was not a correct answer"

@app.route('/success')
def success():
    return "That was correct!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224)
