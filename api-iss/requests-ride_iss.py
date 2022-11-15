#!/usr/bin/env python3

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    # requests.get(API): get the HTTP obj, fetch the JSON string, then use .json() method to convert the JSON string to python dict
    helmet=requests.get(MAJORTOM).json()
    print(type(helmet)) # dict

    # print(helmet)
    # print(helmet["people"])
    for person in helmet['people']:
        print(person['name'])

if __name__=="__main__":
    main()
