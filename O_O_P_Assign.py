class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creates an instance of the Person class
person1 = Person("Clyde", 25, "male")

# Calls the introduce method to display the person's information
person1.introduce()