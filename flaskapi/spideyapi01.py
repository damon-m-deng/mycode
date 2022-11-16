#!/usr/bin/env python3

"""Return JSON from an endpoint in our Flask API. The client should be able to post JSON to our API as well"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app=Flask(__name__)

# list
herodata= [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
              ]
             }]

@app.route('/')
def index():
    # jsonify returns legal JSON
    return jsonify(herodata)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
