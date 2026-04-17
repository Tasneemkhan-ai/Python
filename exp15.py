#Aim:Usng a debugger
#Name:Khan Tasneem
#Date:15-04-2026
import pdb
  
  print("Debugging Demonstration Program")
  
  def print_pattern(rows):
for i in range(rows):
          pdb.set_trace()    # breakpoint
          for j in range(i + 1):
              print("*", end="")
         print()
 print_pattern(5)
