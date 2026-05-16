# len() gives total number of characters in string

fruit = "Mango"

mangoLen = len(fruit)
print(mangoLen)


# # string slicing
print(fruit[0:4])   # from index 0 to 3
print(fruit[1:4])   # from index 1 to 3
print(fruit[:5])    # automatically starts from 0
print(fruit[0:-3])  # negative slicing


# # using len() in slicing
print(fruit[0:len(fruit)-3])

# another negative slicing example
print(fruit[-1:len(fruit)-3])   
print(fruit[-3:-1])

nm = "harry"
print(nm[-4:-2])