def collatz(number):
    while (number!=1):
      if (number%2==0):
        print(number//2)
        return (collatz(number//2))
      else:
        print(3*number + 1)
        return (collatz(3*number + 1))

print("Enter number of operations")
n=int(input())
print("\n")

for i in range(0,n):
  print("Enter a number")
  try:
    number = int(input())
  
    collatz(number)
  except NameError:
    print("Please enter an integer")
    
