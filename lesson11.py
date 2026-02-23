try:
    nummber = int(input("enter number: "))
    result = 10/number
    print("result:", result)
except:
    print("error!: you cannot divide by zero.")
try:
    nummber = int(input("enter number: "))
    print(20/number) 
except ZeroDivisionError:
    print("error!: divion by zero is not allowed.")
except ValueError:
    print("error!: please enter valid number!")
else:
    print("correct answer")
finally:
    print("calculation suvvessful!")

try:
    age = int(input("enter age: "))
    if age <= 0:
        raise ValueError
    print("your age is:", age)
except ValueError:
    print("Error!: please enter valid positive number!")
else:
    print("age accepted")
finally:
    ("thank you for using the program.")
