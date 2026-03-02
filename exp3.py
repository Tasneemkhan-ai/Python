#Aim: To calculate gross salary from basic salary, daily allowance, house rent allowance, travel allowance
#Coder: Tasnereem Khan
#Date: 17-01-2026
print("- Gross Salary Calculator-")
#To get base salary from user
bs=float(input("Enter your base salary:"))
print("Basic salary is",bs)
da=0.7*bs                #daily allowance
print("Daily allowance is ",da)
ta=0.3*bs                  #travel allowance
print("Travel allowance is",ta)
hra=0.1*bs                 #house rent allowance
print("House rent allowance is",hra)
gross_salary=bs+da+ta+hra     #calculation of gross salary
print("Gross salary is",gross_salary)
