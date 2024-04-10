multiline = '''An example of multiple line 
string which is written as this'''

# String Slicing HowTo....

name = "Vinayak Tiwari"
print(len(name))
print(name[0:7])
print(name[9:14])
print(name[0:-3])

print(name[-4:-2])
# What's happening is that it deduces the no. from len of string
# Example [-4:-2] it implies that 14 - 4 = 10 & 14 - 2 = 12
# The code will run from name[10:12]

# String-Operations
# Note : Strings are Immutable
a = "!!!!Vinayak!!!!"
print(a.upper())
# Upper Case All Characters

print(a.lower())
# Lower Case All Characters 

print(a.strip("!"))
# removes Character passed inside Function

print(a.replace("Vinayak","Hello"))
# replaces the text to other given string

print(a.split(" "))
# splits the string



str1 = "Does it ends with a dollar $"
print(str1.endswith("$"))
# Checks whether the strings ends with given Characters

print(str1.find("it"))
# Finds The Given Input in The String

print(str1.title())
# Converts the First letter into Upper case


# CHECKING STRING AND ITS CHARACTERISTICS


print(str1.isalnum())
# Checks if the string is alphabetic and numerical

print(str1.islower())
# Checks if the string Characters are in lower cases

print(str1.isspace())
# Checks if the string has white space

print(str1.istitle())
# Checks if the First letter is in Upper case or not
