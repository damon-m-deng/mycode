#!/usr/bin/env python3

# using NASA NEOW (Near Earth Object Web) service

import requests

NEOURL="https://api.nasa.gov/neo/rest/v1/feed?"

def returncreds():
    with open("./nasa.creds","r") as mycreds:
        nasacreds=mycreds.read()
    # strip off new lines
    nasacreds = "api_key="+nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds=returncreds()

    startdate="start_date=2019-11-11"

    neow=requests.get(NEOURL+startdate+"&"+nasacreds).json()
    # print(type(neow)) # dict

    print(neow)

if __name__=="__main__":
    main()
