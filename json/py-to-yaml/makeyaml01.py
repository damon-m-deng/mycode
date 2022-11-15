#!/usr/bin/env python3

import yaml

def main():
    # py data structure
    hitchhikers = [
            {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
            {"name": "Arthur Dent", "species": "Human"}
            ]
    print(hitchhikers)

    # open a new file in write mode
    with open("galaxyguide.yaml","w") as zfile:
        # yaml.dump(input_data, file-like obj)
        # yaml.dump() creates YAML strings and write to files
        ## compare to JSON.dump(): creates a JSON string, and JSON.dumps() to write to file
        yaml.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
