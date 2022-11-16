#!/usr/bin/env python3

from flask import Flask # import Flask class

app=Flask(__name__) # Flask class takes the current working module __name__ as the source of the application


# decorator .route('PATH')
# if you send a GET request to PATH, you will get a response of "Hello World!"
@app.route('/hello')

def hello_world():
    return "Hello World!"

# Flask.add_url_rule()
# equivalent to @app.route()
# anybody going to the url '/hello' will call hello_world() function
# the middle "hello" is a nickname of this URL rule
# app.add_url_rule("/hello", "hello", hello_world)

if __name__=="__main__":
    # launch the application
    app.run(host="0.0.0.0", port=2224) # aux1 port used by this training env
