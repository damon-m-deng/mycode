#!/usr/bin/python3
"""Alta3 Research
Simple flask application using redirect()"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort 

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app=Flask(__name__)

pic_location= "https://static.alta3.com/courses/api/lec_flaskcontrol_python/dont-panic.png"

limiter=Limiter(
        app,
        key_func=get_remote_address,
        default_limits['200 per day','50 per hour']
        )

@app.route('/upload')
def upload():
    print(pic_location)
    return render_template('upload.html')

@app.route('/uploader', methods=['GET','POST'])
def upload_file():
    global pic_location
    if request.method=='GET':
        return render_template('upload.html')
    if request.method=='POST':
        f=request.files['file']
        filename=f.filename
        file_ext=filename.split('.')[-1]
        pic_location=f'static/newpic.{file_ext}'
        f.save('static/newpic.'+file_ext)
        return redirect('/')

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
