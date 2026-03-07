# AIM: Write a Python program that takes two 
# numbers as input and performs division. 
# Implement exception handling to manage division 
# by zero and invalid input errors gracefully.
# Coder: Tasneem Khan
# Date: 16/02/2026

print("--- Basic Exception Handling ---\n")

try:
  a = float(input("Enter the first number: "))
  b = float(input("Enter the second number: "))
  result = a / b
  print(f"The result of {a} divided by {b} is: {result}")
except ZeroDivisionError:
  print("Error: You cannot divide by zero.")
except ValueError:
  print("Error: Invalid input. Please enter numeric values.")
else:
  print("Division performed successfully.")
finally:
  print("Program execution completed.")