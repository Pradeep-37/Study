"""
In Python, *args and **kwargs are special syntax used in function definitions to pass a variable 
number of arguments to a function. 
They are useful when the number of arguments to a function is uncertain. lk
"""
# they need not to be args or kw args they can be any name
"""
*args
Purpose: Allows you to pass a variable number of non-keyworded arguments to a function.
How it works:
Collects all positional arguments passed to the function into a tuple.
"""
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))       # Output: 6
print(add_numbers(10, 20, 30, 40)) # Output: 100

# Iterating Over *args
def greet_people(*args):
    for name in args:
        print(f"Hello, {name}!")

greet_people("Alice", "Bob", "Charlie")

"""
**kwargs
Purpose: Allows you to pass a variable number of keyworded arguments (key-value pairs) to a function.
How it works:
Collects all keyword arguments passed to the function into a dictionary.
"""
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, city="New York")

# Combining *args and **kwargs
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Alice", age=30)
