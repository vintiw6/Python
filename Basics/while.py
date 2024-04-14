i = int(input("Enter The number: "))
while( i <= 38):
    i = int(input("Enter The number: "))
    print(i)
    i = i + 1

# Decrementing Loop
count = 5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("Out of the loop")

# Do-While Loop
user = True
while user:
  number = int(input("Enter a number (0 to quit): "))
  user = number != 0
  if number != 0:
    print(f"You entered: {number}")
print("Goodbye!")
