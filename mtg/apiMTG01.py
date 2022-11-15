#!/usr/bin/env python3

import requests

API="https://api.magicthegathering.io/v1/"

def main():
    resp=requests.get(API+"sets")
    # print(type(resp.json())) # dict
    # print(dir(resp))
    # print(resp.json().keys()) # dict_keys(['sets'])

    cardsets=resp.json().get('sets')
    # for cardset in cardsets:
        # print(cardset)
    
    # write cardsets into a file
    with open("mtgsets.index","w") as mtgfile:
        for cardset in cardsets:
            print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)

    setcode=input('What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ').lower()
    resp_short=requests.get(API+"cards?set="+setcode)
    cards=resp.json()

    print(cards)

if __name__ == "__main__":
    main()
