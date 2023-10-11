#!/usr/bin/python3

# use range to count backwards

for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 == 0:
        cap = 0
    else:
        cap = 32
    print('{}'.format(chr(letter - cap)), end='')
