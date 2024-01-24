"""
** Destructor
- Destructors are called when an object gets destroyed.
- Python has a garbage collector that handles memory management automatically. 
- The __del__() method is a known as a destructor method in Python.
- It is called when all references to the object have been deleted i.e when an object is garbage collected. 

** Advantages of using destructors in Python:
* Automatic cleanup:
    Destructors provide automatic cleanup of resources used by an object when it is no longer needed.
    This can be especially useful in cases where resources are limited,
    or where failure to clean up can lead to memory leaks or other issues.
* Consistent behavior:
    Destructors ensure that an object is properly cleaned up,
    regardless of how it is used or when it is destroyed.
    This helps to ensure consistent behavior and can help to prevent bugs and other issues.
* Easy to use:
    Destructors are easy to implement in Python, and can be defined using the __del__() method.
* Supports object-oriented programming:
    Destructors are an important feature of object-oriented programming,
    and can be used to enforce encapsulation and other principles of object-oriented design.
* Helps with debugging:
    Destructors can be useful for debugging, as they can be used to trace the lifecycle of an object
    and determine when it is being destroyed.
"""

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("Destructor is called. Deleting the employee object.")
    
    def __str__(self):
        return self.name + " " + str(self.age) + "\n"

def create_employee_object(name, age):
    print("Creating Object.....")
    emp = Employee(name=name, age=age)
    print(str(emp))
    print("Getting out of scope of function...")

print("Start Program...")
create_employee_object("Sukriti Guin", 21)
print("End of program...")
