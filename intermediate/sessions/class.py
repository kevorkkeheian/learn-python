
class Person:
    
    # TODO 1: Create a constructor method
    def __init__(self, id, fname, lname, age):
        self.person_id = id
        self.first_name = fname
        self.last_name = lname
        self.age = age

    # TODO 2: Create a method to print the person's full name
    def full_name(self) -> str:
        # full_name = f"{self.first_name} {self.last_name}"
        # return full_name
        # return f"{self.first_name} {self.last_name}"
        return self.first_name + " " + self.last_name

        
        
    
# TODO 3: Create a class Student that inherits from Employee
class Employee():
    def __init__(self, id, fname, lname, age, sid, grade):
        self.employee_id = id
        self.first_name = fname
        self.last_name = lname
        self.student_id = sid
        self.grade = grade


# TODO 4: Create a person
p1 = Person(1, "John", "Doe", 30)
p2 = Person(2, "Jane", "Doe", 25)


# TODO 5: Print the person's full name
print(p1.full_name())
p1.first_name = "Kevork"
print(p1. first_name)


# TODO 6: Create a student
e1 = Employee(3, "John", "Doe", 30, "12345", "A")
e2 = Employee(4, "Jane", "Doe", 25, "54321", "B")



