#!/usr/bin/env python3

import urllib.request
import json

NASAAPI="https://api.nasa.gov/planetary/apod?"

def main():
    # open credential file
    with open("./nasa.creds","r") as mycreds:
        nasacreds=mycreds.read()
    
    # remove any extra new line /n on the credential key
    nasacreds="api_key="+nasacreds.strip("\n")

    # call the webservice with my key
    apodurlobj=urllib.request.urlopen(NASAAPI+nasacreds)
    # print(apodurlobj) # <http.client.HTTPResponse object at 0x7f136a2e3f40>
    
    # read the file-like obj
    apodread=apodurlobj.read()
    # print(apodread) # byte string: b'{...}
    
    # decode JSON to python data structure
    apod = json.loads(apodread.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(type(apod)) # dict

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

if __name__=="__main__":
    main()
