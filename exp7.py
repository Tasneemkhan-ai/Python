# AIM: Write a Python program to create,
# update, and manipulate a dictionary of student records,
# including their grades and attendance.
# Coder: Tasneem Khan
# Date:02-03-2026

print("--- Student Records Manager ---")
students_records = {
    "251P005" : {"name":"Kawsar","grade":"A","attendance": 68},
    "251P055" : {"name":"Ayesha","grade":"B+","attendance": 88},
    "251P026" : {"name":"Arina","grade":"A-","attendance": 55},
}

print(f"Current Student Records: {students_records}")

# Write your code here
# TODO: Add a new Student Record 
new_uin = input("Enter New Student UIN:")
new_name = input("Enter New Student Name: ")
new_grade = input("Enter New Student Grade: ")
new_attendance = int(input("Enter New Student Attendance: "))
students_records[new_uin] = {"name":new_name,"grade":new_grade,"attendance":new_attendance}
# TODO: Update the Grade of Student of UIN 251P055
upg_uin = input("Enter UIN to Update: ")
upg_grade = input("Enter New Grade of Student: ")
students_records[upg_uin]["grade"] = upg_grade
# TODO: Remove Student with UIN 251P026
del_uin = input("Enter UIN of the Student to Delete: ")
del_students_records=[del_uin]
# Stop coding here
print(f"Final Student Records: {students_records}")