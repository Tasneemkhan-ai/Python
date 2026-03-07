# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Tasneem Khan
# Date: 02-03-2026

print("--- Factorial Finder ---\n")


# Write your code here
n=int(input("Enter number:"))
fact = 1  #to avoid multiplication with zero
if n < 0:   #exception case for negative numbers
    print("Factorial is not defined ")
else:
    for i in range(1, n + 1):  #condition for factorial
        fact *= i
    print(f"The factorial of {n} is {fact}")
