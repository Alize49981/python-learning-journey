{"name" : "Adan", 
 "age": 25,
 "skills": "electrician"}
import json
data = {"name": "Adan",
"age": 23,
"course": "eduation"}
with open("data.json", "w") as file:
    json.dump(data,file)

with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])

#csv
import csv
with open("students.csv", "w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "course"])
    writer.writerow(["Amina", 32, "medicine"])

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)