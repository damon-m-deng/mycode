#!/usr/bin/env python3

import pandas as pd

pet1={"name":"Misty","age":12,"species":"cat"}
pet2={"name":"Peach","age":1,"species":"cat"}
pet3={"name":"Pepper","age":5,"species":"cat"}
pet4={"name":"Bones","age":8,"species":"dog"}
pet5={"name":"Bernie","age":3,"species":"hamster"}
pet6={"name":"Greg","species":"fish"}

pets_df=pd.DataFrame([pet1,pet2,pet3,pet4,pet5,pet6])

# print(pets_df) # print all?
# print(pets_df.tail()) # .tail() last 5
# print(pets_df.info()) # more info: class type, range index, check for missing value, etc
print(pets_df.shape) # tuple (6,3) .shape shows dimension: 6 rows, 3 columns
