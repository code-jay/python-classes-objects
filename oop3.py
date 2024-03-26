class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, age, qualification, grade):
        Person.__init__(self, name, age)
        self.quali = qualification
        self.grade = grade

    def printAge(self):
        return self.age

    def printQualification(self):
        return self.quali

student1 = Student("Jay", 30, "BCA")

student1.printName()
print(student1.printAge())
print(student1.printQualification())

