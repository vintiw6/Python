tup = (1 , 5 , 3 , 6 , "Green" , True , "Red")
tuple1 = (0 , 1 , 2 , 3 , 2 , 3 , 1 , 3 , 2 ,1)

print(type(tup), tup)
print(tup[0])
print(tup[-2])
print(tup[3])

if 6 in tup:
    print("Yes 6 Present in this tuple")

# Tuples can be sliced as well
tup2 = tup[1:4]
print(tup2)


# Count Method
# USED TO COUNT ELEMENT
res = tuple1.count(3)
print('Count of 3 in tuple1 is: ',res)

# Index Method
ray = tuple1.index(3 , 4 , 8)
print('Count of 3 in tuple1 is: ',ray)

# Length of Tuple
len = len(tuple1)
print(len)