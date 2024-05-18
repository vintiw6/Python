# Dictionaries Is A Collection of Ordered Data 

dict = {
    "Name1" : "Vianyak" ,
    "Name2" : "Aditi" ,
    "Object" : "Fork" }
print(dict["Name1"])


# We can always use print(dict) to get the whole info
print(dict)


# Another way is to use 
print(dict.get(4))
#  In This method we give a key which doesnt exist gives backk answer as none


# We can use loops to get all the info in a systemic way
for key in dict.keys():
    print(dict[key])
# This will print all elements in the dictionary 


# We Use items to get the pairs of elements
print(dict.items())