a = input("Enter the Number: ")
print(f"Multiplication tablle of {a} is: ")

# Try tell to check if the program is being run likely how dev thought of
try:
 for i in range (1 , 11):
    print(f"{int(a)} x {i} = {int(a)*i}")
# if its not what we want we use except    
except:
  print("Invalid Input")


try:
  num = int(input("Enter Yout Integer: "))
  a = [ 6 , 3 ]  
  print(a[num])
except ValueError:
  print("number entered isn't an integer. ") 
except IndexError:
  print("Index error")   