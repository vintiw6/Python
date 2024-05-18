# Set Methods

s1 = { 1 , 2 , 3 , 4 }
s2 = { 3 , 4 , 7 , 9 }

# Creates a Union between Set1 and Set2
print(s1.union(s2))
# This doesn't update the Set1 or Set2

# To Update Any Set we 
s1.update(s2)
# This will add the elements which are unique to Set2 and add it to Set1





cities1 = { "Tokyo" , "Barcelona" , "Moscow" , "Delhi"}
cities2 = { "Tokyo" , "Madrid" , "Mumbai" , "Barcelona"}
cities3 = cities1.intersection(cities2)
cities4 = { "Barcelona" , "Moscow" , "Mumbai" }
# To add a new Element we use 
cities1.add("Manchester")

# To remove we can use both Remove/Discard methods
cities1.remove("Manchester")
cities1.discard("Manchester")
# Differnce is if we remove a null object we get an error


# If we qwant to remove all elements but keep an empty set we can use clear
cities4.clear()

# We can use Intersection will give us the common elements in both the sets
print(cities3)

# Symmetric Differnce Allows to give output of elements which arent common
print(cities1.symmetric_difference(cities2))

# Differnce only compare a single set from other set
print(cities1.difference(cities2))

# isDisJoint checks if both sets have no elements in common
print(cities1.isdisjoint(cities2))

# issuperset checks if the all the  elements of Set2 are already present in Set1 
print(cities1.issuperset(cities2))

# issubset checks if the elements of Set1 are present in Set2
print(cities3.issubset(cities1))

# pop removes the last element of the set tho it being unordered means it can remove any random element
cities4.pop

# we can delete entire Set by using del
del cities4