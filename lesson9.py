students = {"Ali": 24,"Hasan": 25, "Abdi": 23}
print(students["Ali"])
print(students["Abdi"])
students["Usuf"] = 26 
print(students)
students.pop("Hasan")
print(students)
for key in students:
    print(key)
for value in students.values():
    print(value)

for key,value in students.items():
    print(key, ":", value)
students = {}
students["Ali"] = int(input("enter your age: "))
students["Abdi"] = int(input("enter your age: "))
students["Hasan"] = int(input("enter your age: "))
print("\nstudents detail:")
for key, value in students.items():
    print(key, ":", value)



student = ("Ali", 23, "Kenya")
print(student[0])
