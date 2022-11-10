#!/usr/bin/env python3

def main():
    # 'a' = 'append'
    # 'w' = 'write' -- will overwrite the previous content
    # using 'with': don't need close()
    with open('test', 'a') as file:
        file.write('blah, blah, blah...')
if __name__ == "__main__":
    main()
