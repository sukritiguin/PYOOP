"""

** Some points on Python class:

- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute

** object

* An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values.


** An object consists of:

- State: It is represented by the attributes of an object. It also reflects the properties of an object.
- Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
- Identity: It gives a unique name to an object and enables one object to interact with other objects.

** Self
Self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in Python.
It binds the attributes with the given arguments.
Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the “self” parameter. 

** [__init__]
? Use as constructor
? default funtion that calls automatically when object is created
* Conclusion
    So we can conclude that __init__ is not a private method, In Python, there’s nothing like private/protected by technique,
    it’s just a convention, and we can access private/protected methods. It’s more like a convention, rather than a technique.
    It is advised that we should follow this convention for better understanding.



"""


class Martine:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
    
    def displayDetails(self):
        print(f"Name : {self.first_name} {self.last_name} and DOB: {self.date_of_birth}")


m1 = Martine("Sukriti", "Guin", "28/11/2002")
m2 = Martine("Suman", "Chawal", "11/10/2010")

m1.displayDetails()
m2.displayDetails()

m3 = m2
m3.last_name = "Das"

print("========== After assigning m3 = m2 =================")
print(" -------- m2 object ----------------")
m2.displayDetails()
print(" -------- m3 object ----------------")
m3.displayDetails()