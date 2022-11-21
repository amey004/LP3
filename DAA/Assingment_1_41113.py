#Amey Bhattad
#41113
#Printing fibonaaci series
#using Recursion
def fibonacciR(n):
    if n<=1:
        return n;
    return fibonacciR(n-1) + fibonacciR(n-2)

#using iteration Iteration
def fibonacci(n):
    f0 = 0
    f1 = 1
    if n<0:
        print("Invalid Input") 
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2, n+1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f1

x = int(input("0: Recursive method \n1: Iterative method\nEnter choice: "))
n = int(input("Enter n for n^th fibonacci number: "))

if x==0:
    print(fibonacciR(n))
elif x==1:
    print(fibonacci(n))
else:
    print("Invalid input")