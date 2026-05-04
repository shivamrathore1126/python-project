#  variables
# create a variable (text)
A = "Shivam"
print(A)

# create variables (numbers)
A = 10
B = 5
print(A + B)

# we can change the value type anytime
A = 10
B = "Hello"
print(B)

# assign multiple variables in one line
A, B, C = 1, 2, 3
print(A, B, C)

# assign same value to multiple variables
A = B = C = 100
print(A, B, C)

# datatypes
# string (text)
A = "Hello"
print( "the type of A is:", type(A))

# integer (whole number)
B = 10
print("the type of B is:", type(B))

# float (decimal number)
C = 10.5
print("the type of C is:", type(C))

# boolean (true or false)
D = True
print("the type of D is:", type(D))

# list tupal set dist
# list (multiple values)
list = ["apple", "banana", "mango"]
print("the type of list is:", type(list))

# tuple (cannot change)
tuple = ("apple", "banana", "mango")
print("the type of tuple is:", type(tuple))

# set (no duplicate values)
set = {"apple", "banana", "mango"}
print("the type of set is:", type(set))

# dictionary (key-value pair)
dictionary = {"name": "Shivam", "age": 18}
print("the type of dictionary is:", type(dictionary))