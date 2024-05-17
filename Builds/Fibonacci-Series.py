def FibonacciSeries(num):
  if num <= 1:
       return num
  else:
       return(FibonacciSeries(num-1) + FibonacciSeries(num-2))
  
n = input()
print("Fibonacci sequence:")
for i in range(int(n)):
    print(FibonacciSeries(i)) 

     