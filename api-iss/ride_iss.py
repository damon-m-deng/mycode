#!/usr/bin/env python3

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from API"""
    # call the api
    groundctl=urllib.request.urlopen(MAJORTOM)
    print(groundctl) # <http.client.HTTPResponse object at 0x7fe2b4094070>
    print(type(groundctl)) # <class 'http.client.HTTPResponse'>
    
    # get JSON from the API request, reads out as a JSON string
    helmet=groundctl.read()

    print(type(helmet)) # <class 'bytes'>
    # print(helmet) # b'{...}: byte string

    # decode using utf-8, then convert bytes to dict
    helmetson=json.loads(helmet.decode('utf-8'))
    print(type(helmetson)) # <class 'dict'>

    print(helmetson['number'])
    print(helmetson['people'][0])

    # display every item in a list
    for item in helmetson["people"]:
        print(item["name"])

if __name__ == "__main__":
    main()
