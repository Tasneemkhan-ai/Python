#Aim:EMail and phone number validator
#Coder:Tasneem Khan
#Date:02-04-2026

import re
print("Phone number and Email validator")
phone_number=input("Enter your 10 digit mobile number:")
email_id=input("ENter your email id:")
phone_pattern=re.compile(r'^\d{10}$')
email_pattern=re.compile(r'^[a-zA-Z0-9._%+-]+@eng\.rizvi\.edu\.in$')
if phone_pattern.match(phone_number):
    print("Vaild Mobile phone number")
else:
    print("Inalid phone number")
if email_pattern.match(email_id):
    print("Vaild email id")
else:
    print("INvalid email id")
