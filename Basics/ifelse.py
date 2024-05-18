a = int(input("Enter Your age: "))
print("Your age is",a)
if( a <= 10 ):
    print("You are a Kid")
elif( a <= 18 ):
    print("You are an Adult")
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


# We Can use else with for and while loop
for i in range(5):
    print(i)
else:
    print("No i present")  
# Note : it doesn't break the loop it ends there        