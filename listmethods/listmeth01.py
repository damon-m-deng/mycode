#!/usr/bin/env python3
proto = ["ssh","http","https"]
print(proto)
print(proto[0])

# <list>.extend(iterable)
# an iterable can be a string, set, tuple, etc
# .extend use case: combining 2 lists into a single list
proto.extend("dns") # .extend function will iterate and add d, n, s to the list
print(proto)
