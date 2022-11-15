#!/usr/bin/env python3

import pandas as pd

def main():
    # create a DF: read from a csv pd.read_csv()
    ciscocsv = pd.read_csv("./ciscodata.csv")
    # read from a json pd.read_json()
    ciscojson=pd.read_json("./ciscodata2.json")

    print(ciscocsv.head()) # display first 5 entries of csv
    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv, ciscojson],ignore_index=True, sort=False)

    # export to json
    # NOT to include index numbers
    ciscodf.to_json("combined_ciscodata.json", orient="records")
    # export to excel
    ciscodf.to_excel("combined_ciscodata.xls", index=False)
    # export to csv
    ciscodf.to_csv("combined_ciscodata.csv", index=False)

    # create a python dict
    x=ciscodf.to_dict(orient='records')
    print(x)

if __name__=="__main__":
    main()
    
