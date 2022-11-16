#!/usr/bin/env python3

import requests

NASAAPI="https://api.nasa.gov/planetary/apod?"

def returncreds():
    # open credential files
    with open("./nasa.creds","r") as mycreds:
        nasacreds=mycreds.read()
    
    # remove the new line \n
    nasacreds="api_key="+nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds=returncreds()

    apod=requests.get(NASAAPI+nasacreds).json()

    # print(type(apod)) # dict

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__=="__main__":
    main()
