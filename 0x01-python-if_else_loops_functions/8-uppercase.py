#!/usr/bin/python3

lowerstart = 97
lowerend = 122
def to_upper(str):
     for i in str:
         if ord(i) >= lowerstart:
             if ord(i) <= lowerend:
                 cap = ord(i) - 32
                 print(chr(cap), end="")  
