#!/usr/bin/env python3

import requests

URL="http://ip.jsontest.com/"

def main():
    respjson=requests.get(URL).json()
    print(type(respjson)) # dict
    print(f"The current WAN IP is --> {respjson['ip']}")
if __name__ == "__main__":
    main()
