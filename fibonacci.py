# Author: Nguyen L.
# Date:   April 27th, 2020
# Given a number n, print the nth Fibonacci Number
# Algorithm: Fn = Fn-1 + Fn-2

# function to find nth fibonacci number
def findFibonacci(n):

    # go through statements
    if n < 0:
        print("THIS IS INCORRECT INPUT!")

    # seed values
    elif n == 0 or n == 1:
        return n
    else: 
        return findFibonacci(n-1) + findFibonacci(n-2)

n = int(input("Input n: "))
print(findFibonacci(n))

