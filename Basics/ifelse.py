a = int(input("Enter Your age: "))
print("Your age is",a)
if(a<15):
    print("You are a teenager")
elif(a<=39):
    print("You are an adult")
else:
    print("You are an Senior Citizen")
    
    
# As we know previously we can use Nested loops in Python as well
num = int(input("Enter Your Number: "))
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10") 
    elif(num > 10 and num <= 50):
        print("Number is between 11-50")    
    else:
        print("Number is  Greater than 50")        
else:
    print("Number is greater than zero")        