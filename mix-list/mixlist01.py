#!/usr/bin/env python3

my_list = ["192.168.0.5", 5060, "UP"]

print(f"The first item in the list (IP): {my_list[0]}")
print(f"The second item in the list (port): {my_list[1]}")
print(f"The last item in the list (state): {my_list[2]}")

iplist = [5060, "80", 55,"10.0.0.1", "10.20.30.1", "ssh"]

# return IP addresses only
print(f"IP addresses are {iplist[3]}, and {iplist[4]}")
print("IP addresses are", iplist[3], ", and", iplist[4])
print("IP addresses are "+iplist[3]+", and "+iplist[4])
