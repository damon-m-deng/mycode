#!/usr/bin/env python3

import requests

API="http://api.open-notify.org/astros.json"

def main():
    dict_data=requests.get(API).json()
    print("People in space:",dict_data['number'])

    for person in dict_data['people']:
        print(f"{person['name']} on the {person['craft']}")
if __name__=="__main__":
    main()
