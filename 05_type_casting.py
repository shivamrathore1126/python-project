# Type casting means changing one data type into another

# Explicit Type Casting -> done by user manually

# convert string to integer
A = "11"
B = int(A)
print(B)

# convert integer to float
A = 26
B = float(A)
print (B)

# convert integer to string
A = 100 
B = str(A)
print (B)

# Imp0licit Type Casting -> done automatically by Python

# Python automatically converts int to float
A = 10
B = 5.5
C = A + B
print(C)

# result becomes float automatically
print(type(C))