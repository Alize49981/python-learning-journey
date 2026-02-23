file = open("grade.txt", "w")
file.write("my name is Ali\n")
file.write("python is interesting\n")
file.close

file = open("grade.txt", "r")
content = file.read()
print(content)
file.close

with open("grade.txt", "w") as file:
    file.write("hd is my friend\n")
    file.write("ahmed\n")
with open("grade.txt", "a") as file:
    file.write("abdu\n")
with open("grade.txt", "r") as file:
    ("update file content:")
    print(file.read())

#error
try:
    number1 = int(input('enter number: '))
    number2 = int(input('enter number: '))
    print(number1 * number2)
except:
    print('error: cannot multiply by zero.')
