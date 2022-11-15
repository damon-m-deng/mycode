#!/usr/bin/env python3

import os
import json

os.chdir('/home/student/mycode/json')

with open("combined_ciscodata.json","r") as of:
    # moviedata=of.read() # str
    ### json.load(of) returns python data types read from an openfile(of)
    ciscodata=json.load(of)
# print(ciscodata)
# print(type(ciscodata)) # python dict
# print(ciscodata['device'])

cisco_dict=ciscodata
### json.dump(x, of) take python data types(x) and write legal JSON strings in an open file(of)
with open("cisco_json.json","w") as of:
    cisco_json=json.dump(cisco_dict, of)

### json.dumps(x) take python data types (x) and create a legal json string
cisco_json = json.dumps(cisco_dict)
print(type(cisco_json)) # str json string

### json.loads(x) take JSON strings(x) and create python data types
cisco_dict = json.loads(cisco_json)
print(type(cisco_dict)) # dict: python dictionary
