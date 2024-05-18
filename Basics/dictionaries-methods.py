ep1 = { 122 : 45 , 123 : 89 , 567 : 69 , 
670 : 69}
ep2 = { 222 : 67 , 566 : 90 }
ep3 = ep1

# Update Method
ep1.update(ep2)
print(ep1)
# What it does is that it updates ep1 with the data of ep2


# Empty Dictionaries
empt = {}
print(empt)
# this Creates an Empty Dictionaries


# Pop-Method
print(ep2.pop(222))
# this rmeoves the specific given element


# Pop-Item Method
removed_pair = ep1.popitem()
print(ep1)  
print(removed_pair)
# this rmeoves the last element from the dictionary 


# Del keyword Used to delete the whole Dictionary
del ep1[122]


# Clear Method
ep3.clear()
print(ep3)
# This will clear all the elements in the dictionary


