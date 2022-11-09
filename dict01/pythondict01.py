#!/usr/bin/env python3

def main():
    switch = {
                "hostname": "sw1",
                "ip":"10.0.1.1",
                "version":"1.2",
                "vendor": "cisco"
            }
    print(switch)
    print(type(switch))

    # search value by providing key
    print(switch["hostname"]) # sw1
    print(switch["ip"])

    print(switch.keys())
    print(switch.values())

if __name__ == "__main__":
    main()
