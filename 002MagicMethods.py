"""

** Magic Methods
- In Python, magic methods, also known as dunder methods (short for "double underscore"), are special methods that begin and end with double underscores.
- These methods define how objects behave in certain situations or contexts. They are also called "special methods" or "special functions."
- Magic methods are automatically invoked by the Python interpreter in response to specific events or operations on objects.

** Points to remember about str and repr

* If __str__ is defined in a class and __repr__ is not, Python will use __str__ for both str() and print() operations.
* If __repr__ is defined and __str__ is not, Python will use __repr__ for str() and print() if __str__ is not available.

"""


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"x cordinate is {self.x} and y cordinate is {self.y}"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return 2
    
    def __iter__(self):
        return iter([self.x, self.y])
    
    def __getitem__(self, index):
        if index==0:return self.x
        elif index==1:return self.y
        else:
            raise IndexError("Index out of bound!")
    
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __add__(self, __value: object) -> object:
        return Vector(self.x + __value.x, self.y + __value.y)
    
    def __sub__(self, __value: object) -> object:
        return Vector(self.x - __value.x, self.y - __value.y)

v1 = Vector(2,3)
v2 = Vector(4,7)

print(f"Repr of v1: {repr(v1)}")
print(f"Repr of v2: {repr(v2)}")

print(f"Str of v1 : {str(v1)}")
print(f"Str of v2 : {str(v2)}")


# Iteration
print("Coordinates of v1 : ")
for coord in v1:
    print(coord)  # Output: 2, then 3

print(f"First index of v1 : {v1[0]}")
print(f"Second index of v2 : {v2[1]}")

print(f"Check v1 is equal to v2 or not ? : {v1==v2}")

print(f"Addition of v1 and v2 : {repr(v1+v2)}")

print(f"Substraction of v1 and v2 : {repr(v1-v2)}")



"""
In Python, the `__repr__` and `__str__` methods serve different purposes, and understanding when to use each is important for effective class design.
Here's a guideline on when to use `__repr__` and `__str__`:

* 1. **`__repr__`:**
   - **Purpose:** To provide a detailed, unambiguous representation of an object, primarily for developers and debugging.
   - **Use Cases:**
     - Debugging: When you want to see the internal state of an object for debugging purposes.
     - Development: During development, to get a comprehensive view of an object's content.
     - Unambiguous Representation: When the string returned by `__repr__` can be used to recreate the object using `eval()`.

   def __repr__(self):
       return f"ClassName(attribute1={self.attribute1}, attribute2={self.attribute2})"

2. **`__str__`:**
   - **Purpose:** To provide a readable, human-friendly representation of an object.
   - **Use Cases:**
     - End-User Output: When you want to display information about an object to end users or external systems.
     - Readability: For a more concise and user-friendly output compared to `__repr__`.
     - Customization: If you want to provide a different representation than what `__repr__` offers for casual display.

   
   def __str__(self):
       return f"{self.attribute1}, {self.attribute2}"
"""