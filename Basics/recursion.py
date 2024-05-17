# A Common Example of Recursion Is Factorial Function 
# As we are calling the factorial function inside the function itself

def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num-1))
    
num = 5
print("Number = ", num)
print("Factorial = " ,factorial(num))    


