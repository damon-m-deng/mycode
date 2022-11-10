#!/usr/bin/env python3

## First module

print("This code will always execute")

def main():
    print(__name__) # __main__
    print("Module #1 Name=", __name__)

    print("This code belongs to the main function in module 1.")

# all files end with .py are called MODULES
# any files that ends with .py can be imported

if __name__ == "__main__":
    # main()
    print("Code is being run directly from PYTHON")
else:
    print("Code is being run IN-directly from IMPORT")
