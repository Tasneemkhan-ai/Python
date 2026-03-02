#Aim:Use of sets and their operations
#Coder:Tasneem Khan
#Date: 23-01-2026
print("--- Students apperaing for JEE and CET and NEET ---")
JEE = {"Alina", "Aisha", "Zainab", "Sara", "Hina"}
print("Students who appeared for JEE:", JEE)
CET = {"Ali", "Aisha", "Zainab", "Sara", "Hina", "Sana"}
print("Students who appeared for CET:", CET)
NEET={"Alina", "Ali", "Zainab","Rahul", "Sara", "Hina", "Sana"}
print("Students who appeared for NEET:", NEET)
union_set = JEE.union(CET)    # Students who appeared either for JEE or CET
print("Students who appeared for JEE or CET:", union_set) 
intersection_set = JEE.intersection(CET)    # Students who appeared for both JEE and CET
print("Students who appeared for both JEE and CET:",intersection_set)
difference_set = JEE.union(NEET).difference(CET)   # Students who appeared for JEE and NEET but not CET
print("Students who appeared for JEE and NEET but not CET:", difference_set)
neet_only = NEET.difference(JEE.union(CET))   # Students who appeared for NEET but not JEE and CET
print("Students who only appeared for NEET but not JEE and CET:", neet_only)