#!/usr/bin/env python3

## Second module

# create 2nd module and impor the first module
import first_module

# from first module:
# print(__name__) # first module

print("Module #2 Name=",__name__) # __main__

## __name__ is set to the name of the module being imported
## __name__ is set to __main__ on the module being run directly

# if __name__ == "__main__"
# this clause checks: Is this file being run directly, or is it being imported


## if__name__ == "__main__": main() was added on first module
# Module #1 Name=first module was NOT printed
# because when mod1 gets imported, mod1's __name__ will not be __main__, therefore main() from mod1 was NOT called

# if mod1's main needs to get called here in mod2
first_module.main()
