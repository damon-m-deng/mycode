#!/usr/bin/env python3

# pass variable via a URL path

from flask import Flask # import Flask class

app=Flask(__name__) # Flask class takes the current working module __name__ as the source of the application


# decorator .route('PATH')
# if you send a GET request to PATH, you will get a response of "Hello World!"
@app.route('/hello/<name>')

# when user gives a <name> on the url, name will be used as a variable for hello_world function
# Therefore, if user visits URL/hello/David, the user will see 'Hello David!'
def hello_world(name):
    return f"Hello {name}!"

if __name__=="__main__":
    # launch the application
    app.run(host="0.0.0.0", port=2224) # aux1 port used by this training env
