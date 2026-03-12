# List, Functions & Modules
# List superpowers
# --------------------------

# numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# print(len(numbers))
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sorted(numbers))


# List slicing
# ---------------

# fruits = ["apple", "banana", "mango", "orange", "grape"]
# print(fruits[0:3]) # from index 0,1,2
# print(fruits[2:]) # from index 2 to end
# print(fruits[:3]) # from index 0,1,2
# print(fruits[-1]) # last item
# print(fruits[-2:]) # last two items

# List comprehension
# -------------------

# Long way

# numbers = [1, 2, 3, 4, 5]
# doubled = []
# for num in numbers:
#     doubled.append(num*2)
#     print(doubled)

# The Python way
# -----------------

# numbers = [1,2,3,4,5]
# doubled = [num * 2 for num in numbers]
# print(doubled)

# Filtering inside
# ---------------------

# numbers = [1,2,3,4,5]
# doubled_evens = [num * 2 for num in numbers if num % 2 == 0]
# print(doubled_evens)

# Functions — Going Deeper
# Multiple return values — PHP can't do this natively:
# -----------------------------------------------------

# def get_min_max(numbers):
#   return min(numbers), max(numbers)

# lowest, highest = get_min_max([3,1,4,1,5,9])
# print(lowest)
# print(highest)

# *args — accept any number of arguments:
# ----------------------------------------

# def add_all(*numbers):
#     return sum(numbers)


# print(add_all(1, 2, 3))
# print(add_all(1, 2, 3, 4, 5))

# **kwargs — accept any number of named arguments:

# def show_info(**details):
#     for key, value in details.items():
#        print(f"{key}: {value}")


# show_info(name="Nick", city="Nairobi", role="Developer")


# Modules — Python's use / require
# ----------------------------------

# import math
# import random
# import datetime

# print(math.sqrt(16))
# print(math.pi)
# print(random.randint(1,10))
# print(datetime.date.today())

# You can also import specific things:

# from math import sqrt, pi
# from random import randint, choice

# print(sqrt(25))
# print(randint(1,100))
# print(choice(["apple", "banana", "mango"]))
