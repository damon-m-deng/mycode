#!/usr/bin/env python3

import json

def main():
    hitchhikers = [
            {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
            {"name": "Arthur Dent", "species": "Human"}
                ]

    print(hitchhikers)

    with open("galaxyguide.json","w") as zfile:
        # json.dump(python_data, file like obj) returns a json string
        json.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
