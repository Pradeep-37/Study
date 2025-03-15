# No, a dictionary cannot have duplicate keys. If you try to insert a duplicate key, the latest value 
# will overwrite the previous one.
dic = {'a': 1, 'b': 2, 'a': 3}  # Duplicate key 'a'
print(dic)  

"""
1, True, and 1.0 all have the same hash value in Python, so they are treated as the same key.
The last assigned value ('c') overwrites the previous values. 
"""
dic = {}
dic[1] = 'a'
dic[True] = 'b'
dic[1.0] = 'c'
print(dic)

# difference between is and == in Python
# == → Checks if values are equal.
# is → Checks if objects have the same memory address (identity check).
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (Values are the same)
print(a is b)  # False (Different objects in memory)

#The finally block always executes, even if there is a return in try.
# Since finally has a return 2, it overrides the return 1 from try.
def tricky():
    try:
        return 1
    finally:
        return 2
print(tricky())

#Falsy values in Python
print(bool([]), bool({}), bool(set()), bool(0), bool(""), bool(None))
# Any non-empty value is True.

a = "abcdef"
print(a[::-1])  # ?
print(a[-2:-5:-1])  # ?
print(a[::2])  # ?

#a = b → a = 10     b = a + b → b = 5 + 10 = 15
# Python evaluates everything on the right side first before assigning.
a = 5
b = 10
a, b = b, a + b
print(a, b)

# strings are immutable and cannot modify them directly
x = "Python"
x[0] = "J"
print(x)

