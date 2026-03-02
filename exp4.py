#Aim: To calculate simple interest
#Coder: Tasneem Khan 
#Date: 19-01-2026
print("---Simple Interest Calculator---")
#To take principal from the user
principal=float(input("Enter the principal:"))
#To take interest from the user
intrst=float(input("Enter the rate of interest:"))
#TO take time period from the user
time=float(input("Enter the time period(in years):"))
#formula of simple interest
SI=(principal*intrst*time)/100
print("Simple interst =",SI)