#!/usr/bin/env python3

import requests

API="http://api.open-notify.org/iss-now.json"

def main():
    # fetch data from the API and convert it to a python dict
    resp = requests.get(API)

if __name__=="__main__":
    main()
