"""
Exception Handling is a mechanism in Python that allows you to handle runtime errors gracefully, 
preventing crashes and ensuring smooth execution of a program. 
try:
    # Code that may cause an exception
except ExceptionType:
    # Code that handles the exception
else:
    # Code that runs if no exception occurs (optional)
finally:
    # Code that always runs, even if an exception occurs (optional)
"""
try:
    x = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#  Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))  # Raises ValueError if input is not an integer
    result = 10 / num  # Raises ZeroDivisionError if num is 0
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Catching Any Exception (Exception)
# Exception is a base class for all exceptions, so it catches any error.
try:
    x = int("abc")  # This raises ValueError
except Exception as e:
    print("An error occurred:", e)

# raise in Exception Handling
"""
The raise keyword in Python is used to manually trigger an exception. It allows you to create 
custom error messages and handle unexpected situations effectively.
Here, raise ValueError("message") forces Python to stop execution and display the error.
"""
x = -1
if x < 0:
    raise ValueError("Negative values are not allowed")

# raise can be used inside a try block to trigger an exception and handle it in the except block.
try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Only positive numbers allowed")  # Raise an exception
except ValueError as e:
    print(f"Exception caught: {e}")  # Handle the exception

# Custom exceptions
# Python allows you to define your own exception classes by inheriting from Exception.
class AgeTooSmallError(Exception):
    """Custom exception for age validation"""
    def __init__(self, message="Age must be 18 or above"):
        self.message = message
        super().__init__(self.message)

# Using the custom exception
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError()  # Raise custom exception
except AgeTooSmallError as e:
    print(f"Custom Exception: {e}")
