# Importing for further uses
from math import pi


# Function declaration
def AreaRectangle(a , b):
    area = a * b
    print(area)

def AreaCircle(a):
 area = pi * a * a
 print(area)
 
# What pass does is it makes us create a function which is empty
def AreaArea(a,b):
    pass
 
a = int(input("Enter The length: "))
b = int(input("Enter The Breadth: "))
AreaRectangle(a, b)

c = int(input("Enter the Radius of the Circle: "))
AreaCircle(c)
