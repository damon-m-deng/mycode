#!/usr/bin/env python3

import crayons

print(crayons.red('Red string'))

print(f"{crayons.red('Red')} while {crayons.blue('blue')}")

crayons.disable() # disable the crayons package

print(f"{crayons.red('red')} white {crayons.blue('blue')}")

crayons.DISABLE_COLOR = False # enable the crayons package

print(f"{crayons.red('red')} white {crayons.blue('blue')}")

# print 'red string' in red
print(crayons.red('red string', bold=True))

# print 'yellow string' in yellow
print(crayons.yellow('yellow string', bold=True))

# print 'magenta string' in magenta
print(crayons.magenta('magenta string', bold=True))

# print 'white string' in white
print(crayons.white('white string', bold=True))
