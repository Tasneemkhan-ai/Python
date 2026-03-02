#Aim: To calculate simple interest
#Coder: Tasneem Khan 
#Date: 19-01-2026
print("---Simple Interest Calculator---")
principal=float(input("Enter the principal:"))    #To take principal from the user
intrst=float(input("Enter the rate of interest:"))   #To take interest from the user
time=float(input("Enter the time period(in years):"))    #TO take time period from the user
SI=(principal*intrst*time)/100                 #formula of simple interest
print("Simple interst =",SI)
