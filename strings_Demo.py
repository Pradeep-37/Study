str="pradeep reddy.com"
str1="is a good boy"
str3="reddyi"


print(str[1])  # individual letters
print(str[0:8]) # to get a substring in python
print(str+' '+str1) # concatenation
print(str3 in str) # to check substring. This is very important in automation as we want to check some expected text in the output 

var=str.split(".")  # split a string into list. imp in automation to extract some text from output
print(var)
print(var[0])

str4=" great "
print(str4.strip())  # removes white spaces at begin and end of string
print(str4.lstrip())  # removes only left ie start white spaces
print(str4.rstrip())  # removes only right ie end white spaces
