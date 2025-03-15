""" 
File handling in Python allows us to read, write, and manipulate files stored on the disk. 
Python provides built-in functions like open(), read(), write(), and close() to handle file operations.
"""
file = open("example.txt", "r")  # Opens the file in read mode

#reading
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Prints the entire file
    
# readline() vs readlines()
with open("example.txt", "r") as file:
    line1 = file.readline()  # Reads the first line
    line2 = file.readline()  # Reads the second line

print(line1)  
print(line2)
#Reads only one line at a time.Useful when processing large files.

with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)
# Reads all lines at once and returns them as a list.Can cause memory issues for large files.

#writing
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")


# 🔥 1. truncate(size)
# It resizes the file to the specified size (in bytes).
# If the size is smaller than the current file size, the file is truncated (cut short).
# If the size is larger, the file is extended — and the extra space might be filled with null bytes (\x00).
# If no size is given, it truncates the file at the current position of the file pointer.
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
    file.truncate(5)  # Keeps only "Hello"

# Before truncation: Hello, World!
# After truncation: Hello

"""⚡ 2. flush()
It forces the buffer to write its content to the file immediately.
Normally, when you write to a file, Python uses buffering — meaning it waits until the buffer is full before writing to disk.
flush() pushes all unwritten data to the file without closing it."""
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
    file.flush()  # Immediately writes to the file without closing it
#Why use it? When you want to make sure the data is saved immediately (useful for logging or real-time writing).