#!/usr/bin/python3

def fizzbuzz():
    # using the modulo operator
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 != 0:
            print("Fizz ", end="")
        elif num % 5 == 0 and num % 3 != 0:
            print("Buzz ", end="")
        elif num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz ", end="")
        else:
            print(num, end=" ")
    print()
