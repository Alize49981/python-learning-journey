class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def get_grade(self):
        if self.marks >=80:
            return "A"
        elif self.marks >=60:
            return "B"
        elif self.marks >=40:
            return "C"
        else:
            return "fail"
s1 = student("Ali", 75)
s2 = student("Amina", 35)
print(s1.name, s1.get_grade())
print(s2.name, s2.get_grade())

class student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major =major
    def introduce(self):
        print(f"hi, i am learning {self.name},{self.age} years old, majoring in {self.major}")
class graduatestudent(student):
    def __init__(self, name, age, major, thesis_topic):
        super().__init__(name, age, major)
        self.thesis_topic = thesis_topic
    def introduce(self):
        print(f"hi, i am {self.name}, {self.age} years old, majoring in {self.major} .my thesis is on '{self.thesis_topic}.")
student1 =student("Ali", 23, "Computer science")
student2 =graduatestudent("Ahmed", 25, "History", "industrial revolution")
student1.introduce()
student2.introduce()
class car:
    def __init__(self, brand, color, model, year):
        self.brand = brand
        self.color = color
        self.model = model
        self.year = year
    def get_details(self):
        return f"{self.brand}, {self.color}, {self.model}, {self.year}"
car1 = car("Toyota", "red", "model 5", 2025)
print(car1.get_details())

class book:
    def __init__(self, name, title, author):
        self.name =name
        self.title = title
        self.author = author
    def book_info(self):
        return f"{self.name}, {self.title}, {self.author}"
bookA = book("IRE", "History of islam", "Dr. ALI")
print(bookA.book_info())

class phone:
    def __init__(self, name, brand, model, year):
        self.name = name
        self.brand = brand
        self.model = model
        self.year = year
    def get_details(self):
            return f"{self.name}, {self.brand}, {self.model}, {self.year}"
phonex = phone("iphone 17", "Apple", 17, 2026)
print(phonex.get_details())
        

        