# 1This is a comment
print("Hello, World!")

print("hey harry who are you?") #This is a comment


""" 2 to add a multiline comment you could
 insert a # for each line:
This is a comment
written in
more than just one line """

print("are i m harry and i a,m a student of python")

""" 3 you can add a multiline string (triple quotes) in your code,
and place your comment inside it:
"""
# ..................
"""
This is a comment
written in
more than just one line
"""
print("What is your name?")

    
#    Python Escape Characters
""" escape character allows you to 
  use double quotes when you normally 
  would not be allowed:"""

# \' -> Single Quote use karne ke liye
txt = 'It\'s a beautiful day'
print(txt)

# \\ -> Backslash print karne ke liye
txt = "This is a backslash: \\"
print(txt)

# \n -> New Line (next line me print karega)
txt = "Hello\nbro ki haal hai?"
print(txt)

# \r -> Carriage Return (line ke starting se overwrite karta hai)
txt = "Shri\rRadha!"
print(txt)

# \t -> Tab (space jaisa gap deta hai)
txt = "Name:\tShivam Rathore"
print(txt)

# \b -> Backspace (ek character hata deta hai)
txt = "SHRI \bRADHA!"
print(txt)

# \f -> Form Feed (rare use, page break jaisa behave karta hai)
txt = "hy bro\fwhere are you?"
print(txt)


# Python print()

# object(s) -> Jo bhi value print karni ho (multiple bhi de sakte hain)
print("Hello", "World", 123)

# sep -> Multiple values ke beech separator set karta hai (default = space)
print("Hello", "World", sep="-")
print("2026", "04", "24", sep="/")

# end -> Line ke end me kya print hoga (default = \n)
print("Hello", end=" ")
print("World")

# end ka custom use
print("Loading", end="...")
print("Done")

# sep + end together
print("A", "B", "C", sep="*", end=" END\n")



