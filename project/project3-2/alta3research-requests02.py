#!/usr/bin/env python3

## CLIENT SIDE

import requests

def main():
    URL='http://0.0.0.0:2224/status'
    # send a GET request to your Flask API; it should target the endpoint that returns JSON.
    ### send a GET request to get the player's stats at URL/status
    resp=requests.get(URL).json()
    # take the returned JSON and "normalize" it into a format that is easy for users to understand.
    print(resp)

if __name__=="__main__":
    main()
