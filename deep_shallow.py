"""
Feature	                        Shallow Copy	                                            Deep Copy
Definition	            Creates a new object but shares references to nested objects.	Creates a new object with completely independent nested objects.
Changes to Nested Objects	Affects the original object.	                            Does not affect the original object.
function                          uses copy() function                                        uses deepcopy() function
"""
# shallow copy and deep copy are ways to duplicate objects, but they handle the references to nested objects differently.
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

# Modify a nested object in the shallow copy
shallow_copied[0][0] = 99

print("Original:", original)          # Original is affected
print("Shallow Copy:", shallow_copied)


"""
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

# Modify a nested object in the deep copy
deep_copied[0][0] = 99

print("Original:", original)          # Original remains unchanged
print("Deep Copy:", deep_copied)

"""