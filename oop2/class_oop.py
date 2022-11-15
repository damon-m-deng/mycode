#!/usr/bin/env python3

class Cat:
    # ctor with attributes
    def __init__(self, name):
        self.name = name
    
    # class methods
    def speak(self):
        return 'Meow'

mycat = Cat("Bella")
print(mycat) # <__main__.Cat object at 0x7f7f7de4c1c0>
print(mycat.name) # Bella
print(type(mycat)) # <class '__main__.Cat'>
print(dir(mycat)) # will include class attribute and class methods
print(mycat.speak()) # Meow
