#!/usr/bin/env python3

import requests
import time
import hashlib
from pprint import pprint
import argparse

API='http://gateway.marvel.com/v1/public/characters'

def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest

def marvelcharcall(rand, keyhash, pubkey, lookmeup):
    resp=requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")

    if resp.status_code !=200:
        response=None
    else:
        response=resp.json()
    return response

def main():
    # get keys from local files
    # see ArgumentParser.add_argument('--dev') and args=parser.parse_args()
    with open(args.dev) as pkey:
        privkey=pkey.read().rstrip('\n')
    
    with open(args.pub) as pkey:
        pubkey=pkey.read().rstrip('\n')

    # create a random integer from a float timestamp
    rand=str(time.time()).rstrip('.')

    # build a hash with hashbuilder (timestamp, pub, priv key)
    keyhash=hashbuilder(rand, privkey, pubkey)

    result=marvelcharcall(rand, keyhash, pubkey, "Wolverine")

    pprint(result)

if __name__=='__main__':
    parser=argparse.ArgumentParser()

    # pass pub and priv keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')

    args=parser.parse_args()
    main()
