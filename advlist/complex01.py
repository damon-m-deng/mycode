#!/usr/bin/env python3

def main():
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
    print(list1)
    print(list1[1]) # arista_eos

    list2 = ["juniper"]
    list1.extend(list2)
    print(list1) # ['cisco_nxos', 'arista_eos', 'cisco_ios', 'juniper']
    
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    list1.append(list3)
    print(list1) # ['cisco_nxos', 'arista_eos', 'cisco_ios', 'juniper', ['10.1.0.1', '10.2.0.1', '10.3.0.1']]
    
    # return the list of the IP addresses from list1
    print(list1[4])

    # chain indexing
    print(list1[4][1]) # 10.2.0.1
    print(list1[4][1][3]) # 2
main()

