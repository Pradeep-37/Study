""" 
A lambda function in Python is a small, anonymous function that is defined using the lambda keyword. 
Lambda functions can have any number of arguments but only one expression. 
They are often used for short, simple functions where a full function definition is unnecessary.
"""
# lambda arguments: expression

square = lambda x: x * x
print(square(5))  # Output: 25

add = lambda x, y: x + y  # with multiple arguments
print(add(3, 5))  # Output: 8

#Lambda Function Inside Another Function
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15

#Use cases
# Can be used for sorting, map(), filter(),reduce()
# Sorting with sorted()
names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # Output: ['Bob', 'Alice', 'David', 'Charlie']

#  Mapping with map()
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

# Filtering with filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# Reducing with functools.reduce()      Use lambda functions to perform cumulative operations.
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24



