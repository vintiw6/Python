#exponential: 3**3 ,meaning 3 to the power 3
print("** Available Operators **")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation\n")

a = input("Enter The value of First digit: ")
b = input("Enter The value of Second digit: ")
x = input("Enter The Operator: ")

if x == 1:
    result = a + b
elif x == 2:
    result = a - b
elif x == 3:
    result = a * b
elif x == 4:
    if b != 0:
        result = a / b
    else:
        print("Division by zero is not allowed.")
        result = "N/A"  
elif x == 5:
    result = a % b
elif x == 6:
    result = a ** b
else:
    print("An unexpected error occurred.")
    result = "N/A" 

print(a, {1: "+", 2: "-", 3: "*", 4: "/", 5: "%", 6: "**"}[int(x)], b, "=", result)