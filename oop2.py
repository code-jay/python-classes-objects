class Employee:
    def __init__(barani, name, age):
        barani.name = name
        barani.age = age

    def __str__(self):
        return f"{self.name}"
    
    def myfunc(self):
        print("Hello My name is "+ self.name)

# object or instance
        
emp1 = Employee("Jay", 30)

emp2 = Employee("John", 12)


del emp1
print(emp2)
print(emp1)





