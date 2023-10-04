#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = number % 10 if number >= 0 else -number % 10
print(f"Last digit of {number} is {new_number} and ", end="")
if new_number > 5:
    print("is greater than 5")
elif new_number < 6 and new_number != 0:
    print("is less than 6 and not equal to 0")
elif new_number == 0:
    print("is 0")
