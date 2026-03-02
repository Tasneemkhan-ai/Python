#Aim:To manage task list using list and tuple
#Coder:Tasneem khan
#Date: 21-01-2026
print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(tasks)
newTask = input("Enter a new task to add: ")
tasks.append(newTask)    #to add an element
print("Tasks after Adding:",tasks)
num= int(input("Enter the index of the task to edit: "))  
newTask = input("Enter the new task: ")  #to edit an element
tasks[num] = newTask
print("Updated tasks:",tasks)
index = int(input("Enter the index of the task to remove: "))
tasks.pop(index)   #to remove the element
print("Tasks after Removing:",tasks)
tasks.sort()      #to sort out the list 
print(f"Tasks after Sorting: {tasks}")
