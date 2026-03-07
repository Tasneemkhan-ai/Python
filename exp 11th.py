#Aim:Simple python calculator using function
#Coder:Tasneem Khan
#Date:27-02-2026
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y!=0:
     return x/y
    else:
       print("Divide by zero is not possible")
print("---Simple calculator---\n" 
      "Choice of operations:+,-,*,/")
x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
choice=str(input("Enter choice of operation:"))
if choice=="+":
   print("Result=",add(x,y))
elif choice=="-":
   print("Result=",sub(x,y))
elif choice=="*":
   print("Result=",mul(x,y))
elif choice=="/":
   print("Result=",div(x,y))
else:
   print("Invalid Operator")
