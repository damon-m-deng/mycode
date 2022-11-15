#!/usr/bin/env python3

import os
import requests # used to make HTTP requests

# Global constant (all caps)
API = "https://api.spacexdata.com/v3/dragons/dragon1"

def main():
    os.chdir("/home/student/mycode/json")
    
    # perform an HTTP GET request
    response=requests.get(API) # response is an HTTP response obj
    print(response) # <Response [200]>
    print(response.status_code) # 200
    
    # get JSON from the response
    space_data=response.json() 
    # all "requests" obj have a .json() method
    # .json() method gets JSON and converts to python data type without import json

    print(space_data)
    print(type(space_data)) # dict
    print(space_data['id'])

if __name__=="__main__":
    main()
