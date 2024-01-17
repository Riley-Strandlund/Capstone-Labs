"""
The dataclasses version of the code doesn't have an as lengthy variable assignment code like the traditional one.
def __init__(self, name, school_id, gpa):     
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

I like the dataclass one because you create a variable and decide its dataType instead of creating a variable then on another line deciding its dataType.
"""

from dataclasses import dataclass

@dataclass

class Student:
    name: str
    college_id: int
    gpa: float

    def __str__(self):
        return f"Name: {self.name}, College ID: {self.college_id}, GPA: {self.gpa}" # This isn't required to print the info, but it is prettier.

    
def main():
    alice = Student('Alice', 12345, 3.6)
    bob = Student('Bob', 98765, 2.5)
    print(alice)
    print(bob)

if __name__ == '__main__': # __name__ is built in variable. This bit is mainly for calling functions or partial stuff to another file.
    main()



# Below is the traditional not data class code.
    
class Student2: # both str and init require 'self' as the first argument in the function.
    def __init__(self, name, school_id, gpa):    # __init__ = initialize     
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self): # __str__ = returns a string of an object^
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'



alex = Student2('Alex', 'abcdef', 4.0)
print( alex.name)
print( alex ) # This accesses the '__str__' function in the object


sam = Student2('Sam', 'anasoidn', 2.3)
print( sam )

# Self is similar to 'this' in JavaScript
# Anything after 'self' is an attribute you want to add to the class
# For example a student would have a name, student id, GPA, and/or grade.
