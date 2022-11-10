#!/usr/bin/env python3

import uuid # UUID generator

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

# range
for rand in range(howmany):
    print(uuid.uuid4()) 
