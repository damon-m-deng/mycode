#!/usr/bin/env python3

import os
import urllib.request # used to make HTTP requests (GET, POST, PUT, DELETE)
import json

# Global constant (all caps)
API = "https://api.spacexdata.com/v3/dragons/dragon1"

def main():
    os.chdir("/home/student/mycode/json")

    # perform an HTTP GET request
    response=urllib.request.urlopen(API) # response is an HTTP response object
    # print(response) # <http.client.HTTPResponse object at 0x7fc5d46f3e50>
    # print(type(response)) # <class 'http.client.HTTPResponse'>

    # strip JSON off of the response
    ### THIS PART CAN BE REPLACED BY USING "requests"
    data=response.read() # read off all attached content
    encoding=response.info().get_content_charset('utf-8') # prep bytes decode
    space_data = json.loads(data.decode(encoding)) # loads() converts json string to python dict

    # print(space_data)
    print(type(space_data)) # dict
    print(space_data['id'])

if __name__=="__main__":
    main()
