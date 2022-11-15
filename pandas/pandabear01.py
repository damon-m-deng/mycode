#!/usr/bin/env python3

import pandas as pd

def main():
    # define the name of our xls file
    excel_file='./movies.xls'

    # create a DataFrame (DF) object
    # pd.read_excel(): read am excel file into a pandas DataFrame
    movies=pd.read_excel(excel_file)

    # show the 5 rows of DF
    print(movies.head())

    # choose the first column "Title" as index
    # index_col is None by default
    # index_col =0 means setting Title (from excel) as first column's name
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    
    # DF has 5 rows and 24 columns (indexed by title)
    # print the top 10 movies in the dataframe
    print(movies_sheet1.head())

    # export 5 movies from the top dataframe to excel
    movies_sheet1.head(5).to_excel("5movies.xlsx")
    # export 5 movies from the top of the dataframe to json
    movies_sheet1.head(5).to_json("5movies.json")
    # export 5 moives from the top of the dataframe to csv
    movies_sheet1.head(5).to_csv("5movies.csv")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
