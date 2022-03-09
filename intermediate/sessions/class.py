from datetime import datetime
import re

class Detail():
    def __init__(self, created_on, updated_on):
        self.created_on = created_on
        self.updated_on = updated_on
    
    @property
    def created_on(self):
        print("Getting created_on")
        return self.__created_on

    @property
    def updated_on(self):
        print("Getting updated_on")
        return self.__updated_on

    @created_on.setter
    def created_on(self, value):
        print("Setting created_on")
        self.__created_on = value

    @updated_on.setter
    def updated_on(self, value):
        print("Setting updated_on")
        self.__updated_on = value

# The Person class inherts from Detail class
class Person(Detail):
    # Self is used to refer to the current instance of the class
    # Init is used to initialize the class
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}"

    # Properties are used to define the attributes of the class
    @property
    def first_name(self):
        print("Retrieving first name...")
        return self.__first_name
    
    @property
    def last_name(self):
        print("Retriving last name...")
        return self.__last_name


    @first_name.setter
    def first_name(self, value):
        print("Setting first name...")
        self.__first_name = value
    
    @last_name.setter
    def last_name(self, value):
        print("Setting last name...")
        self.__last_name = value

    def say_hello(self):
        print("Hello, " + self.first_name + " " + self.last_name)
    
    def get_first_name(self):
        print("first name is: " + self.first_name)

# the Student class inherts from Person class
# This is is called multi-level inheritance
class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        # The super() function is used to inherit the attributes of the parent class
        super().__init__(first_name, last_name)
        self.student_id = student_id

        # When a person is created the created and updated datetime is the same
        created_on = datetime.utcnow()
        updated_on = datetime.utcnow()
    
    def say_id(self):
        print("ID: " + self.student_id)



# Create an empty list
list = []

# Create a detail object
detail = Detail(datetime.now(), datetime.now())

# Create a person object
person = Person("John", "Doe")

# Create a student object by using [person] as the parent class
student = Student(person.first_name, person.last_name, "00001")

# Add the student object to the list
list.append(student)

# Create a new  person
person = Person("Jane", "Doe")
student = Student(person.first_name, person.last_name, "00002")

list.append(student)

print(person)










# student.say_id()
print(person.get_first_name())
# student.say_hello()

# To check if [student] is a childo of [Person]
print(isinstance(student, Person))

# To check if [student] is a child of [Student]
print(isinstance(student, Student))

# To check if [Student] is a child of [Person]
print(isinstance(Student, Person))