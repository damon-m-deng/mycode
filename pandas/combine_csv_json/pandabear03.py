#!/usr/bin/env python3

import pandas as pd

def main():
    # read from a csv pd.read_csv()
    ciscocsv = pd.read_csv("./ciscodata.csv")
    # read from a json pd.read_json()
    ciscojson=pd.read_json("./ciscodata2.json")

    print(ciscocsv.head()) # display first 5 entries of csv
    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv, ciscojson],ignore_index=True)
    print(ciscodf)

if __name__=="__main__":
    main()
    
