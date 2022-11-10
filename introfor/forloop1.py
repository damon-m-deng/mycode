#!/usr/bin/env python3

vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
approved_vendors = ["cisco", "juniper", "big_ip"]

for vendor in vendors:
    print("The vendor is:"+vendor, end=" ")
    if vendor not in approved_vendors:
        print(" - not an approved vendor", end="")
print("Loop ends")
