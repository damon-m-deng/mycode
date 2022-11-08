#!/usr/bin/env python3
def main():
    proto = ["ssh","http","https"]
    protoa = ["ssh","http","https"]
    print(proto)
    
    # .append()
    proto.append("dns")
    protoa.append("dns")
    print(proto)

    proto2=[22,80,443,53]
    
    # .extend() iterative
    proto.extend(proto2)
    print("This is using .extend()")
    print(proto)
    protoa.append(proto2)
    print("This is using .append()")
    print(protoa) 
    
    # chain index protoa = ["ssh", "http", "https", "dns", [22, 80, 443, 53]]
    print(protoa[4][1]) # 80 ## if 80 is a string, you can chain one more [i] to get a char

    # .insert(i, x) insert item x before index i
    # .insert(0, x): insert at the font
    # .insert(len(list), x): same as append
    proto.insert(1, "rdp")
    print(proto)

    # .remove(x): remove the first item from the list whose value is equal to x
    # returns "ValueError" if not found
    proto.remove("rdp")
    print(proto)

    # :: and -1
    print(proto[-1]) # return the last item

    # list slicing [start:end:step]
    # [::2] from the start to the end, return every 2nd element
    # [::-1] return the whole list in the REVERSE order
    print(proto[::2])
    print(proto[::-1])
main()
