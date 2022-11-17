#!/usr/bin/env python3

# ?QueryParameter

## What is this script trying to do?
## There is a template .j2 with placeholders(variables)
## When client makes a GET request with ?queryParam
#### This py script will 
#### 1. Grab the variables needed for the template from client's queryparameter
#### 2. Return the switch config data in the same format as the template#### 3. If there are no data provided from client's qparms, use default values defined in this script

## Test:
## 1. renders a template with default values
## $ curl "http://0.0.0.0:2224/ciscoios -L

## 2. renders a template with client's input values
## $ curl "http://0.0.0.0:2224/ciscoios/?switchname=hal9000&username=dreadpirateroberts&ip=192.168.0.1&mtu=1450&gateway=172.0.0.1" -L


from flask import Flask
from flask import request

# flask request: works with the data that the CLIENT has sent to our app/server
# use case: 
## To grab CLIENT's data from forms (request.form)
## To grab CLIENT's data from input query parameter arguments (request.args)
## To grab CLIENT's request type (request.method) GET/POST/PUT, etc


from flask import render_template

app=Flask(__name__)

@app.route('/ciscoios/')
def ciscoios():
    try:
        qparms={}
        # In the URL, client passes(after ?) switchname=USER_INPUT or default 'bootstrap switch'
        qparms['switchname']=request.args.get('switchname', 'bootstrapped switch')
        # user passes username= or default "admin"
        qparms["username"]  = request.args.get("username", "admin")
        # user passes gateway= or default "0.0.0.0"
        qparms["defaultgateway"] = request.args.get("gateway", "0.0.0.0")
        # user passes ip= or default "0.0.0.0"
        qparms["switchIP"] = request.args.get("ip", "0.0.0.0")
        # user passes mask= or default "255.255.255.0"
        qparms["netmask"] = request.args.get("mask", "255.255.255.0")
        # user passes mtu= or default "1450"
        qparms["mtusize"] = request.args.get("mtu", "1450")

        # render template and save as baseIOS.conf
        # **: take all the keys in qparms dict ('defaultgateway', 'switchIP'), treat the keys like variables, get the values (given by the client) and pass the values to 'baseIOS.conf.j2' template
        return render_template('baseIOS.conf.j2', **qparms)
    except Exception as err:
        return f"Uh-oh! {err}"
if __name__=="__main__":
    app.run(host='0.0.0.0', port=2224)
