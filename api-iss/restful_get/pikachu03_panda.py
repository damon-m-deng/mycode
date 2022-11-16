#!/usr/bin/env python3

"""allows a user to pass in a word to search. count the number of time that word appears, print total word list, export everything to JSON format"""

# for accepting args from the cmd line
import argparse
import requests
import pandas

ITEMURL="http://pokeapi.co/api/v2/item"

def main():
    items=requests.get(ITEMURL+"?limit=1000").json()

    matchedwords=[]

    for item in items["results"]:
        if args.searchword in item['name']:
            matchedwords.append(item['name'])

    finishedlist=matchedwords.copy()

    # convert matchedwords into a dict
    matchedwords={}
    # create a key of 'matched' with value of the matched list
    matchedwords['matched']=finishedlist

    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    # export to json using pandas
    # make a DF from the dict
    itemsdf=pandas.DataFrame(matchedwords)
    itemsdf.to_json('pokemonitems.json')

    print('Gotta collect \'em all!')

if __name__=="__main__":
    # argparse.ArgumentParser: creates a new ArgumentParser object
    parser=argparse.ArgumentParser(description="Pass in a word to search the Pokemon item API")
    # ArgumentParser.parser.add_argument
    parser.add_argument('--searchword', metavar="SEARCHW", type=str, default='ball', help="pass in any word, default is 'ball'")
    args=parser.parse_args()
    main()

## in command line: use $ python3 pikachu03_panda.py --searchword heal
