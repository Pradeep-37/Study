# Decorators in Python are functions that modify the behavior of other functions or methods without 
# changing their code.
# Implemented using @decorator_name syntax.

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator  # Applying decorator
def say_hello():
    print("Hello, World!")

say_hello()

# Multiple Decorators  You can stack multiple decorators on a function.

def decor1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decor1
@decor2
def greet():
    print("Hello!")

greet()
