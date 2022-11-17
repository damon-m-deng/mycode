#!/usr/bin/env python3

# this is the server that hosts a flask app
# when client sends a POST request, server's endpoint returns a JSON

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import json

# make a flask App that runs 'this' python module
app=Flask(__name__)

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

# decorator: when client visits URL/, index() will be called
@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        data=request.json # if client makes a POST request, convert customer posted data to JSON
        if data: # if the converted JSON is not None
            data=json.loads(data) # converts JSON to python data structure
            name=data['name']
            realName = data["realName"]
            since = data["since"]
            powers = data["powers"]
            herodata.append({"name":name,"realName":realName,"since":since,"powers":powers}) # herodata is a list contains dict, add another dict entry from client input
    # jsonify return legal JSON
    return jsonify(herodata)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
