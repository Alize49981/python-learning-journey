
age = int(input("enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")
    age = int(input("enter your age: "))
    if age >=18:
        print("you can vote")
    else:
        print("you cannot vote")

age = 20
if age >=18:
    print("you are an adult")

    age = int(input("enter age: "))
    if age >=18:
        print("Adult")
    else:
        print("Minor")


 
password = "1234" 
if password =="1234":
    print("access granted")
    username = input("enter username: ")
    password = input("enter password: ")
    if username =="Ali" and password =="1234":
        print("login successful")
    else:
        print("failed")