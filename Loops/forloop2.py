#1. Using a for loop print values for the dictionary below:


ll = int(input("Enter lower range limit"))
ul = int(input("Enter upper range limit"))

for x in range(ll, ul + 1):
    if x % 3 == 0 and x % 5 == 0:
       print("Fizzbuzz")
    elif x % 5 == 0:
         print("Buzz")
    elif x % 3 == 0:
         print("Fizz")
    else:
         print(x)









