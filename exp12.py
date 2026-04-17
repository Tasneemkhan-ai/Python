#Aim: Simple python calculator using function
#Coder: Tasneem Khan
#Date: 27-02-2026

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return "Divide by zero is not possible"
    return x/y

print("---Simple calculator---\n")
print("Choice of operations: +, -, *, /")
print("Type 'q' to quit")

while True:
    try:
        choice = input("\nEnter choice of operation: ")
        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice not in ['+','-','*','/']:
            print("Invalid Operator")
            continue
            
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        
        if choice == "+":
            print("Result =", add(x,y))
        elif choice == "-":
            print("Result =", sub(x,y))
        elif choice == "*":
            print("Result =", mul(x,y))
        elif choice == "/":
            print("Result =", div(x,y))
            
    except ValueError:
        print("Invalid input. Please enter numbers only.")
