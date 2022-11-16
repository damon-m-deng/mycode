#!/usr/bin/env python3

"""passing a json string via URL (testing only)"""
# below URL takes a json string and return whether this is a valid json string
# URL? + json={JSON_string}

import requests
import json

URL="http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    mydata = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]} # python dict

    # use json lib to convert python data to legal json, then strip out whitespace
    # json.dumps(): converts python data to json string
    jsonToValidate=f"json={json.dumps(mydata).replace(' ','')}"
    print(jsonToValidate)
    # user request lib to send an HTTP GET
    respjson=requests.get(f"{URL}?{jsonToValidate}").json()
    
    print(type(respjson)) # dict
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")
if __name__ == "__main__":
    main()
